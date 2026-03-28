"""本地向量索引檢索模組。"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import unicodedata
from pathlib import Path
from typing import Any, Sequence

import numpy as np
from openai import OpenAI

try:
    import faiss
except ImportError as exc:  # pragma: no cover
    raise ImportError("找不到 faiss，請先安裝 faiss-cpu。") from exc

try:
    from .config import AppConfig, load_config
    from .utils import RetrievedChunk
except ImportError:  # pragma: no cover - 支援直接 `python src/retrieve.py`
    from config import AppConfig, load_config  # type: ignore
    from utils import RetrievedChunk  # type: ignore


LOGGER = logging.getLogger(__name__)

_QUERY_STOPWORDS = {
    "請問",
    "請",
    "根據",
    "是否",
    "多少",
    "為何",
    "多少錢",
    "是什麼",
    "什麼",
    "以及",
    "還有",
    "關於",
    "年度",
    "年報",
    "公司",
    "資料",
    "請比較",
}

_QUERY_ALIAS_MAP = {
    "北富銀": "台北富邦銀行",
    "前度": "年度",
    "fyp": "初年度保費收入",
    "ifrs-17": "ifrs 17",
}


def _missing_openai_key_error() -> str:
    """缺少 OPENAI_API_KEY 時回傳可執行的錯誤訊息。"""
    project_root = Path(__file__).resolve().parents[1]
    env_path = project_root / ".env"
    return (
        "未讀到 OPENAI_API_KEY。\n"
        f"請在 {env_path} 設定：OPENAI_API_KEY=你的金鑰\n"
        "若尚未建立 .env，請先執行：cp .env.example .env"
    )


def _setup_logging(level: str = "INFO") -> None:
    """初始化日誌。"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def _resolve_path(path: Path, project_root: Path) -> Path:
    """將路徑正規化為絕對路徑（相對路徑以專案根目錄為基準）。"""
    if path.is_absolute():
        return path
    return project_root / path


