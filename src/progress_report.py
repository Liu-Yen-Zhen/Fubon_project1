"""從 run_records.md 彙總每輪評估成效，輸出歷程報表。"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


@dataclass(slots=True)
class RunMetrics:
    """單次 run 的核心指標。"""

    run_time: str
    total: int | None = None
    correct: int | None = None
    accuracy: float | None = None
    error_rate: float | None = None
    refused: int | None = None
    hallucination: int | None = None
    retrieval_error: int | None = None
    synthesis_error: int | None = None
    numeric_error: int | None = None
    multi_question_error: int | None = None
    hallucination_error: int | None = None
    refusal_needed_but_not_triggered: int | None = None


def _safe_int(value: str | None) -> int | None:
    """安全轉整數。"""
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _safe_float(value: str | None) -> float | None:
    """安全轉浮點數。"""
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _extract_subsection(run_block: str, title: str) -> str:
    """取出 run_block 中指定章節內容。"""
    start_pattern = re.compile(rf"^###\s+{re.escape(title)}\s*$", flags=re.MULTILINE)
    match = start_pattern.search(run_block)
    if not match:
        return ""

    section_start = match.end()
    next_header = re.search(r"^###\s+", run_block[section_start:], flags=re.MULTILINE)
    if not next_header:
        return run_block[section_start:]
    return run_block[section_start : section_start + next_header.start()]


def _extract_metric(text: str, pattern: str) -> str | None:
    """抽取單一指標文字。"""
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1)


def _iter_runs(content: str) -> Iterable[tuple[str, str]]:
    """逐段走訪每個 Run Record。"""
    headers = list(re.finditer(r"^## Run Record - (.+)$", content, flags=re.MULTILINE))
    if not headers:
        return

    for idx, header in enumerate(headers):
        run_time = header.group(1).strip()
        start = header.end()
        end = headers[idx + 1].start() if idx + 1 < len(headers) else len(content)
        yield run_time, content[start:end]


def parse_run_records(run_records_path: Path) -> list[RunMetrics]:
    """解析 run_records.md，產生每輪指標。"""
    if not run_records_path.exists():
        raise FileNotFoundError(f"找不到 run records：{run_records_path}")

    content = run_records_path.read_text(encoding="utf-8")
    metrics_rows: list[RunMetrics] = []

    for run_time, block in _iter_runs(content):
        batch_text = _extract_subsection(block, "Batch Evaluate")
        error_text = _extract_subsection(block, "Error Analysis")

        total = _safe_int(_extract_metric(batch_text, r"題數:\s*(\d+)"))
        correct = _safe_int(_extract_metric(batch_text, r"correct 數:\s*(\d+)"))
        accuracy = _safe_float(_extract_metric(batch_text, r"accuracy:\s*([0-9.]+)"))
        refused = _safe_int(_extract_metric(batch_text, r"refused 數:\s*(\d+)"))
        hallucination = _safe_int(_extract_metric(batch_text, r"hallucination 數:\s*(\d+)"))

        retrieval_error = _safe_int(_extract_metric(error_text, r"retrieval_error:\s*(\d+)"))
        synthesis_error = _safe_int(_extract_metric(error_text, r"synthesis_error:\s*(\d+)"))
        numeric_error = _safe_int(_extract_metric(error_text, r"numeric_error:\s*(\d+)"))
        multi_question_error = _safe_int(_extract_metric(error_text, r"multi_question_error:\s*(\d+)"))
        hallucination_error = _safe_int(_extract_metric(error_text, r"hallucination:\s*(\d+)"))
        refusal_needed = _safe_int(_extract_metric(error_text, r"refusal_needed_but_not_triggered:\s*(\d+)"))

        error_rate = (1.0 - accuracy) if accuracy is not None else None
        metrics_rows.append(
            RunMetrics(
                run_time=run_time,
                total=total,
                correct=correct,
                accuracy=accuracy,
                error_rate=error_rate,
                refused=refused,
                hallucination=hallucination,
                retrieval_error=retrieval_error,
                synthesis_error=synthesis_error,
                numeric_error=numeric_error,
                multi_question_error=multi_question_error,
                hallucination_error=hallucination_error,
                refusal_needed_but_not_triggered=refusal_needed,
            )
        )

    return metrics_rows


def write_csv(rows: list[RunMetrics], output_csv: Path) -> Path:
    """輸出 CSV 報表。"""
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(asdict(RunMetrics(run_time="")).keys())
    with output_csv.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
    return output_csv


def write_markdown(rows: list[RunMetrics], output_md: Path) -> Path:
    """輸出 Markdown 報表。"""
    output_md.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# Optimization Progress Report")
    lines.append("")
    lines.append(f"- 總 run 次數：{len(rows)}")
    lines.append("")

    if rows:
        latest = rows[-1]
        lines.append("## 最新結果")
        lines.append("")
        lines.append(f"- run_time：{latest.run_time}")
        lines.append(f"- correct / total：{latest.correct} / {latest.total}")
        lines.append(f"- accuracy：{latest.accuracy:.4f}" if latest.accuracy is not None else "- accuracy：N/A")
        lines.append(f"- error_rate：{latest.error_rate:.4f}" if latest.error_rate is not None else "- error_rate：N/A")
        lines.append(f"- refused：{latest.refused}")
        lines.append(f"- hallucination：{latest.hallucination}")
        lines.append("")

    lines.append("## 歷程表")
    lines.append("")
    lines.append(
        "| run_time | correct | total | accuracy | error_rate | refused | hallucination | retrieval_error | synthesis_error | numeric_error | multi_question_error | hallucination_error | refusal_needed_but_not_triggered |"
    )
    lines.append(
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
    )
    for row in rows:
        lines.append(
            f"| {row.run_time} | {row.correct or 0} | {row.total or 0} | "
            f"{(f'{row.accuracy:.4f}' if row.accuracy is not None else 'N/A')} | "
            f"{(f'{row.error_rate:.4f}' if row.error_rate is not None else 'N/A')} | "
            f"{row.refused or 0} | {row.hallucination or 0} | "
            f"{row.retrieval_error or 0} | {row.synthesis_error or 0} | {row.numeric_error or 0} | "
            f"{row.multi_question_error or 0} | {row.hallucination_error or 0} | "
            f"{row.refusal_needed_but_not_triggered or 0} |"
        )

    output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_md


def _build_arg_parser() -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    parser = argparse.ArgumentParser(description="彙整 run_records.md 成效歷程報表")
    parser.add_argument(
        "--run-records-path",
        type=Path,
        default=Path("outputs/run_records.md"),
        help="run_records.md 路徑",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=Path("outputs/progress_history.csv"),
        help="CSV 輸出路徑",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=Path("outputs/progress_history.md"),
        help="Markdown 輸出路徑",
    )
    return parser


def main() -> int:
    """命令列入口。"""
    parser = _build_arg_parser()
    args = parser.parse_args()

    try:
        rows = parse_run_records(args.run_records_path)
        write_csv(rows, args.output_csv)
        write_markdown(rows, args.output_md)
        print(f"rows: {len(rows)}")
        print(f"csv: {args.output_csv}")
        print(f"md: {args.output_md}")
        return 0
    except Exception as exc:
        print(f"progress report 失敗：{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
