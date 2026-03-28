"""集中管理 RAG 問答 prompts。"""

from __future__ import annotations

import json
from typing import Any, Sequence

ANSWER_SYSTEM_PROMPT = """
你是「富邦金控年報 RAG 問答助理」。
你只能根據提供的檢索內容作答，不可使用外部知識、記憶或推測補答案。

回答規則（必須全部遵守）：
1. 只能引用檢索內容中的資訊；沒有證據就不可回答。
2. 若證據不足、互相矛盾或無法定位，必須拒答。
3. 你必須先判斷題目是否為「多子問題」：
   - 典型特徵：多個問號、出現「分別/各/比較/以及/同時/彙整/總結」等字詞。
4. 若為多子問題，answer 必須逐點對應每個子問題（例如 1. 2. 3.），不可遺漏任何子問題。
5. 每個子問題只回答與該子問題直接相關的資訊，不可跨子題混答。
6. 若涉及數字、金額、比率、年度比較，必須優先使用檢索內容中的明確數據；不得臆測。
7. 語言必須使用繁體中文與台灣用語。
6. 若問題是「單一事實/單一數值」（例如：多少、為何、幾名、幾年、比例、總額）：
   - answer 請盡量精簡成「值 + 必要單位」或「項目：值」。
   - 不要重複題目敘述，不要加背景鋪陳。
8. 若問題有多個子題：
   - answer 用分點格式，並盡量以「項目：值」呈現。
9. 答案長度需受控：
   - 多子題時，每點盡量一句，不要冗長背景。
10. 若題目要求「預測、推估、推論未來」，且檢索內容無明確可支持之預測數據，必須拒答。
11. 若題目提及的主體（公司/機構）在檢索內容中無明確證據，必須拒答。
12. 輸出必須是單一 JSON 物件，不可輸出任何額外文字、註解或 Markdown。
13. 回答範圍必須嚴格對齊題目：
   - 優先只回答題目直接要求的資訊，不要加入未被要求的延伸資訊。
   - 若題目是單一實體（例如「富邦金控」），不得自行擴展到子公司資訊，除非題目明確要求。
14. 回答風格需精簡：
   - 非多子題時，盡量用一句到兩句完成。
   - 避免背景敘述、歷程說明、重複鋪陳。
15. 若問題包含多個子問題，允許分點作答；但每點只保留與該子題直接相關的資訊。
16. JSON 結構必須為：
   {
     "answer": "最終答案",
     "pages": [1, 2],
     "refused": false,
     "reason": ""
   }
17. 若 refused=true：
   - answer 請留空字串 ""。
   - reason 必須簡短說明拒答原因（僅根據證據不足事實）。
18. 若 refused=false：
   - answer 必須可直接作為最終回答。
   - reason 必須為空字串 ""。
19. pages 需填入有依據的頁碼整數陣列，去重複並由小到大排序；若無可用頁碼可填 []。
""".strip()


REFUSAL_TEMPLATE = "抱歉，根據目前檢索到的年報內容，證據不足以回答此問題。請提供更明確問題或更多資料。"


def get_answer_system_prompt() -> str:
    """回傳問答系統 prompt。"""
    return ANSWER_SYSTEM_PROMPT


def _extract_chunk_fields(chunk: Any) -> dict[str, Any]:
    """將不同格式 chunk 轉成統一欄位。"""
    if isinstance(chunk, dict):
        chunk_id = str(chunk.get("chunk_id", ""))
        text = str(chunk.get("text", ""))
        page = chunk.get("page", chunk.get("page_start"))
        source = str(chunk.get("source", ""))
        score = chunk.get("score")
        return {
            "chunk_id": chunk_id,
            "page": page,
            "text": text,
            "source": source,
            "score": score,
        }

    chunk_id = str(getattr(chunk, "chunk_id", ""))
    text = str(getattr(chunk, "text", ""))
    page = getattr(chunk, "page", None)
    if page is None:
        page = getattr(chunk, "page_start", None)
    source = str(getattr(chunk, "source", ""))
    if not source:
        metadata = getattr(chunk, "metadata", {}) or {}
        source = str(metadata.get("source", ""))
    score = getattr(chunk, "score", None)
    return {
        "chunk_id": chunk_id,
        "page": page,
        "text": text,
        "source": source,
        "score": score,
    }


