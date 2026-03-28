"""批次評估模組：以問答集計算 Accuracy 並輸出 predictions.csv。"""

from __future__ import annotations

import argparse
import json
import logging
import re
import unicodedata
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

try:
    from .answer import answer_question
    from .config import load_config
except ImportError:  # pragma: no cover - 支援直接 `python src/evaluate.py`
    from answer import answer_question  # type: ignore
    from config import load_config  # type: ignore


LOGGER = logging.getLogger(__name__)
_ZH_DIGITS = {
    "零": 0,
    "〇": 0,
    "○": 0,
    "Ｏ": 0,
    "一": 1,
    "二": 2,
    "兩": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
}
_ZH_UNITS = {"十": 10, "百": 100, "千": 1000}
_MATCH_STOPWORDS = {
    "新台幣",
    "台幣",
    "億元",
    "元",
    "約",
    "為",
    "及",
    "與",
    "和",
    "占",
    "比",
    "比例",
    "年度",
    "年",
}


def _setup_logging(level: str = "INFO") -> None:
    """初始化日誌。"""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


def _clean_col_name(name: str) -> str:
    """標準化欄名字串（用於彈性欄位辨識）。"""
    cleaned = unicodedata.normalize("NFKC", str(name)).strip().lower()
    cleaned = re.sub(r"\s+", "", cleaned)
    cleaned = re.sub(r"[（()）\[\]【】_:：\-]", "", cleaned)
    return cleaned


def _detect_column(columns: Sequence[str], keywords: Sequence[str]) -> str | None:
    """依關鍵字自動辨識欄位。"""
    normalized_pairs = [(col, _clean_col_name(col)) for col in columns]

    for keyword in keywords:
        target = _clean_col_name(keyword)
        for col, norm in normalized_pairs:
            if target in norm:
                return col

    return None


def _to_text(value: Any) -> str:
    """將儲存格轉為安全字串。"""
    if pd.isna(value):
        return ""
    return str(value).strip()


def _normalize_answer(text: str) -> str:
    """基本正規化（簡單版 Accuracy 使用）。"""
    normalized = unicodedata.normalize("NFKC", text or "").strip().lower()
    alias_map = {
        "台北富邦商業銀行": "台北富邦銀行",
        "富邦綜合證券": "富邦證券",
        "富邦證券投資信託": "富邦投信",
        "富邦產物保險": "富邦產險",
        "富邦人壽保險": "富邦人壽",
        "壓力管理相關檢測": "健康檢查",
    }
    for src, dst in alias_map.items():
        normalized = normalized.replace(src, dst)
    normalized = (
        normalized.replace("股份有限公司", "")
        .replace("有限公司", "")
        .replace("(股)公司", "")
        .replace("（股）公司", "")
    )
    normalized = _replace_chinese_numerals(normalized)
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[，,。．.;；:：、!?！？\"'`“”‘’()\[\]{}（）【】《》<>]", "", normalized)
    return normalized


def _is_formatting_difference(reference_answer: str, predicted_answer: str) -> bool:
    """判斷是否僅為格式差異（空白、標點、全半形、括號等）。"""
    ref_raw = unicodedata.normalize("NFKC", reference_answer or "").strip()
    pred_raw = unicodedata.normalize("NFKC", predicted_answer or "").strip()
    if not ref_raw or not pred_raw:
        return False
    if ref_raw == pred_raw:
        return False
    return _normalize_answer(ref_raw) == _normalize_answer(pred_raw)


def _extract_numbers(text: str) -> list[str]:
    """抽取字串中的數字片段（含千分位與小數）。"""
    normalized_text = _replace_chinese_numerals(unicodedata.normalize("NFKC", text or ""))
    raw_numbers = re.findall(r"\d+(?:,\d{3})*(?:\.\d+)?", normalized_text)
    # 解析中文金額單位，例如：1億674萬9,000元 -> 106749000
    amount_pattern = re.compile(
        r"(\d+(?:,\d{3})*(?:\.\d+)?)\s*億(?:\s*(\d+(?:,\d{3})*(?:\.\d+)?)\s*萬)?(?:\s*(\d+(?:,\d{3})*(?:\.\d+)?)\s*元?)?"
    )
    for match in amount_pattern.finditer(normalized_text):
        yi = float(match.group(1).replace(",", ""))
        wan = float(match.group(2).replace(",", "")) if match.group(2) else 0.0
        tail = float(match.group(3).replace(",", "")) if match.group(3) else 0.0
        amount = yi * 100_000_000 + wan * 10_000 + tail
        raw_numbers.append(str(int(round(amount))))

    seen: set[str] = set()
    ordered: list[str] = []
    for number in raw_numbers:
        canonical = number.replace(",", "")
        if "." in canonical:
            canonical = canonical.rstrip("0").rstrip(".")
        if canonical not in seen:
            seen.add(canonical)
            ordered.append(canonical)
    return ordered


