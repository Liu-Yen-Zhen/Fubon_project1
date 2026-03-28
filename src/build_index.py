"""建立 chunks 向量索引（OpenAI Embeddings + FAISS）。"""

from __future__ import annotations

import argparse
import json
import logging
import os
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterator, Sequence

import numpy as np
from openai import OpenAI

try:
    import faiss
except ImportError as exc:  # pragma: no cover
    raise ImportError("找不到 faiss，請先安裝 faiss-cpu。") from exc

try:
    from .config import AppConfig, load_config
    from .utils import ensure_dir, utc_now_iso
except ImportError:  # pragma: no cover - 支援直接 `python src/build_index.py`
    from config import AppConfig, load_config  # type: ignore
    from utils import ensure_dir, utc_now_iso  # type: ignore


LOGGER = logging.getLogger(__name__)


def _missing_openai_key_error(project_root: Path) -> str:
    """缺少 OPENAI_API_KEY 時回傳可執行的錯誤訊息。"""
    env_path = project_root / ".env"
    return (
        "未讀到 OPENAI_API_KEY。\n"
        f"請在 {env_path} 設定：OPENAI_API_KEY=你的金鑰\n"
        "若尚未建立 .env，請先執行：cp .env.example .env"
    )


@dataclass(slots=True)
class IndexChunk:
    """索引 metadata 所需欄位。"""

    chunk_id: str
    page: int
    text: str
    source: str


