"""錯誤分析：根據 predictions.csv 產生可信、可讀的錯誤分析報告。"""

from __future__ import annotations

import argparse
import logging
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


LOGGER = logging.getLogger(__name__)

ERROR_CATEGORIES = [
    "retrieval_error",
    "synthesis_error",
    "numeric_error",
    "multi_question_error",
    "hallucination",
    "formatting_difference",
    "refusal_needed_but_not_triggered",
]

_STRONG_HALLUCINATION_NOTE_KEYWORDS = (
    "應拒答卻硬答",
    "引用頁碼與檢索結果不符",
    "回答數字與引用頁碼內容不符",
)


def _setup_logging(level: str = "INFO") -> None:
    """初始化日誌。"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def _to_bool(value: Any) -> bool:
    """將各種格式轉為布林值。"""
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    return text in {"true", "1", "yes", "y", "t"}


def _safe_int(value: Any, default: int = 0) -> int:
    """安全轉整數。"""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _to_text(value: Any) -> str:
    """將欄位值安全轉字串，避免 NaN 顯示。"""
    if pd.isna(value):
        return ""
    return str(value).strip()


def _normalize_text(text: str) -> str:
    """基本文字正規化。"""
    return re.sub(r"\s+", "", str(text or "").strip().lower())


def _normalize_for_format_compare(text: str) -> str:
    """格式差異檢測用正規化：去空白、標點、全半形差異。"""
    normalized = unicodedata.normalize("NFKC", text or "").strip().lower()
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[，,。．.;；:：、!?！？\"'`“”‘’()\[\]{}（）【】《》<>]", "", normalized)
    return normalized


def _extract_numbers(text: str) -> list[str]:
    """抽取數字字串（保留小數）。"""
    numbers = re.findall(r"\d+(?:,\d{3})*(?:\.\d+)?", text or "")
    normalized = [num.replace(",", "") for num in numbers]
    deduped: list[str] = []
    seen: set[str] = set()
    for num in normalized:
        if num not in seen:
            seen.add(num)
            deduped.append(num)
    return deduped


def _needs_refusal(reference_answer: str) -> bool:
    """依標準答案判斷是否理應拒答。"""
    normalized = _normalize_text(reference_answer)
    if not normalized:
        return True

    keywords = [
        "無法回答",
        "無法判斷",
        "資料不足",
        "查無資料",
        "未提及",
        "未提供此資訊",
        "無法推論",
        "不適用",
        "n/a",
    ]
    return any(_normalize_text(keyword) in normalized for keyword in keywords)


def _is_multi_question(question: str) -> bool:
    """判斷題目是否為多子問題。"""
    q = str(question or "")
    marks = q.count("？") + q.count("?")
    if marks >= 2:
        return True

    multi_patterns = [
        r"分別",
        r"各是",
        r"比較",
        r"以及",
        r"與.+?各",
        r"同時",
        r"彙整",
        r"總結",
    ]
    return any(re.search(pattern, q) for pattern in multi_patterns)


def _is_numeric_error(reference_answer: str, predicted_answer: str) -> bool:
    """判斷是否為數值錯誤。"""
    ref_numbers = _extract_numbers(reference_answer)
    if not ref_numbers:
        return False

    pred_numbers = _extract_numbers(predicted_answer)
    if not pred_numbers:
        return True

    pred_set = set(pred_numbers)
    return not all(num in pred_set for num in ref_numbers)


def _infer_formatting_difference(reference_answer: str, predicted_answer: str) -> bool:
    """推斷是否僅為格式差異。"""
    ref_raw = _to_text(reference_answer)
    pred_raw = _to_text(predicted_answer)
    if not ref_raw or not pred_raw:
        return False
    if ref_raw == pred_raw:
        return False
    return _normalize_for_format_compare(ref_raw) == _normalize_for_format_compare(pred_raw)


def _effective_hallucination(row: pd.Series) -> bool:
    """判斷有效 hallucination（排除純格式差異誤報）。"""
    raw_hallucination = _to_bool(row.get("hallucination", False))
    if not raw_hallucination:
        return False

    formatting_difference = _to_bool(row.get("formatting_difference", False))
    note = _to_text(row.get("note", ""))
    if formatting_difference and not any(keyword in note for keyword in _STRONG_HALLUCINATION_NOTE_KEYWORDS):
        return False
    return True


def _classify_error(row: pd.Series) -> tuple[str, str]:
    """規則式錯誤分類（單一主分類）。"""
    question = _to_text(row.get("question", ""))
    reference_answer = _to_text(row.get("reference_answer", ""))
    predicted_answer = _to_text(row.get("predicted_answer", ""))
    note = _to_text(row.get("note", ""))
    refused = _to_bool(row.get("refused", False))
    hallucination_flag = _to_bool(row.get("hallucination_effective", False))
    retrieved_count = _safe_int(row.get("retrieved_chunks_count", 0), default=0)

    if _needs_refusal(reference_answer) and not refused:
        return "refusal_needed_but_not_triggered", "標準答案顯示應拒答，但模型未拒答。"

    if hallucination_flag:
        return "hallucination", "回答含證據不支持資訊。"

    if retrieved_count <= 0 or "檢索流程失敗" in note or "找不到索引檔" in note:
        return "retrieval_error", "檢索結果不足或檢索流程失敗。"

    if _is_multi_question(question):
        return "multi_question_error", "多子問題覆蓋不完整或子題對應不穩定。"

    if _is_numeric_error(reference_answer, predicted_answer):
        return "numeric_error", "數值資訊與標準答案不一致。"

    return "synthesis_error", "檢索有內容但最終整合答案與標準答案不一致。"


def load_predictions(predictions_path: Path) -> pd.DataFrame:
    """讀取 predictions.csv。"""
    if not predictions_path.exists():
        raise FileNotFoundError(f"找不到 predictions.csv：{predictions_path}")

    df = pd.read_csv(predictions_path)
    required_cols = [
        "question",
        "reference_answer",
        "predicted_answer",
        "refused",
        "hallucination",
        "note",
        "is_correct",
    ]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"predictions.csv 缺少必要欄位：{missing}")
    return df


def analyze_errors(
    predictions_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int], dict[str, Any]]:
    """分析錯誤並回傳錯誤資料、格式差異資料、分類計數與摘要。"""
    df = predictions_df.copy()
    total_count = len(df)

    raw_correct_mask = df["is_correct"].apply(_to_bool)
    inferred_format_mask = df.apply(
        lambda row: _infer_formatting_difference(row.get("reference_answer", ""), row.get("predicted_answer", "")),
        axis=1,
    )
    provided_format_mask = (
        df["formatting_difference"].apply(_to_bool)
        if "formatting_difference" in df.columns
        else pd.Series([False] * total_count, index=df.index)
    )
    format_mask = provided_format_mask | inferred_format_mask
    df["formatting_difference"] = format_mask

    df["hallucination_effective"] = df.apply(_effective_hallucination, axis=1)

    # 定義一致性：
    # 1) formatting_difference 視為內容等價（可算 correct）
    # 2) true hallucination 不可視為 correct
    effective_correct_mask = (raw_correct_mask | df["formatting_difference"]) & (~df["hallucination_effective"])
    df["is_correct_effective"] = effective_correct_mask
    df["is_error_effective"] = ~effective_correct_mask

    error_df = df.loc[df["is_error_effective"]].copy()
    categories: list[str] = []
    reasons: list[str] = []
    for _, row in error_df.iterrows():
        category, reason = _classify_error(row)
        categories.append(category)
        reasons.append(reason)
    error_df["error_category"] = categories
    error_df["error_reason"] = reasons

    formatting_df = df.loc[df["formatting_difference"] & (~df["hallucination_effective"])].copy()
    formatting_df["error_category"] = "formatting_difference"
    formatting_df["error_reason"] = "僅格式差異（空白/標點/全半形/括號），內容等價。"

    counts = {category: 0 for category in ERROR_CATEGORIES}
    for category, count in error_df["error_category"].value_counts().to_dict().items():
        counts[category] = int(count)
    # formatting_difference 為獨立品質指標，不直接併入 true hallucination。
    counts["formatting_difference"] = int(len(formatting_df))

    corrected_by_format_count = int((~raw_correct_mask & df["formatting_difference"] & (~df["hallucination_effective"])).sum())
    hallucination_downgraded_count = int(
        (df["hallucination"].apply(_to_bool) & (~df["hallucination_effective"]) & df["formatting_difference"]).sum()
    )

    summary = {
        "total_count": total_count,
        "correct_count": int(df["is_correct_effective"].sum()),
        "error_count": int(df["is_error_effective"].sum()),
        "accuracy": float(df["is_correct_effective"].mean()) if total_count else 0.0,
        "hallucination_count": int(df["hallucination_effective"].sum()),
        "formatting_difference_count": int(len(formatting_df)),
        "corrected_by_format_count": corrected_by_format_count,
        "hallucination_downgraded_count": hallucination_downgraded_count,
    }
    return error_df, formatting_df, counts, summary


def _render_cases_md(df: pd.DataFrame, max_cases: int) -> list[str]:
    """輸出案例 Markdown 列表。"""
    lines: list[str] = []
    if df.empty:
        lines.append("無。")
        lines.append("")
        return lines

    for idx, (_, row) in enumerate(df.head(max_cases).iterrows(), start=1):
        sample_id = _to_text(row.get("sample_id", "N/A")) or "N/A"
        lines.append(f"{idx}. 題號：{sample_id}")
        lines.append(f"   - 問題：{_to_text(row.get('question', ''))}")
        lines.append(f"   - 標準答案：{_to_text(row.get('reference_answer', ''))}")
        lines.append(f"   - 預測答案：{_to_text(row.get('predicted_answer', ''))}")
        lines.append(f"   - note：{_to_text(row.get('note', ''))}")
        lines.append(f"   - 分類理由：{_to_text(row.get('error_reason', ''))}")
    lines.append("")
    return lines


def _build_recommendations(summary: dict[str, Any], counts: dict[str, int]) -> list[str]:
    """依錯誤分布產生下一步建議。"""
    recs: list[str] = []
    if counts.get("retrieval_error", 0) > 0:
        recs.append("提高召回：擴充 query 改寫、調整 chunk 參數、加入 hybrid retrieval（BM25 + 向量）。")
    if counts.get("multi_question_error", 0) > 0:
        recs.append("強化多子題覆蓋：提示詞要求逐點映射子題，並加入子題完整性檢核。")
    if counts.get("numeric_error", 0) > 0:
        recs.append("強化數值穩定：增加數值抽取與單位換算檢核，避免 % 與小數換算錯誤。")
    if counts.get("hallucination", 0) > 0:
        recs.append("降低幻覺：在回答後做證據對齊檢查，證據不足時改為拒答。")
    if counts.get("synthesis_error", 0) > 0:
        recs.append("改善整合品質：增加輸出長度控制與範圍收斂，避免答非所問。")
    if summary.get("formatting_difference_count", 0) > 0:
        recs.append("優化評估可讀性：持續維護格式正規化規則，避免格式差異影響指標解讀。")
    if not recs:
        recs.append("目前未觀察到顯著錯誤；建議擴充未見題型測試集以驗證泛化能力。")
    return recs


def build_error_analysis_md(
    *,
    summary: dict[str, Any],
    counts: dict[str, int],
    error_df: pd.DataFrame,
    formatting_df: pd.DataFrame,
    max_cases_per_category: int,
) -> str:
    """組出 error_analysis.md 內容。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_count = int(summary["total_count"])
    correct_count = int(summary["correct_count"])
    error_count = int(summary["error_count"])
    accuracy = float(summary["accuracy"])

    lines: list[str] = []
    lines.append("# Error Analysis")
    lines.append("")
    lines.append(f"- generated_at: {now}")
    lines.append("")

    lines.append("## evaluation definitions")
    lines.append("")
    lines.append("- `is_correct`: 與標準答案內容一致（含等價表示）且非 true hallucination。")
    lines.append("- `hallucination`: 回答包含證據不支持資訊（不存在/錯誤數字，或頁碼證據無法支持）。")
    lines.append("- `formatting_difference`: 僅格式差異（空白、標點、全半形、括號），不算 hallucination。")
    lines.append("- `error`: `not is_correct`；因此 true hallucination 一定列入 error。")
    lines.append("")

    lines.append("## overall summary")
    lines.append("")
    lines.append(f"- total_questions: {total_count}")
    lines.append(f"- correct: {correct_count}")
    lines.append(f"- errors: {error_count}")
    lines.append(f"- accuracy: {accuracy:.4f}")
    lines.append(f"- hallucination_count: {int(summary.get('hallucination_count', 0))}")
    lines.append(f"- formatting_difference_count: {int(summary.get('formatting_difference_count', 0))}")
    lines.append(f"- corrected_by_format_count: {int(summary.get('corrected_by_format_count', 0))}")
    lines.append(f"- hallucination_downgraded_to_format_count: {int(summary.get('hallucination_downgraded_count', 0))}")
    lines.append("")

    lines.append("## error counts by type")
    lines.append("")
    lines.append("| type | count | ratio_in_errors | ratio_in_total |")
    lines.append("|---|---:|---:|---:|")
    for category in ERROR_CATEGORIES:
        count = int(counts.get(category, 0))
        ratio_errors = (count / error_count) if error_count else 0.0
        ratio_total = (count / total_count) if total_count else 0.0
        lines.append(f"| {category} | {count} | {ratio_errors:.2%} | {ratio_total:.2%} |")
    lines.append("")

    lines.append("## representative examples")
    lines.append("")
    for category in ERROR_CATEGORIES:
        lines.append(f"### {category}")
        if category == "formatting_difference":
            lines.extend(_render_cases_md(formatting_df, max_cases_per_category))
        else:
            category_df = error_df[error_df["error_category"] == category]
            lines.extend(_render_cases_md(category_df, max_cases_per_category))

    lines.append("## recommended next-step improvements")
    lines.append("")
    for idx, recommendation in enumerate(_build_recommendations(summary, counts), start=1):
        lines.append(f"{idx}. {recommendation}")
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def generate_error_analysis(
    predictions_path: Path,
    output_path: Path,
    max_cases_per_category: int = 3,
) -> dict[str, Any]:
    """從 predictions.csv 產生 error_analysis.md。"""
    predictions_df = load_predictions(predictions_path=predictions_path)
    error_df, formatting_df, counts, summary = analyze_errors(predictions_df=predictions_df)
    report_text = build_error_analysis_md(
        summary=summary,
        counts=counts,
        error_df=error_df,
        formatting_df=formatting_df,
        max_cases_per_category=max_cases_per_category,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_text, encoding="utf-8")

    print(f"題數: {summary['total_count']}")
    print(f"correct 數: {summary['correct_count']}")
    print(f"accuracy: {summary['accuracy']:.4f}")
    print(f"error 數: {summary['error_count']}")
    print(f"hallucination 數: {summary.get('hallucination_count', 0)}")
    print(f"formatting_difference 數: {summary.get('formatting_difference_count', 0)}")
    for category in ERROR_CATEGORIES:
        print(f"{category}: {counts.get(category, 0)}")
    print(f"error_analysis.md: {output_path}")

    return {
        "summary": summary,
        "counts": counts,
        "output_path": str(output_path),
    }


def _build_arg_parser() -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    parser = argparse.ArgumentParser(description="根據 predictions.csv 產生錯誤分析報告")
    parser.add_argument(
        "--predictions-path",
        type=Path,
        default=Path("outputs/predictions.csv"),
        help="predictions.csv 路徑",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("outputs/error_analysis.md"),
        help="error_analysis.md 輸出路徑",
    )
    parser.add_argument(
        "--max-cases-per-category",
        type=int,
        default=3,
        help="每個錯誤類別展示案例數",
    )
    parser.add_argument("--log-level", type=str, default="INFO", help="日誌層級")
    return parser


def main() -> int:
    """命令列入口。"""
    parser = _build_arg_parser()
    args = parser.parse_args()
    _setup_logging(args.log_level)

    try:
        if args.max_cases_per_category <= 0:
            raise ValueError("--max-cases-per-category 必須大於 0。")

        generate_error_analysis(
            predictions_path=args.predictions_path,
            output_path=args.output_path,
            max_cases_per_category=args.max_cases_per_category,
        )
        return 0
    except (FileNotFoundError, ValueError) as exc:
        LOGGER.error("%s", exc)
        return 1
    except Exception as exc:  # pragma: no cover
        LOGGER.exception("產生錯誤分析失敗：%s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