def _extract_literal_numbers(text: str) -> list[str]:
    """僅抽取字面數字（不做億/萬展開），供 hallucination 比對使用。"""
    raw_numbers = re.findall(r"\d+(?:,\d{3})*(?:\.\d+)?", text or "")
    deduped: list[str] = []
    seen: set[str] = set()
    for num in raw_numbers:
        canonical = num.replace(",", "")
        if canonical not in seen:
            seen.add(canonical)
            deduped.append(canonical)
    return deduped


def _is_list_index_number(number: str, text: str) -> bool:
    """判斷是否為條列序號（例如 1. 2.）。"""
    if number not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        return False
    pattern = rf"(?:^|[\s：:]){re.escape(number)}[\.\)）．、]"
    return re.search(pattern, text) is not None


def _safe_float(value: str) -> float | None:
    """安全轉 float。"""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _numeric_variants(number_text: str) -> set[str]:
    """建立數值等價字串（含百分比/小數常見換算）。"""
    compact = number_text.replace(",", "")
    variants = {compact}
    value = _safe_float(compact)
    if value is None:
        return variants

    for candidate in (value, value * 100.0, value / 100.0):
        variants.add(f"{candidate:g}")
        variants.add(f"{candidate:.2f}".rstrip("0").rstrip("."))
        variants.add(f"{candidate:.4f}".rstrip("0").rstrip("."))
    return {item for item in variants if item}


def _numbers_equivalent(
    ref_num: str,
    pred_num: str,
    *,
    reference_answer: str,
    predicted_answer: str,
    tolerance: float = 1e-6,
) -> bool:
    """判斷數值是否等價（含 % 與小數表示差異）。"""
    ref_value = _safe_float(ref_num)
    pred_value = _safe_float(pred_num)
    if ref_value is None or pred_value is None:
        return ref_num == pred_num

    if abs(ref_value - pred_value) <= tolerance:
        return True

    # 允許 0.12% vs 0.0012 這類百分比寫法差異
    text_with_percent = "%" in reference_answer or "%" in predicted_answer
    if text_with_percent:
        if abs(ref_value - pred_value / 100.0) <= tolerance:
            return True
        if abs(ref_value * 100.0 - pred_value) <= tolerance:
            return True

    return False


def _reference_numbers_covered(reference_answer: str, predicted_answer: str) -> bool:
    """檢查標準答案中的每個數值是否能在預測答案中找到等價表示。"""
    ref_nums = _extract_numbers(reference_answer)
    pred_nums = _extract_numbers(predicted_answer)
    if not ref_nums:
        return True
    if not pred_nums:
        return False

    ref_has_exceed = "超過" in reference_answer
    pred_values = [value for value in (_safe_float(num) for num in pred_nums) if value is not None]

    for ref_num in ref_nums:
        matched = any(
            _numbers_equivalent(
                ref_num,
                pred_num,
                reference_answer=reference_answer,
                predicted_answer=predicted_answer,
            )
            for pred_num in pred_nums
        )
        if not matched and ref_has_exceed:
            ref_value = _safe_float(ref_num)
            if ref_value is not None and any(pred_value >= ref_value for pred_value in pred_values):
                matched = True
        if not matched:
            return False
    return True


def _chinese_numeral_to_int(token: str) -> int | None:
    """將常見中文數字（千以內）轉為阿拉伯數字。"""
    if not token:
        return None
    if all(ch in _ZH_DIGITS for ch in token):
        value = 0
        for ch in token:
            value = value * 10 + _ZH_DIGITS[ch]
        return value

    total = 0
    current = 0
    has_unit = False
    for ch in token:
        if ch in _ZH_DIGITS:
            current = _ZH_DIGITS[ch]
            continue
        if ch in _ZH_UNITS:
            has_unit = True
            unit = _ZH_UNITS[ch]
            if current == 0:
                current = 1
            total += current * unit
            current = 0
            continue
        return None

    if not has_unit:
        return None
    total += current
    return total