def _setup_logging(level: str = "INFO") -> None:
    """初始化基本日誌格式。"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def _resolve_path(path: Path, project_root: Path) -> Path:
    """將 CLI 路徑正規化為絕對路徑（相對路徑以專案根目錄為基準）。"""
    if path.is_absolute():
        return path
    return project_root / path


def _batched(items: Sequence[str], batch_size: int) -> Iterator[list[str]]:
    """將序列分批。"""
    if batch_size <= 0:
        raise ValueError("batch_size 必須大於 0。")
    for start in range(0, len(items), batch_size):
        yield list(items[start : start + batch_size])


def load_chunks(chunks_path: Path) -> list[IndexChunk]:
    """讀取 `chunks.jsonl` 並驗證必要欄位。"""
    if not chunks_path.exists():
        raise FileNotFoundError(f"找不到 chunks 檔案：{chunks_path}")

    chunks: list[IndexChunk] = []
    with chunks_path.open("r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            raw = line.strip()
            if not raw:
                continue

            try:
                row = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ValueError(f"chunks 檔案 JSON 格式錯誤（line {line_no}）：{exc}") from exc

            chunk_id = str(row.get("chunk_id", "")).strip()
            text = str(row.get("text", "")).strip()
            source = str(row.get("source", "")).strip()

            if "page" in row:
                page = int(row["page"])
            elif "page_start" in row:
                page = int(row["page_start"])
            else:
                page = -1

            if not chunk_id:
                raise ValueError(f"line {line_no} 缺少 chunk_id")
            if not text:
                LOGGER.warning("line %s text 為空，已略過 chunk_id=%s", line_no, chunk_id)
                continue
            if not source:
                source = "unknown-source"

            chunks.append(IndexChunk(chunk_id=chunk_id, page=page, text=text, source=source))

    if not chunks:
        raise ValueError("未讀到任何可用 chunks。")

    LOGGER.info("已載入 chunks：%s 筆", len(chunks))
    return chunks


def _embed_batch_once(
    client: OpenAI,
    texts: Sequence[str],
    model_name: str,
) -> list[list[float]]:
    """單次呼叫 OpenAI Embeddings API。"""
    response = client.embeddings.create(
        model=model_name,
        input=list(texts),
    )
    data_sorted = sorted(response.data, key=lambda item: item.index)
    return [item.embedding for item in data_sorted]


def _embed_batch_with_retry(
    client: OpenAI,
    texts: Sequence[str],
    model_name: str,
    max_retries: int,
    retry_base_seconds: float = 1.5,
) -> list[list[float]]:
    """對單批資料做重試。"""
    if max_retries < 0:
        raise ValueError("max_retries 不可小於 0。")

    for attempt in range(max_retries + 1):
        try:
            return _embed_batch_once(client=client, texts=texts, model_name=model_name)
        except Exception as exc:  # pragma: no cover - 依外部 API 與網路狀況而定
            if attempt >= max_retries:
                raise RuntimeError(f"Embedding 批次失敗（已重試 {max_retries} 次）：{exc}") from exc
            sleep_seconds = retry_base_seconds * (2**attempt)
            LOGGER.warning(
                "Embedding 批次失敗，%s 秒後重試（%s/%s）：%s",
                round(sleep_seconds, 2),
                attempt + 1,
                max_retries,
                exc,
            )
            time.sleep(sleep_seconds)

    raise RuntimeError("Embedding 批次失敗：未知錯誤。")


def embed_texts(
    texts: Sequence[str],
    model_name: str,
    batch_size: int,
    max_retries: int,
    client: OpenAI | None = None,
) -> list[list[float]]:
    """將文字分批轉成向量（獨立函式，方便未來替換模型）。"""
    if not texts:
        return []

    api_client = client or OpenAI()
    vectors: list[list[float]] = []

    total_batches = (len(texts) + batch_size - 1) // batch_size
    for batch_idx, batch in enumerate(_batched(texts, batch_size=batch_size), start=1):
        batch_vectors = _embed_batch_with_retry(
            client=api_client,
            texts=batch,
            model_name=model_name,
            max_retries=max_retries,
        )
        vectors.extend(batch_vectors)
        LOGGER.info("Embedding 進度：%s/%s batches", batch_idx, total_batches)

    return vectors


def build_vector_index(vectors: Sequence[Sequence[float]]) -> faiss.Index:
    """建立 FAISS IndexFlatIP（先正規化，近似 cosine similarity）。"""
    if not vectors:
        raise ValueError("vectors 為空，無法建立索引。")

    matrix = np.asarray(vectors, dtype=np.float32)
    if matrix.ndim != 2:
        raise ValueError(f"vectors 維度錯誤：{matrix.shape}")

    faiss.normalize_L2(matrix)
    dimension = int(matrix.shape[1])
    index = faiss.IndexFlatIP(dimension)
    index.add(matrix)
    LOGGER.info("FAISS 索引建立完成：ntotal=%s, dim=%s", index.ntotal, dimension)
    return index


def save_index_bundle(
    index: faiss.Index,
    chunks: Sequence[IndexChunk],
    output_dir: Path,
    embedding_model: str,
) -> Path:
    """輸出索引與 metadata 到指定資料夾。"""
    ensure_dir(output_dir)

    index_path = output_dir / "faiss.index"
    metadata_path = output_dir / "metadata.jsonl"
    manifest_path = output_dir / "index_manifest.json"

    faiss.write_index(index, str(index_path))

    with metadata_path.open("w", encoding="utf-8") as file:
        for chunk in chunks:
            file.write(json.dumps(asdict(chunk), ensure_ascii=False) + "\n")

    manifest = {
        "created_at_utc": utc_now_iso(),
        "embedding_model": embedding_model,
        "metric": "cosine_via_ip_with_l2_norm",
        "vector_count": int(index.ntotal),
        "dimension": int(index.d),
        "files": {
            "index": index_path.name,
            "metadata": metadata_path.name,
        },
    }
    with manifest_path.open("w", encoding="utf-8") as file:
        json.dump(manifest, file, ensure_ascii=False, indent=2)

    LOGGER.info("索引輸出完成：%s", output_dir)
    return output_dir


def run_index_build(
    config: AppConfig,
    chunks_path: Path,
    output_dir: Path,
    batch_size: int,
    max_retries: int,
) -> Path:
    """建置索引主流程。"""
    chunks = load_chunks(chunks_path)
    vectors = embed_texts(
        texts=[item.text for item in chunks],
        model_name=config.embedding_model,
        batch_size=batch_size,
        max_retries=max_retries,
    )
    if len(vectors) != len(chunks):
        raise RuntimeError("Embedding 數量與 chunks 數量不一致。")

    index = build_vector_index(vectors=vectors)
    return save_index_bundle(
        index=index,
        chunks=chunks,
        output_dir=output_dir,
        embedding_model=config.embedding_model,
    )


def _build_arg_parser(config: AppConfig) -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    default_chunks_path = Path(os.getenv("CHUNKS_PATH", "data/processed/chunks.jsonl"))
    default_output_dir = Path(os.getenv("INDEX_DIR", str(config.index_dir)))
    default_batch_size = int(os.getenv("EMBEDDING_BATCH_SIZE", "32"))
    default_max_retries = int(os.getenv("EMBEDDING_MAX_RETRIES", "3"))

    parser = argparse.ArgumentParser(description="建立年報 chunks 向量索引（OpenAI + FAISS）")
    parser.add_argument(
        "--chunks-path",
        type=Path,
        default=default_chunks_path,
        help="chunks JSONL 路徑",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_output_dir,
        help="索引輸出資料夾",
    )
    parser.add_argument(
        "--embedding-model",
        type=str,
        default=None,
        help="Embedding 模型名稱（未指定則使用 .env 的 EMBEDDING_MODEL）",
    )
    parser.add_argument("--batch-size", type=int, default=default_batch_size, help="Embedding 批次大小")
    parser.add_argument("--max-retries", type=int, default=default_max_retries, help="每批最大重試次數")
    parser.add_argument("--log-level", type=str, default="INFO", help="日誌層級")
    return parser


def main() -> int:
    """命令列入口。"""
    config = load_config()
    parser = _build_arg_parser(config)
    args = parser.parse_args()
    _setup_logging(level=args.log_level)

    try:
        openai_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not openai_key or openai_key.startswith("your_"):
            raise ValueError(_missing_openai_key_error(config.project_root))
        if args.batch_size <= 0:
            raise ValueError("--batch-size 必須大於 0。")
        if args.max_retries < 0:
            raise ValueError("--max-retries 不可小於 0。")

        if args.embedding_model:
            config.embedding_model = args.embedding_model

        chunks_path = _resolve_path(args.chunks_path, config.project_root)
        output_dir = _resolve_path(args.output_dir, config.project_root)
        LOGGER.info("chunks_path: %s", chunks_path)
        LOGGER.info("index_output_dir: %s", output_dir)

        output_dir = run_index_build(
            config=config,
            chunks_path=chunks_path,
            output_dir=output_dir,
            batch_size=args.batch_size,
            max_retries=args.max_retries,
        )
        LOGGER.info("完成：%s", output_dir)
        return 0
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        LOGGER.error("%s", exc)
        return 1
    except Exception as exc:  # pragma: no cover
        LOGGER.exception("建立索引失敗：%s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
