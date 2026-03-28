"""年報 PDF 文字抽取、清理與切片。"""

from __future__ import annotations

import argparse
import json
import logging
import re
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader

try:
    from .config import AppConfig, load_config
except ImportError:  # pragma: no cover - 支援直接 `python src/ingest_pdf.py`
    from config import AppConfig, load_config  # type: ignore


LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class ChunkRecord:
    """可寫入 JSONL 的切片資料。"""

    chunk_id: str
    page: int
    text: str
    source: str


def _setup_logging(level: str = "INFO") -> None:
    """初始化簡單日誌格式。"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def extract_pages(pdf_path: Path) -> list[tuple[int, str]]:
    """抽取 PDF 每頁文字，並保留頁碼。"""
    if not pdf_path.exists():
        raise FileNotFoundError(f"找不到 PDF：{pdf_path}")

    pages: list[tuple[int, str]] = []
    reader = PdfReader(str(pdf_path))
    for idx, page in enumerate(reader.pages, start=1):
        try:
            raw_text = page.extract_text() or ""
            pages.append((idx, raw_text))
        except Exception as exc:  # pragma: no cover - 依 PDF 品質而異
            LOGGER.warning("第 %s 頁抽取失敗：%s", idx, exc)
            pages.append((idx, ""))

    LOGGER.info("PDF 抽取完成：共 %s 頁", len(pages))
    return pages


def _is_noise_line(line: str) -> bool:
    """判斷是否為常見頁首頁尾雜訊。"""
    patterns = [
        r"^\d{1,4}$",
        r"^\d{1,4}\s*/\s*\d{1,4}$",
        r"^第\s*\d+\s*頁$",
        r"^Page\s*\d+$",
        r"^頁次[:：]?\s*\d+$",
    ]
    return any(re.match(pattern, line, flags=re.IGNORECASE) for pattern in patterns)


def _detect_common_border_lines(pages: Iterable[tuple[int, str]]) -> set[str]:
    """抓出跨頁重複出現的頁首頁尾文字，作為清理名單。"""
    candidates: Counter[str] = Counter()
    pages_list = list(pages)

    for _, raw_text in pages_list:
        lines = [line.strip() for line in raw_text.replace("\r", "\n").split("\n") if line.strip()]
        if not lines:
            continue

        border_lines = lines[:2] + lines[-2:]
        for line in border_lines:
            if 2 <= len(line) <= 40:
                candidates[line] += 1

    min_repeat = max(5, int(len(pages_list) * 0.08))
    return {line for line, count in candidates.items() if count >= min_repeat}


def normalize_page_text(text: str, common_noise_lines: set[str] | None = None) -> str:
    """清理頁面文字（換行、空白與常見雜訊）。"""
    normalized = text.replace("\u3000", " ").replace("\xa0", " ")
    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in normalized.split("\n")]

    clean_lines: list[str] = []
    for line in lines:
        if not line:
            continue
        if _is_noise_line(line):
            continue
        if common_noise_lines and line in common_noise_lines:
            continue
        line = re.sub(r"\s{2,}", " ", line)
        clean_lines.append(line)

    merged = "\n".join(clean_lines)
    merged = re.sub(r"[ \t]{2,}", " ", merged)
    merged = re.sub(r"\n{3,}", "\n\n", merged)
    return merged.strip()


def _hard_split(text: str, max_chars: int) -> list[str]:
    """將過長文字以標點優先策略切成較短片段。"""
    if len(text) <= max_chars:
        return [text]

    results: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            window = text[start:end]
            cut = max(
                window.rfind("。"),
                window.rfind("；"),
                window.rfind("！"),
                window.rfind("？"),
                window.rfind("，"),
                window.rfind("、"),
                window.rfind(" "),
            )
            if cut >= max_chars // 3:
                end = start + cut + 1

        part = text[start:end].strip()
        if part:
            results.append(part)
        start = end

    return results


def _split_sentences(text: str, max_unit_chars: int) -> list[str]:
    """以換行與標點為主切段，並保證單段不過長。"""
    units: list[str] = []
    for paragraph in re.split(r"\n+", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        sentence_like = re.split(r"(?<=[。！？!?；;])\s*", paragraph)
        for segment in sentence_like:
            segment = segment.strip()
            if not segment:
                continue
            units.extend(_hard_split(segment, max_chars=max_unit_chars))
    return units


def _build_overlapped_seed(text: str, chunk_overlap: int) -> str:
    """從前一段尾端建立 overlap 種子。"""
    if chunk_overlap <= 0 or not text:
        return ""
    seed = text[-chunk_overlap:].strip()
    return seed


def _chunk_single_page(
    page: int,
    text: str,
    chunk_size: int,
    chunk_overlap: int,
    source_name: str,
) -> list[ChunkRecord]:
    """將單頁內容切成多個 chunk。"""
    max_unit_chars = max(220, int(chunk_size * 0.8))
    sentences = _split_sentences(text=text, max_unit_chars=max_unit_chars)
    if not sentences:
        return []

    page_chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for sentence in sentences:
        sentence_len = len(sentence)
        projected = current_len + sentence_len + (1 if current else 0)
        if projected <= chunk_size or not current:
            current.append(sentence)
            current_len = projected
            continue

        chunk_text = " ".join(current).strip()
        if chunk_text:
            page_chunks.append(chunk_text)

        seed = _build_overlapped_seed(chunk_text, chunk_overlap)
        current = [seed, sentence] if seed else [sentence]
        current_len = sum(len(s) for s in current) + max(0, len(current) - 1)

    if current:
        chunk_text = " ".join(current).strip()
        if chunk_text:
            page_chunks.append(chunk_text)

    # 合併過短片段，避免切太碎
    merged_chunks: list[str] = []
    min_chunk_chars = max(180, chunk_size // 4)
    max_merge_chars = int(chunk_size * 1.5)
    for chunk_text in page_chunks:
        if merged_chunks and len(chunk_text) < min_chunk_chars:
            candidate = f"{merged_chunks[-1]} {chunk_text}".strip()
            if len(candidate) <= max_merge_chars:
                merged_chunks[-1] = candidate
                continue
        merged_chunks.append(chunk_text)

    records: list[ChunkRecord] = []
    for idx, chunk_text in enumerate(merged_chunks, start=1):
        records.append(
            ChunkRecord(
                chunk_id=f"{source_name}-p{page:04d}-c{idx:03d}",
                page=page,
                text=chunk_text,
                source=f"{source_name}#page={page}",
            )
        )
    return records


def chunk_pages(
    pages: list[tuple[int, str]],
    chunk_size: int,
    chunk_overlap: int,
    source_name: str,
) -> list[ChunkRecord]:
    """將頁面文字切成適合檢索的 chunk。"""
    records: list[ChunkRecord] = []
    for page, text in pages:
        if not text:
            continue
        records.extend(
            _chunk_single_page(
                page=page,
                text=text,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                source_name=source_name,
            )
        )
    LOGGER.info("切片完成：共 %s 個 chunks", len(records))
    return records


def ingest_pdf(config: AppConfig, pdf_path: Path | None = None) -> list[ChunkRecord]:
    """執行 ingest：抽取 -> 清理 -> 切片。"""
    target_pdf = pdf_path or config.pdf_path
    raw_pages = extract_pages(target_pdf)
    common_noise_lines = _detect_common_border_lines(raw_pages)

    cleaned_pages: list[tuple[int, str]] = []
    for page, raw_text in raw_pages:
        cleaned_text = normalize_page_text(raw_text, common_noise_lines=common_noise_lines)
        if cleaned_text:
            cleaned_pages.append((page, cleaned_text))

    LOGGER.info("清理後有效頁數：%s", len(cleaned_pages))
    return chunk_pages(
        pages=cleaned_pages,
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
        source_name=target_pdf.name,
    )


def save_ingest_output(chunks: list[ChunkRecord], output_path: Path) -> Path:
    """將切片輸出為 JSONL。"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for chunk in chunks:
            file.write(json.dumps(asdict(chunk), ensure_ascii=False) + "\n")
    LOGGER.info("已輸出 chunks：%s", output_path)
    return output_path


