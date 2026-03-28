"""共用型別與工具函式。"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class DocumentChunk:
    """PDF 切片資料結構。"""

    chunk_id: str
    text: str
    page_start: int
    page_end: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievedChunk:
    """檢索回傳資料結構。"""

    chunk_id: str
    text: str
    page_start: int
    page_end: int
    score: float
    metadata: dict[str, Any] = field(default_factory=dict)


def ensure_dir(path: Path) -> Path:
    """建立資料夾（若不存在）並回傳同一路徑。

    TODO:
        - 加入目錄權限與可寫入性檢查。
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def utc_now_iso() -> str:
    """回傳 UTC ISO-8601 時間字串。"""
    return datetime.now(timezone.utc).isoformat()


def write_chunks_jsonl(chunks: list[DocumentChunk], output_path: Path) -> Path:
    """將 `DocumentChunk` 清單寫入 JSONL。

    TODO:
        - 增加 schema 版本欄位，支援未來相容性。
        - 增加壓縮選項（例如 `.jsonl.gz`）。
    """
    with output_path.open("w", encoding="utf-8") as file:
        for chunk in chunks:
            file.write(json.dumps(asdict(chunk), ensure_ascii=False) + "\n")
    return output_path


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """讀取 JSONL 並回傳字典清單。

    TODO:
        - 對壞行進行錯誤回報與跳過策略。
    """
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            rows.append(json.loads(line))
    return rows