def _load_manifest(index_dir: Path) -> dict[str, Any]:
    """讀取索引 manifest（若存在）。"""
    manifest_path = index_dir / "index_manifest.json"
    if not manifest_path.exists():
        return {}

    with manifest_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _resolve_index_dir(config: AppConfig, override: Path | None = None) -> Path:
    """決定檢索使用的索引資料夾。"""
    candidates: list[Path] = []
    if override is not None:
        candidates.append(_resolve_path(override, config.project_root))

    candidates.append(config.index_dir)
    candidates.append(config.output_dir)

    # 去重複，維持順序
    unique_candidates: list[Path] = []
    seen: set[str] = set()
    for directory in candidates:
        key = str(directory.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique_candidates.append(directory)

    for directory in unique_candidates:
        if (directory / "faiss.index").exists():
            return directory

    searched_files = [str(directory / "faiss.index") for directory in unique_candidates]
    raise FileNotFoundError(
        "找不到索引檔。已搜尋："
        + ", ".join(searched_files)
        + "。請先執行：python src/build_index.py --chunks-path data/processed/chunks.jsonl --output-dir outputs"
    )


def load_index_bundle(index_dir: Path) -> tuple[Any, list[dict[str, Any]]]:
    """讀取本地 FAISS 索引與 metadata。"""
    manifest = _load_manifest(index_dir)
    files_meta = manifest.get("files", {}) if isinstance(manifest, dict) else {}
    index_name = str(files_meta.get("index", "faiss.index"))
    metadata_name = str(files_meta.get("metadata", "metadata.jsonl"))

    index_path = index_dir / index_name
    metadata_path = index_dir / metadata_name

    if not index_path.exists():
        raise FileNotFoundError(f"找不到索引檔：{index_path}")
    if not metadata_path.exists():
        raise FileNotFoundError(f"找不到 metadata 檔：{metadata_path}")

    index = faiss.read_index(str(index_path))
    metadata: list[dict[str, Any]] = []
    with metadata_path.open("r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            raw = line.strip()
            if not raw:
                continue
            try:
                metadata.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise ValueError(f"metadata JSON 格式錯誤（line {line_no}）：{exc}") from exc

    if int(index.ntotal) != len(metadata):
        LOGGER.warning("索引向量數 (%s) 與 metadata 筆數 (%s) 不一致。", index.ntotal, len(metadata))

    return index, metadata


def _get_query_embedding_model(config: AppConfig, index_dir: Path) -> str:
    """優先以 manifest 設定的模型做 query embedding。"""
    manifest = _load_manifest(index_dir)
    model = str(manifest.get("embedding_model", "")).strip() if isinstance(manifest, dict) else ""
    if model:
        return model
    return config.embedding_model


def embed_query(query: str, model_name: str) -> list[float]:
    """將使用者問題轉成查詢向量。"""
    cleaned_query = query.strip()
    if not cleaned_query:
        raise ValueError("query 不可為空。")

    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not openai_key or openai_key.startswith("your_"):
        raise ValueError(_missing_openai_key_error())

    client = OpenAI()
    response = client.embeddings.create(model=model_name, input=[cleaned_query])
    return list(response.data[0].embedding)


def search_top_k(
    index: Any,
    query_vector: Sequence[float],
    top_k: int,
) -> list[tuple[int, float]]:
    """於向量索引查詢 Top-K 候選（score 越高越相關）。"""
    if top_k <= 0:
        raise ValueError("top_k 必須大於 0。")

    query_matrix = np.asarray([query_vector], dtype=np.float32)
    if query_matrix.ndim != 2:
        raise ValueError("query_vector 維度錯誤。")
    faiss.normalize_L2(query_matrix)

    scores, positions = index.search(query_matrix, top_k)
    results: list[tuple[int, float]] = []
    for pos, score in zip(positions[0], scores[0]):
        if int(pos) < 0:
            continue
        results.append((int(pos), float(score)))
    return results


def _normalize_text(text: str) -> str:
    """將文字正規化以便做簡單詞面比對。"""
    normalized = unicodedata.normalize("NFKC", text or "").lower()
    return re.sub(r"\s+", " ", normalized).strip()


def _extract_query_terms(question: str) -> list[str]:
    """抽取 query 的關鍵詞，用於二次排序。"""
    raw = unicodedata.normalize("NFKC", question or "")
    lowered = raw.lower()

    terms: list[str] = []
    terms.extend(re.findall(r"[a-z][a-z0-9\-]{1,}", lowered))
    terms.extend(re.findall(r"\d+(?:\.\d+)?%?", lowered))
    cjk_phrases = re.findall(r"[\u4e00-\u9fff]{2,}", lowered)

    for phrase in cjk_phrases:
        parts = re.split(r"(?:以及|與|和|及|的|在|於|之|請|根據|比較|多少|為何|是否)", phrase)
        for part in parts:
            cleaned = part.strip()
            if len(cleaned) < 2:
                continue
            if cleaned in _QUERY_STOPWORDS:
                continue
            terms.append(cleaned)

    # 常見財務縮寫給較高辨識權重
    for acronym in re.findall(r"[A-Z]{2,8}", raw):
        terms.append(acronym.lower())

    deduped: list[str] = []
    seen: set[str] = set()
    for term in terms:
        if term in seen:
            continue
        seen.add(term)
        deduped.append(term)
    return deduped


def _expand_query_aliases(question: str) -> str:
    """擴展常見別名與錯別字，提升召回。"""
    expanded = question
    for src, dst in _QUERY_ALIAS_MAP.items():
        expanded = expanded.replace(src, dst)
        expanded = expanded.replace(src.upper(), dst.upper())
    return expanded


def _lexical_overlap_score(question_terms: Sequence[str], chunk_text: str) -> float:
    """計算 query 與 chunk 的詞面重疊分數（0~1）。"""
    if not question_terms:
        return 0.0

    normalized_chunk = _normalize_text(chunk_text)
    matched = sum(1 for term in question_terms if term and term in normalized_chunk)
    score = matched / max(len(question_terms), 1)

    acronym_bonus_terms = {"roa", "roe", "car", "eps", "ifrs", "tw-ics", "fyp"}
    bonus_hits = sum(1 for term in question_terms if term in acronym_bonus_terms and term in normalized_chunk)
    score += min(0.15, bonus_hits * 0.05)
    return min(score, 1.0)


def _text_signature(text: str, prefix_len: int = 180) -> str:
    """產生用於去重的文字簽名。"""
    normalized = _normalize_text(text)
    normalized = re.sub(r"[，,。．.;；:：、!?！？\"'`“”‘’()\[\]{}（）【】《》<>]", "", normalized)
    return normalized[:prefix_len]


def _rerank_candidates(
    *,
    question: str,
    pairs: Sequence[tuple[int, float]],
    metadata: Sequence[dict[str, Any]],
    threshold: float,
    target_top_k: int,
) -> list[dict[str, Any]]:
    """以向量分數 + 詞面重疊進行二次排序，並做重複內容去除。"""
    query_terms = _extract_query_terms(question)
    candidates: list[dict[str, Any]] = []

    for chunk_pos, vector_score in pairs:
        if chunk_pos < 0 or chunk_pos >= len(metadata):
            continue

        item = metadata[chunk_pos]
        text = str(item.get("text", ""))
        if not text.strip():
            continue

        lexical_score = _lexical_overlap_score(query_terms, text)
        # 以向量相似度為主，詞面命中為輔，降低關鍵詞題目的漏召回。
        combined_score = (0.82 * float(vector_score)) + (0.18 * lexical_score)

        keep_by_vector = float(vector_score) >= threshold
        keep_by_lexical = lexical_score >= 0.45 and float(vector_score) >= max(0.05, threshold - 0.15)
        if not (keep_by_vector or keep_by_lexical):
            continue

        candidates.append(
            {
                "chunk_pos": int(chunk_pos),
                "vector_score": float(vector_score),
                "lexical_score": float(lexical_score),
                "combined_score": float(combined_score),
                "item": item,
            }
        )

    candidates.sort(
        key=lambda row: (
            row["combined_score"],
            row["vector_score"],
            row["lexical_score"],
        ),
        reverse=True,
    )

    deduped: list[dict[str, Any]] = []
    seen_signatures: set[str] = set()
    seen_chunk_ids: set[str] = set()
    for row in candidates:
        item = row["item"]
        chunk_id = str(item.get("chunk_id", ""))
        if chunk_id and chunk_id in seen_chunk_ids:
            continue

        signature = _text_signature(str(item.get("text", "")))
        if signature and signature in seen_signatures:
            continue

        if chunk_id:
            seen_chunk_ids.add(chunk_id)
        if signature:
            seen_signatures.add(signature)
        deduped.append(row)
        if len(deduped) >= target_top_k:
            break

    return deduped


def _lexical_search_over_metadata(
    *,
    question: str,
    metadata: Sequence[dict[str, Any]],
    top_n: int,
) -> list[dict[str, Any]]:
    """在整份 metadata 上做詞面搜尋，作為向量檢索失效時的 fallback。"""
    query_terms = _extract_query_terms(question)
    if not query_terms:
        return []

    candidates: list[dict[str, Any]] = []
    for chunk_pos, item in enumerate(metadata):
        text = str(item.get("text", ""))
        if not text.strip():
            continue
        lexical_score = _lexical_overlap_score(query_terms, text)
        if lexical_score <= 0:
            continue
        candidates.append(
            {
                "chunk_pos": int(chunk_pos),
                "vector_score": 0.0,
                "lexical_score": float(lexical_score),
                "combined_score": float(lexical_score * 0.35),
                "item": item,
            }
        )

    candidates.sort(key=lambda row: row["lexical_score"], reverse=True)
    return candidates[:top_n]


def retrieve_chunks(
    config: AppConfig,
    question: str,
    top_k: int | None = None,
    *,
    index_dir: Path | None = None,
    min_score: float | None = None,
) -> list[RetrievedChunk]:
    """整合檢索流程，回傳符合門檻的 chunks。"""
    target_top_k = top_k or config.top_k
    if target_top_k <= 0:
        raise ValueError("top_k 必須大於 0。")

    target_dir = _resolve_index_dir(config=config, override=index_dir)
    index, metadata = load_index_bundle(target_dir)
    model_name = _get_query_embedding_model(config=config, index_dir=target_dir)
    normalized_question = _expand_query_aliases(question)
    query_vector = embed_query(normalized_question, model_name=model_name)
    search_k = min(len(metadata), max(target_top_k * 6, target_top_k + 20))
    pairs = search_top_k(index=index, query_vector=query_vector, top_k=search_k)

    threshold = config.min_retrieval_score if min_score is None else min_score
    retrieved: list[RetrievedChunk] = []

    reranked = _rerank_candidates(
        question=normalized_question,
        pairs=pairs,
        metadata=metadata,
        threshold=threshold,
        target_top_k=target_top_k,
    )

    if len(reranked) < target_top_k:
        lexical_fallback = _lexical_search_over_metadata(
            question=normalized_question,
            metadata=metadata,
            top_n=max(target_top_k * 3, 12),
        )
        existing_positions = {int(item["chunk_pos"]) for item in reranked}
        for candidate in lexical_fallback:
            if int(candidate["chunk_pos"]) in existing_positions:
                continue
            reranked.append(candidate)
            existing_positions.add(int(candidate["chunk_pos"]))
            if len(reranked) >= target_top_k:
                break

    for candidate in reranked:
        item = candidate["item"]
        page = int(item.get("page", item.get("page_start", -1)))
        retrieved.append(
            RetrievedChunk(
                chunk_id=str(item.get("chunk_id", "")),
                text=str(item.get("text", "")),
                page_start=page,
                page_end=int(item.get("page_end", page)),
                score=float(candidate["combined_score"]),
                metadata={
                    "source": str(item.get("source", "")),
                    "vector_score": float(candidate["vector_score"]),
                    "lexical_score": float(candidate["lexical_score"]),
                },
            )
        )

    return retrieved


def retrieve(query: str, top_k: int = 5) -> dict[str, Any]:
    """檢索入口函式。

    Returns:
        dict: 至少包含 `insufficient_evidence` 與 `results`。
    """
    config = load_config()
    matched = retrieve_chunks(config=config, question=query, top_k=top_k)
    results = [
        {
            "chunk_id": item.chunk_id,
            "page": item.page_start,
            "text": item.text,
            "score": item.score,
            "source": str(item.metadata.get("source", "")),
        }
        for item in matched
    ]
    return {
        "insufficient_evidence": len(results) == 0,
        "results": results,
    }


def build_context_text(results: Sequence[RetrievedChunk]) -> str:
    """把檢索結果整理成給 LLM 的 context 字串。"""
    blocks: list[str] = []
    for item in results:
        blocks.append(
            (
                f"[chunk_id={item.chunk_id} | page={item.page_start} | score={item.score:.4f}]\n"
                f"{item.text}"
            )
        )
    return "\n\n".join(blocks)


def _build_arg_parser() -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    parser = argparse.ArgumentParser(description="本地索引檢索測試")
    parser.add_argument("--query", type=str, default="", help="查詢問題；留空會進入互動模式")
    parser.add_argument("--top-k", type=int, default=5, help="回傳前 K 筆")
    parser.add_argument("--min-score", type=float, default=None, help="最低檢索分數門檻（覆蓋 .env）")
    parser.add_argument("--index-dir", type=Path, default=None, help="索引資料夾（覆蓋預設）")
    parser.add_argument("--log-level", type=str, default="INFO", help="日誌層級")
    return parser


def _run_single_query(
    query: str,
    top_k: int,
    index_dir: Path | None,
    min_score: float | None,
) -> dict[str, Any]:
    """執行單次檢索並輸出 dict 結果。"""
    config = load_config()
    matched = retrieve_chunks(
        config=config,
        question=query,
        top_k=top_k,
        index_dir=index_dir,
        min_score=min_score,
    )
    results = [
        {
            "chunk_id": item.chunk_id,
            "page": item.page_start,
            "text": item.text,
            "score": item.score,
            "source": str(item.metadata.get("source", "")),
        }
        for item in matched
    ]
    return {
        "insufficient_evidence": len(results) == 0,
        "results": results,
    }


def main() -> int:
    """命令列測試入口。"""
    parser = _build_arg_parser()
    args = parser.parse_args()
    _setup_logging(args.log_level)

    try:
        if args.top_k <= 0:
            raise ValueError("--top-k 必須大於 0。")
        if args.min_score is not None and args.min_score < -1.0:
            raise ValueError("--min-score 不可小於 -1。")

        if args.query.strip():
            output = _run_single_query(
                query=args.query.strip(),
                top_k=args.top_k,
                index_dir=args.index_dir,
                min_score=args.min_score,
            )
            print(json.dumps(output, ensure_ascii=False, indent=2))
            return 0

        print("進入互動模式，直接按 Enter 可離開。")
        while True:
            query = input("請輸入 query：").strip()
            if not query:
                print("已離開。")
                break
            output = _run_single_query(
                query=query,
                top_k=args.top_k,
                index_dir=args.index_dir,
                min_score=args.min_score,
            )
            print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (FileNotFoundError, ValueError) as exc:
        LOGGER.error("%s", exc)
        return 1
    except KeyboardInterrupt:
        print("\n已中斷。")
        return 130
    except Exception as exc:  # pragma: no cover
        LOGGER.exception("retrieve 執行失敗：%s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
