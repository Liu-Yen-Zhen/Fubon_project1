"""集中管理富邦金控年報 RAG 專案設定。"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(slots=True)
class AppConfig:
    """專案執行設定容器。"""

    project_name: str
    project_root: Path
    data_dir: Path
    index_dir: Path
    output_dir: Path
    pdf_path: Path
    qa_excel_path: Path
    supplement_pdf_path: Path
    chunk_size: int
    chunk_overlap: int
    top_k: int
    min_context_chunks: int
    min_retrieval_score: float
    answer_model: str
    embedding_model: str
    log_level: str


def _read_int(name: str, default: int, *, minimum: int | None = None) -> int:
    """讀取整數環境變數並做範圍驗證。"""
    raw = os.getenv(name, str(default)).strip()
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} 必須是整數，收到：{raw}") from exc
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} 必須 >= {minimum}，收到：{value}")
    return value


def _read_float(name: str, default: float, *, minimum: float | None = None) -> float:
    """讀取浮點數環境變數並做範圍驗證。"""
    raw = os.getenv(name, str(default)).strip()
    try:
        value = float(raw)
    except ValueError as exc:
        raise ValueError(f"{name} 必須是數字，收到：{raw}") from exc
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} 必須 >= {minimum}，收到：{value}")
    return value


def load_config(env_file: Path | None = None) -> AppConfig:
    """載入 `.env` 後產生 `AppConfig`。

    Args:
        env_file: 指定 `.env` 路徑；若為 `None` 則使用預設查找機制。

    Returns:
        AppConfig: 供各模組共用的設定物件。
    """
    project_root = Path(__file__).resolve().parents[1]
    if env_file is not None:
        env_path = env_file if env_file.is_absolute() else project_root / env_file
        load_dotenv(env_path, override=False)
    else:
        default_env_path = project_root / ".env"
        # 以專案根目錄的 .env 為主，避免從其他 cwd 執行時讀不到設定。
        if default_env_path.exists():
            load_dotenv(default_env_path, override=False)
        else:
            # fallback：保留 python-dotenv 預設查找行為。
            load_dotenv(override=False)

    data_dir = project_root / os.getenv("DATA_DIR", "data")
    # 預設索引路徑統一到 outputs，避免 build/retrieve 目錄不一致。
    index_dir = project_root / os.getenv("INDEX_DIR", "outputs")
    output_dir = project_root / os.getenv("OUTPUT_DIR", "outputs")

    chunk_size = _read_int("CHUNK_SIZE", 800, minimum=1)
    chunk_overlap = _read_int("CHUNK_OVERLAP", 120, minimum=0)
    if chunk_overlap >= chunk_size:
        raise ValueError(f"CHUNK_OVERLAP({chunk_overlap}) 不可大於或等於 CHUNK_SIZE({chunk_size})。")

    top_k = _read_int("TOP_K", 5, minimum=1)
    min_context_chunks = _read_int("MIN_CONTEXT_CHUNKS", 2, minimum=1)
    min_retrieval_score = _read_float("MIN_RETRIEVAL_SCORE", 0.20, minimum=-1.0)

    return AppConfig(
        project_name=os.getenv("PROJECT_NAME", "fubon-annual-report-rag"),
        project_root=project_root,
        data_dir=data_dir,
        index_dir=index_dir,
        output_dir=output_dir,
        pdf_path=project_root / os.getenv("PDF_PATH", "113年報.pdf"),
        qa_excel_path=project_root / os.getenv("QA_EXCEL_PATH", "題目一_附件_問答集.xlsx"),
        supplement_pdf_path=project_root / os.getenv("SUPPLEMENT_PDF_PATH", "題目一_補充說明.pdf"),
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        top_k=top_k,
        min_context_chunks=min_context_chunks,
        min_retrieval_score=min_retrieval_score,
        answer_model=os.getenv("ANSWER_MODEL", "gpt-4.1-mini"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-large"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