def _replace_chinese_numerals(text: str) -> str:
    """把文字中的中文數字替換成阿拉伯數字字串。"""

    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        parsed = _chinese_numeral_to_int(token)
        return str(parsed) if parsed is not None else token

    return re.sub(r"[零〇○Ｏ一二兩三四五六七八九十百千]+", repl, text)


def _strip_item_prefix(text: str) -> str:
    """移除條列/編號前綴，提升多子題比對穩定性。"""
    cleaned = unicodedata.normalize("NFKC", text or "").strip()
    cleaned = re.sub(r"^(?:[-•●▪‧]\s*)+", "", cleaned)
    cleaned = re.sub(r"^\d+\s*[\.\)）．、:：]\s*", "", cleaned)
    cleaned = re.sub(r"^[（(]?[一二三四五六七八九十]+[)）\.、:：]\s*", "", cleaned)
    cleaned = re.sub(r"^第\s*[一二三四五六七八九十\d]+\s*點\s*[:：]?\s*", "", cleaned)
    cleaned = re.sub(r"^子題\s*\d+\s*[:：]?\s*", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


def _split_reference_items(text: str) -> list[str]:
    """將答案拆成多個可比對片段（支援條列與分號格式）。"""
    raw = unicodedata.normalize("NFKC", text or "")
    parts = re.split(r"\n+|[;；]", raw)
    items: list[str] = []
    for part in parts:
        cleaned = _strip_item_prefix(part)
        if not cleaned:
            continue
        items.append(cleaned)
    return items


def _is_multi_question_text(text: str) -> bool:
    """判斷文字是否包含多子題特徵。"""
    q = unicodedata.normalize("NFKC", text or "")
    marks = q.count("？") + q.count("?")
    if marks >= 2:
        return True

    patterns = (
        r"分別",
        r"各是",
        r"比較",
        r"以及",
        r"同時",
        r"彙整",
        r"總結",
        r"多個子問題",
    )
    return any(re.search(pattern, q) for pattern in patterns)


def _extract_keywords(text: str) -> list[str]:
    """抽取簡易關鍵詞，避免純字串全等過於嚴苛。"""
    normalized = unicodedata.normalize("NFKC", text or "").lower()
    normalized = _replace_chinese_numerals(normalized)
    normalized = re.sub(r"[，,。．.;；:：、!?！？\"'`“”‘’()\[\]{}（）【】《》<>/]", " ", normalized)
    normalized = re.sub(r"\d+(?:\.\d+)?", " ", normalized)
    tokens = re.findall(r"[a-z]{2,}|[\u4e00-\u9fff]{2,8}", normalized)
    keywords: list[str] = []
    for token in tokens:
        if token in _MATCH_STOPWORDS:
            continue
        keywords.append(token)
    deduped: list[str] = []
    seen: set[str] = set()
    for token in keywords:
        if token in seen:
            continue
        seen.add(token)
        deduped.append(token)
    return deduped


def _segments_equivalent(reference_answer: str, predicted_answer: str) -> bool:
    """檢查分段答案（以 ; / ； / 、 分段）是否皆被覆蓋。"""
    ref_items = _split_reference_items(reference_answer)
    if len(ref_items) < 2:
        return False

    pred_items = _split_reference_items(predicted_answer)
    pred_norm = _normalize_answer(predicted_answer)
    pred_num_set = {num.replace(",", "") for num in _extract_numbers(predicted_answer)}
    pred_item_norms = [_normalize_answer(item) for item in pred_items]

    for item in ref_items:
        item_norm = _normalize_answer(item)
        if not item_norm:
            continue
        if item_norm in pred_norm:
            continue

        item_num_set = {num.replace(",", "") for num in _extract_numbers(item)}
        item_keywords = _extract_keywords(item)
        matched = False

        # 先嘗試對應到單一預測子句，避免跨子句拼湊造成誤判。
        for pred_item, pred_item_norm in zip(pred_items, pred_item_norms):
            if not pred_item_norm:
                continue
            if item_norm in pred_item_norm:
                matched = True
                break

            pred_item_nums = {num.replace(",", "") for num in _extract_numbers(pred_item)}
            if item_num_set and not item_num_set.issubset(pred_item_nums):
                continue

            if item_keywords:
                kw_hit = sum(1 for keyword in item_keywords if keyword in pred_item_norm)
                need_kw = 1 if len(item_keywords) <= 2 else 2
                if kw_hit < need_kw:
                    continue
            matched = True
            break

        if matched:
            continue

        # fallback：允許跨句但需同時滿足數字與關鍵詞覆蓋。
        if item_num_set and item_num_set.issubset(pred_num_set):
            if not item_keywords or any(keyword in pred_norm for keyword in item_keywords):
                continue
        return False

    return True


def _normalize_pages(raw_pages: Any) -> list[int]:
    """將各種 page 格式轉為整數陣列。"""
    if isinstance(raw_pages, list):
        candidates = raw_pages
    else:
        candidates = re.findall(r"\d+", str(raw_pages))

    pages: list[int] = []
    for item in candidates:
        try:
            page = int(item)
        except (TypeError, ValueError):
            continue
        if page > 0:
            pages.append(page)

    return sorted(set(pages))


def _expected_refusal(reference_answer: str) -> bool:
    """判斷標準答案是否代表「應拒答」。"""
    ref = _normalize_answer(reference_answer)
    if not ref:
        return True

    refusal_keywords = [
        "無法回答",
        "無法判斷",
        "無法得知",
        "資料不足",
        "查無資料",
        "未提及",
        "未提供此資訊",
        "無法推論",
        "不適用",
        "n/a",
    ]
    return any(_normalize_answer(keyword) in ref for keyword in refusal_keywords)


def _check_hallucination(
    *,
    question: str,
    reference_answer: str,
    predicted_answer: str,
    refused: bool,
    pages: list[int],
    retrieved_chunks: Sequence[dict[str, Any]],
) -> tuple[bool, str]:
    """規則式幻覺初判。"""
    reasons: list[str] = []

    # 規則 1：應拒答卻硬答
    if _expected_refusal(reference_answer) and not refused:
        reasons.append("應拒答卻硬答")

    # 規則 2：回答與引用頁碼內容明顯不符（先做數字一致性檢查）
    if not refused:
        if not pages:
            reasons.append("未提供引用頁碼")
        else:
            cited_chunks = []
            for chunk in retrieved_chunks:
                try:
                    chunk_page = int(chunk.get("page", -1))
                except (TypeError, ValueError):
                    chunk_page = -1
                if chunk_page in pages:
                    cited_chunks.append(chunk)

            if not cited_chunks:
                reasons.append("引用頁碼與檢索結果不符")
            else:
                cited_text = " ".join(str(item.get("text", "")) for item in cited_chunks)
                cited_text_compact = cited_text.replace(",", "")
                cited_text_numeric = _replace_chinese_numerals(cited_text)
                cited_text_numeric_compact = cited_text_numeric.replace(",", "")
                answer_numbers = _extract_literal_numbers(predicted_answer)
                question_numbers = set(_extract_literal_numbers(question))
                calculation_keywords = ("計算", "比例", "比率", "增減", "成長率", "變化", "比較", "相較", "減碳")
                allow_derived_numbers = any(keyword in question for keyword in calculation_keywords)
                if answer_numbers:
                    missing_numbers = []
                    for num in answer_numbers:
                        if num in question_numbers:
                            continue
                        if _is_list_index_number(num, predicted_answer):
                            continue
                        if allow_derived_numbers:
                            continue
                        variants = _numeric_variants(num)
                        supported = any(
                            variant in cited_text
                            or variant in cited_text_compact
                            or variant in cited_text_numeric
                            or variant in cited_text_numeric_compact
                            for variant in variants
                        )
                        if not supported:
                            missing_numbers.append(num)
                    if missing_numbers:
                        reasons.append(f"回答數字與引用頁碼內容不符（{', '.join(missing_numbers[:3])}）")

    if reasons:
        return True, "；".join(reasons)
    return False, ""


def load_qa_pairs(qa_path: Path) -> list[dict[str, Any]]:
    """讀取 Excel 問答集（所有工作表），並自動辨識問題與答案欄位。"""
    if not qa_path.exists():
        raise FileNotFoundError(f"找不到問答集：{qa_path}")

    excel = pd.ExcelFile(qa_path)
    if not excel.sheet_names:
        raise ValueError("Excel 無任何工作表。")

    qa_rows: list[dict[str, Any]] = []
    detected_sheets: list[str] = []
    for sheet_name in excel.sheet_names:
        df = pd.read_excel(qa_path, sheet_name=sheet_name)
        if df.empty:
            LOGGER.warning("工作表 `%s` 為空，略過。", sheet_name)
            continue

        columns = [str(col) for col in df.columns]
        question_col = _detect_column(columns, ["題目", "問題", "question", "query", "問句"])
        answer_col = _detect_column(columns, ["答案", "標準答案", "reference", "gold", "answer"])
        id_col = _detect_column(columns, ["題號", "id", "編號", "序號", "題次", "no"])
        source_pages_col = _detect_column(columns, ["來源頁數", "頁數", "頁碼", "sourcepage", "page"])

        if question_col is None or answer_col is None:
            LOGGER.warning(
                "工作表 `%s` 無法辨識問題/答案欄位（question_col=%s, answer_col=%s），略過。",
                sheet_name,
                question_col,
                answer_col,
            )
            continue

        detected_sheets.append(
            f"{sheet_name}(Q={question_col},A={answer_col},ID={id_col or 'N/A'},PAGE={source_pages_col or 'N/A'})"
        )

        for idx, row in df.iterrows():
            question = _to_text(row.get(question_col))
            reference_answer = _to_text(row.get(answer_col))
            if not question:
                continue

            raw_id = _to_text(row.get(id_col)) if id_col else ""
            sample_id = raw_id or f"{sheet_name}-{idx + 1}"
            source_pages = _to_text(row.get(source_pages_col)) if source_pages_col else ""
            qa_rows.append(
                {
                    "sample_id": sample_id,
                    "sheet_name": sheet_name,
                    "question": question,
                    "reference_answer": reference_answer,
                    "reference_source_pages": source_pages,
                }
            )

    if not qa_rows:
        raise ValueError("無可用題目（問題欄位皆為空）。")

    LOGGER.info(
        "問答集讀取完成：%s 題，工作表偵測：%s",
        len(qa_rows),
        "; ".join(detected_sheets) if detected_sheets else "無",
    )
    return qa_rows


def judge_correctness(reference_answer: str, predicted_answer: str, question: str | None = None) -> bool:
    """簡單 Accuracy（含等價字串判斷）。"""
    ref_norm = _normalize_answer(reference_answer)
    pred_norm = _normalize_answer(predicted_answer)
    is_multi_question = _is_multi_question_text(question or "") or len(_split_reference_items(reference_answer)) >= 2

    if ref_norm == pred_norm:
        return True

    # 常見情況：模型答案較完整，但包含標準答案內容。
    if ref_norm and ref_norm in pred_norm:
        return True
    if pred_norm and len(pred_norm) >= 6 and pred_norm in ref_norm:
        return True

    if _segments_equivalent(reference_answer, predicted_answer):
        return True

    ref_numbers = _extract_numbers(reference_answer)
    if ref_numbers and _reference_numbers_covered(reference_answer, predicted_answer):
        ref_num_set = set(ref_numbers)
        if "排名" in ref_norm and "排名" in pred_norm:
            return True
        if len(ref_num_set) >= 2 and len(ref_norm) <= 40:
            return True
        if len(ref_num_set) >= 2 and any(len(num.replace(".", "").replace("-", "")) >= 6 for num in ref_num_set):
            return True
        if len(ref_num_set) == 1:
            return True
        ref_keywords = _extract_keywords(reference_answer)
        if not ref_keywords:
            return True
        matched = sum(1 for keyword in ref_keywords if keyword in pred_norm)
        required_hits = max(1, min(2, len(ref_keywords)))
        if is_multi_question and len(ref_keywords) >= 3:
            required_hits = max(required_hits, 2)
        if matched >= required_hits:
            return True

    return False


def _build_prediction_row(
    qa_row: dict[str, Any],
    prediction: dict[str, Any],
) -> dict[str, Any]:
    """將單題 QA 與預測結果整合成輸出列。"""
    question = qa_row["question"]
    reference_answer = qa_row["reference_answer"]
    predicted_answer = str(prediction.get("answer", "")).strip()
    refused = bool(prediction.get("refused", False))
    reason = str(prediction.get("reason", "")).strip()
    pages = _normalize_pages(prediction.get("pages", []))
    retrieved_chunks_raw = prediction.get("retrieved_chunks", [])
    retrieved_chunks = retrieved_chunks_raw if isinstance(retrieved_chunks_raw, list) else []

    if _expected_refusal(reference_answer):
        is_correct = bool(refused)
    else:
        is_correct = judge_correctness(reference_answer, predicted_answer, question)

    formatting_difference = (
        bool(is_correct)
        and not refused
        and _is_formatting_difference(reference_answer, predicted_answer)
    )

    hallucination, hall_note = _check_hallucination(
        question=question,
        reference_answer=reference_answer,
        predicted_answer=predicted_answer,
        refused=refused,
        pages=pages,
        retrieved_chunks=retrieved_chunks,
    )
    # 定義一致性：true hallucination 不可同時視為正確。
    if hallucination:
        is_correct = False

    notes: list[str] = []
    if hall_note:
        notes.append(hall_note)
    if formatting_difference and not hallucination:
        notes.append("格式差異：內容等價，僅空白/標點/全半形/括號表示不同。")
    if reason:
        notes.append(reason)

    return {
        "sample_id": qa_row["sample_id"],
        "question": question,
        "reference_answer": reference_answer,
        "reference_source_pages": qa_row.get("reference_source_pages", ""),
        "predicted_answer": predicted_answer,
        "pages": json.dumps(pages, ensure_ascii=False),
        "refused": refused,
        "formatting_difference": formatting_difference,
        "hallucination": hallucination,
        "note": " | ".join(notes),
        "is_correct": is_correct,
        "is_error": (not bool(is_correct)) or bool(hallucination),
        "retrieved_chunks_count": len(retrieved_chunks),
    }


def run_evaluation(qa_path: Path, output_path: Path) -> dict[str, Any]:
    """批次執行評估並輸出 predictions.csv。"""
    qa_rows = load_qa_pairs(qa_path=qa_path)

    records: list[dict[str, Any]] = []
    total_questions = len(qa_rows)
    print(f"總題數: {total_questions}")
    for idx, qa_row in enumerate(qa_rows, start=1):
        question = qa_row["question"]
        LOGGER.info("評估中：%s/%s | %s", idx, total_questions, question[:60])
        try:
            prediction = answer_question(question)
        except Exception as exc:  # pragma: no cover - 執行期保底
            LOGGER.error("第 %s 題執行失敗：%s", idx, exc)
            prediction = {
                "question": question,
                "answer": "",
                "pages": [],
                "refused": True,
                "reason": f"answer_question 例外：{exc}",
                "retrieved_chunks": [],
            }

        record = _build_prediction_row(qa_row=qa_row, prediction=prediction)
        records.append(record)
        completed = len(records)
        running_correct = sum(1 for row in records if bool(row.get("is_correct", False)))
        running_refused = sum(1 for row in records if bool(row.get("refused", False)))
        running_hallucination = sum(1 for row in records if bool(row.get("hallucination", False)))
        running_accuracy = (running_correct / completed) if completed else 0.0
        print(
            "已完成題數: "
            f"{completed}/{total_questions} | "
            f"Accuracy: {running_accuracy:.4f} | "
            f"refused: {running_refused} | "
            f"hallucination: {running_hallucination}"
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result_df = pd.DataFrame(records)
    result_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    total_count = len(result_df)
    correct_count = int(result_df["is_correct"].sum()) if total_count else 0
    refused_count = int(result_df["refused"].sum()) if total_count else 0
    hallucination_count = int(result_df["hallucination"].sum()) if total_count else 0
    accuracy = (correct_count / total_count) if total_count else 0.0

    summary = {
        "total_count": total_count,
        "correct_count": correct_count,
        "accuracy": accuracy,
        "refused_count": refused_count,
        "hallucination_count": hallucination_count,
        "output_path": str(output_path),
    }

    print(f"題數: {total_count}")
    print(f"correct 數: {correct_count}")
    print(f"accuracy: {accuracy:.4f}")
    print(f"refused 數: {refused_count}")
    print(f"hallucination 數: {hallucination_count}")
    print(f"predictions.csv: {output_path}")

    return summary


def _build_arg_parser() -> argparse.ArgumentParser:
    """建立 CLI 參數。"""
    config = load_config()
    parser = argparse.ArgumentParser(description="批次評估富邦年報問答系統")
    parser.add_argument(
        "--qa-path",
        type=Path,
        default=config.qa_excel_path,
        help="問答集 Excel 路徑",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=config.output_dir / "predictions.csv",
        help="預測結果 CSV 輸出路徑",
    )
    parser.add_argument("--log-level", type=str, default=config.log_level, help="日誌層級")
    return parser


def main() -> int:
    """命令列入口。"""
    parser = _build_arg_parser()
    args = parser.parse_args()
    _setup_logging(level=args.log_level)

    try:
        run_evaluation(
            qa_path=args.qa_path,
            output_path=args.output_path,
        )
        return 0
    except (FileNotFoundError, ValueError) as exc:
        LOGGER.error("%s", exc)
        return 1
    except Exception as exc:  # pragma: no cover
        LOGGER.exception("評估失敗：%s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