def _format_retrieved_chunks(retrieved_chunks: Sequence[Any]) -> str:
    """將檢索結果轉成穩定的 context 區塊字串。"""
    blocks: list[str] = []
    for idx, raw_chunk in enumerate(retrieved_chunks, start=1):
        chunk = _extract_chunk_fields(raw_chunk)
        if not chunk["text"].strip():
            continue

        page = chunk["page"]
        page_text = f"{page}" if isinstance(page, int) else "unknown"
        score = chunk["score"]
        score_text = f"{float(score):.4f}" if isinstance(score, (int, float)) else "n/a"
        source_text = chunk["source"] if chunk["source"] else "unknown-source"

        block = (
            f"[{idx}] chunk_id={chunk['chunk_id']} | page={page_text} | score={score_text} | source={source_text}\n"
            f"{chunk['text']}"
        )
        blocks.append(block)

    return "\n\n".join(blocks).strip()


def _build_user_prompt_from_context(question: str, context_text: str) -> str:
    """以已整理 context 產生穩定 user prompt。"""
    question_clean = question.strip()
    output_schema = {
        "answer": "最終答案",
        "pages": [1, 2],
        "refused": False,
        "reason": "",
    }
    schema_json = json.dumps(output_schema, ensure_ascii=False)

    return (
        "任務：根據檢索內容回答問題。\n"
        "限制：不可使用任何外部知識。\n\n"
        f"問題：\n{question_clean}\n\n"
        f"檢索內容：\n{context_text}\n\n"
        "輸出要求：\n"
        "1. 僅輸出單一 JSON 物件。\n"
        "2. JSON key 必須且只能為 answer, pages, refused, reason。\n"
        "3. pages 必須是整數陣列。\n"
        "4. refused=true 時 answer 必須為空字串，reason 必填。\n"
        "5. refused=false 時 reason 必須為空字串。\n\n"
        "6. 若問單一數值，answer 儘量只保留關鍵值與單位。\n"
        "7. 先判斷題目是否為多子題；若是，answer 必須用 1. 2. 3. 條列逐點對應子題。\n"
        "8. 多子題不可漏答；每點只回答該子題直接相關資訊。\n"
        "9. 多子題每點盡量一句，避免冗長背景。\n"
        "10. 只回答題目直接要求內容，不要自行延伸。\n"
        "11. 題目若為單一實體（如富邦金控），不要擴展回答到子公司，除非題目明確要求。\n"
        "12. 若題目主體在證據中找不到，或要求未來預測且無明確數據，必須拒答。\n\n"
        f"JSON 範例格式：\n{schema_json}"
    )


def build_user_prompt(question: str, retrieved_chunks: Sequence[Any]) -> str:
    """建立 user prompt（適合批次評估，穩定且結構化）。"""
    context_text = _format_retrieved_chunks(retrieved_chunks=retrieved_chunks)
    return _build_user_prompt_from_context(question=question, context_text=context_text)


def build_answer_user_prompt(question: str, retrieved_chunks: Sequence[Any] | str) -> str:
    """相容函式名稱與舊介面。"""
    if isinstance(retrieved_chunks, str):
        return _build_user_prompt_from_context(question=question, context_text=retrieved_chunks.strip())
    return build_user_prompt(question=question, retrieved_chunks=retrieved_chunks)


def build_hallucination_check_prompt(question: str, answer: str, context: str) -> str:
    """建立幻覺檢測 prompt 骨架。

    TODO:
        - 後續可加入二次檢查模型，輸出 supported/unsupported label。
        - 定義可追蹤的判斷欄位（例如 evidence_spans）。
    """
    return (
        "請檢查以下答案是否完全可由 context 支持。\n\n"
        f"【問題】{question}\n\n"
        f"【答案】{answer}\n\n"
        f"【Context】\n{context}\n\n"
        "回傳：SUPPORTED 或 UNSUPPORTED，並簡述原因。"
    )
