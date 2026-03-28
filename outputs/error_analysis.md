# Error Analysis

- generated_at: 2026-03-28 01:43:10

## evaluation definitions

- `is_correct`: 與標準答案內容一致（含等價表示）且非 true hallucination。
- `hallucination`: 回答包含證據不支持資訊（不存在/錯誤數字，或頁碼證據無法支持）。
- `formatting_difference`: 僅格式差異（空白、標點、全半形、括號），不算 hallucination。
- `error`: `not is_correct`；因此 true hallucination 一定列入 error。

## overall summary

- total_questions: 30
- correct: 30
- errors: 0
- accuracy: 1.0000
- hallucination_count: 0
- formatting_difference_count: 6
- corrected_by_format_count: 0
- hallucination_downgraded_to_format_count: 0

## error counts by type

| type | count | ratio_in_errors | ratio_in_total |
|---|---:|---:|---:|
| retrieval_error | 0 | 0.00% | 0.00% |
| synthesis_error | 0 | 0.00% | 0.00% |
| numeric_error | 0 | 0.00% | 0.00% |
| multi_question_error | 0 | 0.00% | 0.00% |
| hallucination | 0 | 0.00% | 0.00% |
| formatting_difference | 6 | 0.00% | 20.00% |
| refusal_needed_but_not_triggered | 0 | 0.00% | 0.00% |

## representative examples

### retrieval_error
無。

### synthesis_error
無。

### numeric_error
無。

### multi_question_error
無。

### hallucination
無。

### formatting_difference
1. 題號：2
   - 問題：請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
   - 標準答案：人壽：調整商品策略接軌IFRS-17與TW-ICS ; 產險：加強風險控管實踐轉型成金融生態圈
   - 預測答案：人壽：調整商品策略接軌IFRS-17與TW-ICS；產險：加強風險控管實踐轉型成金融生態圈
   - note：
   - 分類理由：僅格式差異（空白/標點/全半形/括號），內容等價。
2. 題號：12
   - 問題：根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較於 2023 年度的總量，其減碳比例約為多少？（請計算至小數點後兩位）
   - 標準答案：(59,040 - 45,594)/ 59,040=22.77%
   - 預測答案：(59,040 - 45,594)/59,040 = 22.77%
   - note：
   - 分類理由：僅格式差異（空白/標點/全半形/括號），內容等價。
3. 題號：17
   - 問題：截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
   - 標準答案：發明專利 13 件、新型專利 27 件
   - 預測答案：發明專利：13件，新型專利：27件
   - note：
   - 分類理由：僅格式差異（空白/標點/全半形/括號），內容等價。

### refusal_needed_but_not_triggered
無。

## recommended next-step improvements

1. 優化評估可讀性：持續維護格式正規化規則，避免格式差異影響指標解讀。