def _build_arg_parser() -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    parser = argparse.ArgumentParser(description="富邦金控年報 PDF ingest")
    parser.add_argument("--pdf-path", type=Path, default=Path("113年報.pdf"), help="PDF 檔案路徑")
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("data/processed/chunks.jsonl"),
        help="chunks JSONL 輸出路徑",
    )
    parser.add_argument("--chunk-size", type=int, default=800, help="每個 chunk 目標字元數")
    parser.add_argument("--chunk-overlap", type=int, default=120, help="相鄰 chunk 重疊字元數")
    parser.add_argument("--log-level", type=str, default="INFO", help="日誌層級")
    return parser


def main() -> int:
    """命令列入口。"""
    parser = _build_arg_parser()
    args = parser.parse_args()
    _setup_logging(args.log_level)

    try:
        if args.chunk_size <= 0:
            raise ValueError("--chunk-size 必須大於 0")
        if args.chunk_overlap < 0:
            raise ValueError("--chunk-overlap 不可為負數")
        if args.chunk_overlap >= args.chunk_size:
            LOGGER.warning(
                "--chunk-overlap (%s) 大於或等於 chunk-size (%s)，將自動調整為 chunk-size 的一半。",
                args.chunk_overlap,
                args.chunk_size,
            )
            args.chunk_overlap = args.chunk_size // 2

        config = load_config()
        config.pdf_path = args.pdf_path
        config.chunk_size = args.chunk_size
        config.chunk_overlap = args.chunk_overlap

        chunks = ingest_pdf(config=config, pdf_path=args.pdf_path)
        if not chunks:
            LOGGER.warning("未產生任何 chunks，請檢查 PDF 是否可抽取文字。")
        save_ingest_output(chunks=chunks, output_path=args.output_path)
        return 0
    except FileNotFoundError as exc:
        LOGGER.error("%s", exc)
        return 1
    except ValueError as exc:
        LOGGER.error("%s", exc)
        return 1
    except Exception as exc:  # pragma: no cover - 實務錯誤保底
        LOGGER.exception("ingest 失敗：%s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
