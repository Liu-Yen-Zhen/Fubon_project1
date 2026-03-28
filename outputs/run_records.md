## Run Record - 2026-03-27 01:13:08

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex
- note: OPENAI_API_KEY not configured; build_index expected to fail until key is set.

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 01:13:11,904 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 01:13:11,970 | INFO | 清理後有效頁數：272
2026-03-27 01:13:11,989 | INFO | 切片完成：共 685 個 chunks
2026-03-27 01:13:11,996 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 1

```text
2026-03-27 01:13:12,753 | ERROR | 缺少 OPENAI_API_KEY，請先設定 .env。
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 1

```text
2026-03-27 01:13:13,351 | ERROR | 找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 01:13:14,453 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 01:13:14,454 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 01:13:14,455 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,456 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 01:13:14,457 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,458 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 01:13:14,459 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,459 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 01:13:14,461 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,461 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 01:13:14,463 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,463 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 01:13:14,465 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,465 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 01:13:14,466 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,467 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 01:13:14,468 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,469 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 01:13:14,470 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,470 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 01:13:14,472 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,472 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 01:13:14,473 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,474 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 01:13:14,475 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,475 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 01:13:14,477 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,477 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 01:13:14,479 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,479 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 01:13:14,480 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,480 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 01:13:14,482 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,482 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 01:13:14,483 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,484 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 01:13:14,485 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,485 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 01:13:14,487 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,487 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 01:13:14,489 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,489 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 01:13:14,490 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,491 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 01:13:14,492 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,492 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 01:13:14,494 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,494 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 01:13:14,496 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,496 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 01:13:14,497 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,497 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 01:13:14,499 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,499 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 01:13:14,501 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,501 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 01:13:14,502 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,503 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 01:13:14,504 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:13:14,504 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 01:13:14,506 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
總題數: 30
已完成題數: 1/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.0000 | refused: 3 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.0000 | refused: 4 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.0000 | refused: 5 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.0000 | refused: 6 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.0000 | refused: 7 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.0000 | refused: 8 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.0000 | refused: 9 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.0000 | refused: 10 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.0000 | refused: 11 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.0000 | refused: 12 | hallucination: 0
已完成題數: 13/30 | Accuracy: 0.0000 | refused: 13 | hallucination: 0
已完成題數: 14/30 | Accuracy: 0.0000 | refused: 14 | hallucination: 0
已完成題數: 15/30 | Accuracy: 0.0000 | refused: 15 | hallucination: 0
已完成題數: 16/30 | Accuracy: 0.0000 | refused: 16 | hallucination: 0
已完成題數: 17/30 | Accuracy: 0.0000 | refused: 17 | hallucination: 0
已完成題數: 18/30 | Accuracy: 0.0000 | refused: 18 | hallucination: 0
已完成題數: 19/30 | Accuracy: 0.0000 | refused: 19 | hallucination: 0
已完成題數: 20/30 | Accuracy: 0.0000 | refused: 20 | hallucination: 0
已完成題數: 21/30 | Accuracy: 0.0000 | refused: 21 | hallucination: 0
已完成題數: 22/30 | Accuracy: 0.0000 | refused: 22 | hallucination: 0
已完成題數: 23/30 | Accuracy: 0.0000 | refused: 23 | hallucination: 0
已完成題數: 24/30 | Accuracy: 0.0000 | refused: 24 | hallucination: 0
已完成題數: 25/30 | Accuracy: 0.0000 | refused: 25 | hallucination: 0
已完成題數: 26/30 | Accuracy: 0.0000 | refused: 26 | hallucination: 0
已完成題數: 27/30 | Accuracy: 0.0000 | refused: 27 | hallucination: 0
已完成題數: 28/30 | Accuracy: 0.0000 | refused: 28 | hallucination: 0
已完成題數: 29/30 | Accuracy: 0.0000 | refused: 29 | hallucination: 0
已完成題數: 30/30 | Accuracy: 0.0000 | refused: 30 | hallucination: 0
題數: 30
correct 數: 0
accuracy: 0.0000
refused 數: 30
hallucination 數: 0
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 0
accuracy: 0.0000
error 數: 30
retrieval_error: 30
synthesis_error: 0
numeric_error: 0
multi_question_error: 0
hallucination: 0
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 01:14:16

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex
- OPENAI_API_KEY: not set in env (will rely on .env)

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 01:14:19,834 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 01:14:19,887 | INFO | 清理後有效頁數：272
2026-03-27 01:14:19,906 | INFO | 切片完成：共 685 個 chunks
2026-03-27 01:14:19,911 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 1

```text
2026-03-27 01:14:20,738 | ERROR | 缺少 OPENAI_API_KEY，請先設定 .env。
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 1

```text
2026-03-27 01:14:21,398 | ERROR | 找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 01:14:22,286 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 01:14:22,286 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 01:14:22,288 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,288 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 01:14:22,290 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,290 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 01:14:22,292 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,292 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 01:14:22,294 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,294 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 01:14:22,296 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,296 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 01:14:22,298 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,298 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 01:14:22,299 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,300 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 01:14:22,301 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,301 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 01:14:22,303 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,303 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 01:14:22,305 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,305 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 01:14:22,307 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,307 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 01:14:22,308 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,308 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 01:14:22,310 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,310 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 01:14:22,312 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,312 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 01:14:22,313 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,314 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 01:14:22,315 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,315 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 01:14:22,317 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,317 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 01:14:22,319 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,319 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 01:14:22,320 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,321 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 01:14:22,322 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,322 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 01:14:22,324 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,324 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 01:14:22,326 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,326 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 01:14:22,328 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,328 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 01:14:22,329 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,329 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 01:14:22,331 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,331 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 01:14:22,333 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,333 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 01:14:22,335 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,335 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 01:14:22,337 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,337 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 01:14:22,338 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 01:14:22,338 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 01:14:22,340 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
總題數: 30
已完成題數: 1/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.0000 | refused: 3 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.0000 | refused: 4 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.0000 | refused: 5 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.0000 | refused: 6 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.0000 | refused: 7 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.0000 | refused: 8 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.0000 | refused: 9 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.0000 | refused: 10 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.0000 | refused: 11 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.0000 | refused: 12 | hallucination: 0
已完成題數: 13/30 | Accuracy: 0.0000 | refused: 13 | hallucination: 0
已完成題數: 14/30 | Accuracy: 0.0000 | refused: 14 | hallucination: 0
已完成題數: 15/30 | Accuracy: 0.0000 | refused: 15 | hallucination: 0
已完成題數: 16/30 | Accuracy: 0.0000 | refused: 16 | hallucination: 0
已完成題數: 17/30 | Accuracy: 0.0000 | refused: 17 | hallucination: 0
已完成題數: 18/30 | Accuracy: 0.0000 | refused: 18 | hallucination: 0
已完成題數: 19/30 | Accuracy: 0.0000 | refused: 19 | hallucination: 0
已完成題數: 20/30 | Accuracy: 0.0000 | refused: 20 | hallucination: 0
已完成題數: 21/30 | Accuracy: 0.0000 | refused: 21 | hallucination: 0
已完成題數: 22/30 | Accuracy: 0.0000 | refused: 22 | hallucination: 0
已完成題數: 23/30 | Accuracy: 0.0000 | refused: 23 | hallucination: 0
已完成題數: 24/30 | Accuracy: 0.0000 | refused: 24 | hallucination: 0
已完成題數: 25/30 | Accuracy: 0.0000 | refused: 25 | hallucination: 0
已完成題數: 26/30 | Accuracy: 0.0000 | refused: 26 | hallucination: 0
已完成題數: 27/30 | Accuracy: 0.0000 | refused: 27 | hallucination: 0
已完成題數: 28/30 | Accuracy: 0.0000 | refused: 28 | hallucination: 0
已完成題數: 29/30 | Accuracy: 0.0000 | refused: 29 | hallucination: 0
已完成題數: 30/30 | Accuracy: 0.0000 | refused: 30 | hallucination: 0
題數: 30
correct 數: 0
accuracy: 0.0000
refused 數: 30
hallucination 數: 0
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 0
accuracy: 0.0000
error 數: 30
retrieval_error: 30
synthesis_error: 0
numeric_error: 0
multi_question_error: 0
hallucination: 0
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 08:24:48

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:24:52,730 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 08:24:52,783 | INFO | 清理後有效頁數：272
2026-03-27 08:24:52,801 | INFO | 切片完成：共 685 個 chunks
2026-03-27 08:24:52,808 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 1

```text
2026-03-27 08:24:53,639 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 08:24:53,639 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 08:24:53,643 | INFO | 已載入 chunks：685 筆
2026-03-27 08:24:53,858 | INFO | Retrying request to /embeddings in 0.435334 seconds
2026-03-27 08:24:54,299 | INFO | Retrying request to /embeddings in 0.858662 seconds
2026-03-27 08:24:55,163 | WARNING | Embedding 批次失敗，1.5 秒後重試（1/1）：Connection error.
2026-03-27 08:24:56,667 | INFO | Retrying request to /embeddings in 0.444853 seconds
2026-03-27 08:24:57,117 | INFO | Retrying request to /embeddings in 0.808381 seconds
2026-03-27 08:24:57,932 | ERROR | Embedding 批次失敗（已重試 1 次）：Connection error.
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 1

```text
2026-03-27 08:24:58,594 | ERROR | 找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:24:59,852 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 08:24:59,853 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 08:24:59,854 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,855 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 08:24:59,857 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,857 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 08:24:59,858 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,859 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 08:24:59,860 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,860 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 08:24:59,862 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,862 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 08:24:59,864 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,864 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 08:24:59,865 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,865 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 08:24:59,867 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,867 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 08:24:59,869 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,869 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 08:24:59,871 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,871 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 08:24:59,873 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,873 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 08:24:59,874 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,874 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 08:24:59,876 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,876 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 08:24:59,878 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,878 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 08:24:59,879 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,879 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 08:24:59,881 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,881 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 08:24:59,883 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,883 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 08:24:59,884 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,885 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 08:24:59,886 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,886 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 08:24:59,888 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,888 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 08:24:59,889 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,890 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 08:24:59,891 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,891 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 08:24:59,893 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,893 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 08:24:59,895 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,895 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 08:24:59,897 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,897 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 08:24:59,898 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,899 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 08:24:59,900 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,900 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 08:24:59,902 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,902 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 08:24:59,904 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:24:59,904 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 08:24:59,905 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
總題數: 30
已完成題數: 1/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.0000 | refused: 3 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.0000 | refused: 4 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.0000 | refused: 5 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.0000 | refused: 6 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.0000 | refused: 7 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.0000 | refused: 8 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.0000 | refused: 9 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.0000 | refused: 10 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.0000 | refused: 11 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.0000 | refused: 12 | hallucination: 0
已完成題數: 13/30 | Accuracy: 0.0000 | refused: 13 | hallucination: 0
已完成題數: 14/30 | Accuracy: 0.0000 | refused: 14 | hallucination: 0
已完成題數: 15/30 | Accuracy: 0.0000 | refused: 15 | hallucination: 0
已完成題數: 16/30 | Accuracy: 0.0000 | refused: 16 | hallucination: 0
已完成題數: 17/30 | Accuracy: 0.0000 | refused: 17 | hallucination: 0
已完成題數: 18/30 | Accuracy: 0.0000 | refused: 18 | hallucination: 0
已完成題數: 19/30 | Accuracy: 0.0000 | refused: 19 | hallucination: 0
已完成題數: 20/30 | Accuracy: 0.0000 | refused: 20 | hallucination: 0
已完成題數: 21/30 | Accuracy: 0.0000 | refused: 21 | hallucination: 0
已完成題數: 22/30 | Accuracy: 0.0000 | refused: 22 | hallucination: 0
已完成題數: 23/30 | Accuracy: 0.0000 | refused: 23 | hallucination: 0
已完成題數: 24/30 | Accuracy: 0.0000 | refused: 24 | hallucination: 0
已完成題數: 25/30 | Accuracy: 0.0000 | refused: 25 | hallucination: 0
已完成題數: 26/30 | Accuracy: 0.0000 | refused: 26 | hallucination: 0
已完成題數: 27/30 | Accuracy: 0.0000 | refused: 27 | hallucination: 0
已完成題數: 28/30 | Accuracy: 0.0000 | refused: 28 | hallucination: 0
已完成題數: 29/30 | Accuracy: 0.0000 | refused: 29 | hallucination: 0
已完成題數: 30/30 | Accuracy: 0.0000 | refused: 30 | hallucination: 0
題數: 30
correct 數: 0
accuracy: 0.0000
refused 數: 30
hallucination 數: 0
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 0
accuracy: 0.0000
error 數: 30
retrieval_error: 30
synthesis_error: 0
numeric_error: 0
multi_question_error: 0
hallucination: 0
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```


## Run Record - 2026-03-27 08:26:06

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex
- note: manual retry for build_index (escalated network)

### Build Index (Escalated Retry)

- command: `python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 2 --log-level INFO`
- exit_code: 1

```text
OpenAI Embeddings API 回傳 401 Unauthorized。
原因：invalid_api_key（目前 .env 的 OPENAI_API_KEY 值長度僅 10，屬於不完整 key）。
```


## Run Record - 2026-03-27 08:36:13

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex
- note: manual build_index run with escalated network

### Build Index (Escalated)

- command: `python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 2 --log-level INFO`
- exit_code: 1

```text
OpenAI Embeddings API 回傳 429 insufficient_quota。
message: You exceeded your current quota, please check your plan and billing details.
結論：API key 有效，但帳戶/專案目前額度不足，索引未建立。
```

## Run Record - 2026-03-27 08:37:25

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:37:31,250 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 08:37:31,333 | INFO | 清理後有效頁數：272
2026-03-27 08:37:31,363 | INFO | 切片完成：共 685 個 chunks
2026-03-27 08:37:31,372 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

## Run Record - 2026-03-27 08:39:24

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:39:27,318 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 08:39:27,371 | INFO | 清理後有效頁數：272
2026-03-27 08:39:27,389 | INFO | 切片完成：共 685 個 chunks
2026-03-27 08:39:27,396 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 1

```text
2026-03-27 08:39:28,119 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 08:39:28,119 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 08:39:28,123 | INFO | 已載入 chunks：685 筆
2026-03-27 08:39:28,587 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:39:28,638 | INFO | Embedding 進度：1/22 batches
2026-03-27 08:39:29,038 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:39:29,112 | INFO | Embedding 進度：2/22 batches
2026-03-27 08:39:29,460 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:39:29,485 | INFO | Embedding 進度：3/22 batches
2026-03-27 08:39:30,455 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:39:30,507 | INFO | Embedding 進度：4/22 batches
2026-03-27 08:39:30,598 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:39:30,599 | INFO | Retrying request to /embeddings in 4.059000 seconds
2026-03-27 08:39:34,761 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:39:34,762 | INFO | Retrying request to /embeddings in 15.853000 seconds
2026-03-27 08:39:51,337 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:39:51,464 | INFO | Embedding 進度：5/22 batches
2026-03-27 08:39:51,575 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:39:51,575 | INFO | Retrying request to /embeddings in 18.870000 seconds
2026-03-27 08:40:10,924 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:40:11,052 | INFO | Embedding 進度：6/22 batches
2026-03-27 08:40:11,508 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:40:11,648 | INFO | Embedding 進度：7/22 batches
2026-03-27 08:40:12,337 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:40:12,337 | INFO | Retrying request to /embeddings in 19.303000 seconds
2026-03-27 08:40:31,806 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:40:31,808 | INFO | Retrying request to /embeddings in 17.674000 seconds
2026-03-27 08:40:49,628 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:40:49,635 | WARNING | Embedding 批次失敗，1.5 秒後重試（1/1）：Error code: 429 - {'error': {'message': 'Rate limit reached for text-embedding-3-large in organization org-dyNUPXIoECkfVPLNpyUwcgoX on tokens per min (TPM): Limit 40000, Used 27278, Requested 12869. Please try again in 220ms. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}
2026-03-27 08:40:51,575 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:40:51,625 | INFO | Embedding 進度：8/22 batches
2026-03-27 08:40:52,032 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:40:52,060 | INFO | Embedding 進度：9/22 batches
2026-03-27 08:40:52,135 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:40:52,135 | INFO | Retrying request to /embeddings in 14.286000 seconds
2026-03-27 08:41:06,553 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:41:06,553 | INFO | Retrying request to /embeddings in 16.956000 seconds
2026-03-27 08:41:23,646 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:41:23,649 | WARNING | Embedding 批次失敗，1.5 秒後重試（1/1）：Error code: 429 - {'error': {'message': 'Rate limit reached for text-embedding-3-large in organization org-dyNUPXIoECkfVPLNpyUwcgoX on tokens per min (TPM): Limit 40000, Used 29124, Requested 11304. Please try again in 642ms. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}
2026-03-27 08:41:25,517 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:41:25,653 | INFO | Embedding 進度：10/22 batches
2026-03-27 08:41:25,762 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:41:25,763 | INFO | Retrying request to /embeddings in 17.121000 seconds
2026-03-27 08:41:43,501 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:41:43,700 | INFO | Embedding 進度：11/22 batches
2026-03-27 08:41:43,854 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:41:43,855 | INFO | Retrying request to /embeddings in 18.679000 seconds
2026-03-27 08:42:02,676 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:42:02,677 | INFO | Retrying request to /embeddings in 0.169000 seconds
2026-03-27 08:42:03,168 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:42:03,259 | INFO | Embedding 進度：12/22 batches
2026-03-27 08:42:03,358 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:42:03,359 | INFO | Retrying request to /embeddings in 20.764000 seconds
2026-03-27 08:42:24,644 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:42:24,726 | INFO | Embedding 進度：13/22 batches
2026-03-27 08:42:24,802 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:42:24,802 | INFO | Retrying request to /embeddings in 20.149000 seconds
2026-03-27 08:42:45,088 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:42:45,089 | INFO | Retrying request to /embeddings in 17.070000 seconds
2026-03-27 08:43:02,299 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:43:02,302 | WARNING | Embedding 批次失敗，1.5 秒後重試（1/1）：Error code: 429 - {'error': {'message': 'Rate limit reached for text-embedding-3-large in organization org-dyNUPXIoECkfVPLNpyUwcgoX on tokens per min (TPM): Limit 40000, Used 39288, Requested 13886. Please try again in 19.761s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}
2026-03-27 08:43:03,887 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:43:03,887 | INFO | Retrying request to /embeddings in 18.163000 seconds
2026-03-27 08:43:22,203 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:43:22,205 | INFO | Retrying request to /embeddings in 20.829000 seconds
2026-03-27 08:43:43,194 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 429 Too Many Requests"
2026-03-27 08:43:43,197 | ERROR | Embedding 批次失敗（已重試 1 次）：Error code: 429 - {'error': {'message': 'Rate limit reached for text-embedding-3-large in organization org-dyNUPXIoECkfVPLNpyUwcgoX on tokens per min (TPM): Limit 40000, Used 40000, Requested 13886. Please try again in 20.829s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.', 'type': 'tokens', 'param': None, 'code': 'rate_limit_exceeded'}}
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 1

```text
2026-03-27 08:43:43,978 | ERROR | 找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:43:45,003 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 08:43:45,003 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 08:43:45,004 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,005 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 08:43:45,006 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,006 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 08:43:45,008 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,008 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 08:43:45,009 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,009 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 08:43:45,011 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,011 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 08:43:45,012 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,012 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 08:43:45,014 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,014 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 08:43:45,015 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,015 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 08:43:45,017 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,017 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 08:43:45,018 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,019 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 08:43:45,021 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,021 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 08:43:45,023 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,023 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 08:43:45,024 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,024 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 08:43:45,025 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,025 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 08:43:45,027 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,027 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 08:43:45,028 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,028 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 08:43:45,030 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,030 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 08:43:45,031 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,031 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 08:43:45,033 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,033 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 08:43:45,034 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,034 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 08:43:45,036 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,036 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 08:43:45,037 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,037 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 08:43:45,039 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,039 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 08:43:45,040 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,040 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 08:43:45,042 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,042 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 08:43:45,043 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,043 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 08:43:45,045 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,045 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 08:43:45,046 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,046 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 08:43:45,048 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
2026-03-27 08:43:45,048 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 08:43:45,049 | ERROR | 檢索失敗：找不到索引檔。已搜尋：/Users/liuyenzhen/Desktop/Fubon_codex/outputs/faiss.index。請先執行：python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs
總題數: 30
已完成題數: 1/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.0000 | refused: 3 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.0000 | refused: 4 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.0000 | refused: 5 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.0000 | refused: 6 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.0000 | refused: 7 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.0000 | refused: 8 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.0000 | refused: 9 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.0000 | refused: 10 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.0000 | refused: 11 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.0000 | refused: 12 | hallucination: 0
已完成題數: 13/30 | Accuracy: 0.0000 | refused: 13 | hallucination: 0
已完成題數: 14/30 | Accuracy: 0.0000 | refused: 14 | hallucination: 0
已完成題數: 15/30 | Accuracy: 0.0000 | refused: 15 | hallucination: 0
已完成題數: 16/30 | Accuracy: 0.0000 | refused: 16 | hallucination: 0
已完成題數: 17/30 | Accuracy: 0.0000 | refused: 17 | hallucination: 0
已完成題數: 18/30 | Accuracy: 0.0000 | refused: 18 | hallucination: 0
已完成題數: 19/30 | Accuracy: 0.0000 | refused: 19 | hallucination: 0
已完成題數: 20/30 | Accuracy: 0.0000 | refused: 20 | hallucination: 0
已完成題數: 21/30 | Accuracy: 0.0000 | refused: 21 | hallucination: 0
已完成題數: 22/30 | Accuracy: 0.0000 | refused: 22 | hallucination: 0
已完成題數: 23/30 | Accuracy: 0.0000 | refused: 23 | hallucination: 0
已完成題數: 24/30 | Accuracy: 0.0000 | refused: 24 | hallucination: 0
已完成題數: 25/30 | Accuracy: 0.0000 | refused: 25 | hallucination: 0
已完成題數: 26/30 | Accuracy: 0.0000 | refused: 26 | hallucination: 0
已完成題數: 27/30 | Accuracy: 0.0000 | refused: 27 | hallucination: 0
已完成題數: 28/30 | Accuracy: 0.0000 | refused: 28 | hallucination: 0
已完成題數: 29/30 | Accuracy: 0.0000 | refused: 29 | hallucination: 0
已完成題數: 30/30 | Accuracy: 0.0000 | refused: 30 | hallucination: 0
題數: 30
correct 數: 0
accuracy: 0.0000
refused 數: 30
hallucination 數: 0
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 0
accuracy: 0.0000
error 數: 30
retrieval_error: 30
synthesis_error: 0
numeric_error: 0
multi_question_error: 0
hallucination: 0
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 08:49:55

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:49:58,184 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 08:49:58,235 | INFO | 清理後有效頁數：272
2026-03-27 08:49:58,252 | INFO | 切片完成：共 685 個 chunks
2026-03-27 08:49:58,259 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:49:58,793 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 08:49:58,793 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 08:49:58,796 | INFO | 已載入 chunks：685 筆
2026-03-27 08:49:59,501 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:49:59,598 | INFO | Embedding 進度：1/22 batches
2026-03-27 08:49:59,930 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:49:59,984 | INFO | Embedding 進度：2/22 batches
2026-03-27 08:50:00,282 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:00,359 | INFO | Embedding 進度：3/22 batches
2026-03-27 08:50:00,696 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:00,776 | INFO | Embedding 進度：4/22 batches
2026-03-27 08:50:01,129 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:01,203 | INFO | Embedding 進度：5/22 batches
2026-03-27 08:50:01,543 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:01,582 | INFO | Embedding 進度：6/22 batches
2026-03-27 08:50:02,013 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:02,041 | INFO | Embedding 進度：7/22 batches
2026-03-27 08:50:02,431 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:02,572 | INFO | Embedding 進度：8/22 batches
2026-03-27 08:50:02,971 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:03,118 | INFO | Embedding 進度：9/22 batches
2026-03-27 08:50:03,459 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:03,568 | INFO | Embedding 進度：10/22 batches
2026-03-27 08:50:03,886 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:03,986 | INFO | Embedding 進度：11/22 batches
2026-03-27 08:50:04,312 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:04,390 | INFO | Embedding 進度：12/22 batches
2026-03-27 08:50:04,802 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:04,865 | INFO | Embedding 進度：13/22 batches
2026-03-27 08:50:05,175 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:05,251 | INFO | Embedding 進度：14/22 batches
2026-03-27 08:50:05,657 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:05,790 | INFO | Embedding 進度：15/22 batches
2026-03-27 08:50:06,177 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:06,290 | INFO | Embedding 進度：16/22 batches
2026-03-27 08:50:06,658 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:06,733 | INFO | Embedding 進度：17/22 batches
2026-03-27 08:50:07,119 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:07,156 | INFO | Embedding 進度：18/22 batches
2026-03-27 08:50:07,438 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:07,456 | INFO | Embedding 進度：19/22 batches
2026-03-27 08:50:07,880 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:07,901 | INFO | Embedding 進度：20/22 batches
2026-03-27 08:50:08,355 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:08,385 | INFO | Embedding 進度：21/22 batches
2026-03-27 08:50:08,716 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:08,731 | INFO | Embedding 進度：22/22 batches
2026-03-27 08:50:08,801 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 08:50:08,815 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 08:50:08,825 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:50:09,736 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5633891820907593,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.561187207698822,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.5350567698478699,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0007-c002",
      "page": 7,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.534486711025238,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.5141976475715637,
      "source": "113年報.pdf#page=156"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 08:50:10,553 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 08:50:10,553 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 08:50:10,864 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:12,295 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:12,311 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 08:50:12,498 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:17,552 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:17,564 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 08:50:17,772 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:19,430 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:19,436 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 08:50:19,631 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:21,076 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:21,080 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 08:50:21,256 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:22,651 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:22,656 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 08:50:22,878 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:25,259 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:25,263 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 08:50:25,464 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:30,062 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:30,067 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 08:50:30,316 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:31,769 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:31,779 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 08:50:31,995 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:35,090 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:35,100 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 08:50:35,288 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:37,139 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:37,148 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 08:50:37,354 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:38,288 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:38,296 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 08:50:38,498 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:40,895 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:40,903 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 08:50:41,128 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:42,644 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:42,653 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 08:50:42,888 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:47,828 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:47,835 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 08:50:48,083 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:49,682 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:49,690 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 08:50:50,022 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:51,722 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:51,734 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 08:50:51,935 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:53,595 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:53,604 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 08:50:53,851 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:55,033 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:55,041 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 08:50:55,253 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:56,635 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:56,643 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 08:50:56,875 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:50:58,259 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:50:58,268 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 08:50:58,500 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:00,397 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:00,405 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 08:51:00,645 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:02,736 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:02,744 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 08:51:02,980 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:11,558 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:11,567 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 08:51:11,813 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:18,923 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:18,932 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 08:51:19,275 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:24,052 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:24,057 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 08:51:24,274 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:28,188 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:28,216 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 08:51:28,418 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:29,876 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:29,889 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 08:51:30,103 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:32,011 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:32,020 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 08:51:32,266 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:33,954 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 08:51:33,963 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 08:51:34,151 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 08:51:36,047 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 0.0000 | refused: 0 | hallucination: 1
已完成題數: 2/30 | Accuracy: 0.0000 | refused: 0 | hallucination: 1
已完成題數: 3/30 | Accuracy: 0.0000 | refused: 0 | hallucination: 2
已完成題數: 4/30 | Accuracy: 0.0000 | refused: 0 | hallucination: 2
已完成題數: 5/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 6/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 7/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 8/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 9/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 10/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 11/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 2
已完成題數: 12/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 3
已完成題數: 13/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 3
已完成題數: 14/30 | Accuracy: 0.0000 | refused: 1 | hallucination: 3
已完成題數: 15/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 16/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 17/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 18/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 19/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 20/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 21/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 3
已完成題數: 22/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 23/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 24/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 25/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 26/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 27/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 4
已完成題數: 28/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 5
已完成題數: 29/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 6
已完成題數: 30/30 | Accuracy: 0.0000 | refused: 2 | hallucination: 6
題數: 30
correct 數: 0
accuracy: 0.0000
refused 數: 2
hallucination 數: 6
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 0
accuracy: 0.0000
error 數: 30
retrieval_error: 0
synthesis_error: 14
numeric_error: 7
multi_question_error: 3
hallucination: 4
refusal_needed_but_not_triggered: 2
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 09:02:36

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:02:39,178 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 09:02:39,230 | INFO | 清理後有效頁數：272
2026-03-27 09:02:39,248 | INFO | 切片完成：共 685 個 chunks
2026-03-27 09:02:39,254 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:02:39,899 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 09:02:39,899 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:02:39,903 | INFO | 已載入 chunks：685 筆
2026-03-27 09:02:40,912 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:40,974 | INFO | Embedding 進度：1/22 batches
2026-03-27 09:02:41,310 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:41,335 | INFO | Embedding 進度：2/22 batches
2026-03-27 09:02:41,668 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:41,715 | INFO | Embedding 進度：3/22 batches
2026-03-27 09:02:42,040 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:42,061 | INFO | Embedding 進度：4/22 batches
2026-03-27 09:02:42,463 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:42,483 | INFO | Embedding 進度：5/22 batches
2026-03-27 09:02:42,958 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:42,991 | INFO | Embedding 進度：6/22 batches
2026-03-27 09:02:43,642 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:43,665 | INFO | Embedding 進度：7/22 batches
2026-03-27 09:02:44,063 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:44,083 | INFO | Embedding 進度：8/22 batches
2026-03-27 09:02:44,542 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:44,565 | INFO | Embedding 進度：9/22 batches
2026-03-27 09:02:44,855 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:44,881 | INFO | Embedding 進度：10/22 batches
2026-03-27 09:02:45,280 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:45,304 | INFO | Embedding 進度：11/22 batches
2026-03-27 09:02:45,630 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:45,650 | INFO | Embedding 進度：12/22 batches
2026-03-27 09:02:46,034 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:46,056 | INFO | Embedding 進度：13/22 batches
2026-03-27 09:02:46,469 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:46,481 | INFO | Embedding 進度：14/22 batches
2026-03-27 09:02:46,925 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:46,961 | INFO | Embedding 進度：15/22 batches
2026-03-27 09:02:47,365 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:47,389 | INFO | Embedding 進度：16/22 batches
2026-03-27 09:02:47,755 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:47,783 | INFO | Embedding 進度：17/22 batches
2026-03-27 09:02:48,181 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:48,198 | INFO | Embedding 進度：18/22 batches
2026-03-27 09:02:48,487 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:48,510 | INFO | Embedding 進度：19/22 batches
2026-03-27 09:02:48,903 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:48,927 | INFO | Embedding 進度：20/22 batches
2026-03-27 09:02:49,370 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:49,394 | INFO | Embedding 進度：21/22 batches
2026-03-27 09:02:49,656 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:49,662 | INFO | Embedding 進度：22/22 batches
2026-03-27 09:02:49,735 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 09:02:49,752 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:02:49,764 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:02:51,120 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5214056694507598,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.49843545675277706,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0155-c001",
      "page": 155,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.48210775971412656,
      "source": "113年報.pdf#page=155"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4532334470748901,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0154-c002",
      "page": 154,
      "text": "交換或 認股)普通股、海 外存託憑證或其 他有價證券之金 額 無 無 發行及轉換 (交換 或認股)辦法 無 無 發行及轉換 、 交換或認股辦法 、 發行條件對股權可能稀釋情形 及對現有股東權益影響 無 無 交換標的委託保管機構名稱 無 無 - 148 - 3.3 特特別別股股發發行行情情形形 1. 富邦金控甲種特別股 發行(辦理)日期 項 目 2016 年 4 月 22 日 (富邦金控甲種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 600,000 千股 總額 新台幣 36,000,000,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：甲種特別股年率 4.10%(七年期 IRS 0.885%+3.215%)，按每股發行價 格計算。 七年期 IRS 利率將於發行日起滿七年之次日及其後每七年重設。 甲種特別股自 2023 年 4 月 22 日起重設年率為 4.58125%。 2. 股息發放：本公司對於甲種特別股之股息分派具自主裁量權，包括但不限 於因年度決算無盈餘或盈餘不足分派特別股股息，或因特別股股息之分派 將使本公司資本適足率低於法令或主管機關所定最低要求。 本公司決議取 消特別股之股息分派，將不構成違約事件。 其未分派或分派不足額之股 息，不累積於以後有盈餘年度遞延償付。 本公司決算如有盈餘，應先完納 稅捐、彌補虧損，依法令規定提列法定盈餘公積並依法令規定或實際需要 提列特別盈餘公積，並得分派本公司甲種特別股股息。 甲種特別股股息每 年以現金一次發放，於每年股東常會承認財務報告後，由董事會訂定基準 日支付前一年度得發放之股息。 發行年度及收回年度股息之發放，按當年 度實際發行天數計算，所分配股息將認列於股利憑單。 3. 超額股利分配：甲種特別股除依前述所定之股息率領取股息外，不得參加",
      "score": 0.4530540484189987,
      "source": "113年報.pdf#page=154"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:02:52,140 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 09:02:52,140 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 09:02:52,504 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:54,598 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:02:54,605 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 09:02:54,809 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:02:59,616 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:02:59,625 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 09:02:59,841 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:01,259 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:01,266 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 09:03:01,462 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:02,791 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:02,798 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 09:03:03,006 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:04,891 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:04,904 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 09:03:05,127 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:17,278 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:17,295 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 09:03:17,489 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:25,669 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:25,675 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 09:03:25,901 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:27,364 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:27,370 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 09:03:27,575 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:31,646 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:31,655 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 09:03:31,871 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:33,406 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:33,412 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 09:03:33,634 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:35,130 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:35,138 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 09:03:35,354 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:37,032 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:37,040 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 09:03:37,296 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:38,437 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:38,445 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 09:03:38,627 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:40,884 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:40,891 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 09:03:41,120 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:42,420 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:42,426 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 09:03:42,629 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:43,856 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:43,869 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 09:03:44,070 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:45,201 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:45,209 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 09:03:45,417 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:46,924 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:46,931 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 09:03:47,144 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:48,082 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:48,088 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 09:03:48,272 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:49,488 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:49,498 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 09:03:49,712 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:51,126 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:51,136 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 09:03:51,334 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:53,378 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:53,388 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 09:03:53,597 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:03:56,961 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:03:56,969 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 09:03:57,244 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:01,772 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:04:01,780 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 09:04:02,033 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:05,155 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:04:05,166 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 09:04:05,387 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:06,895 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:04:06,903 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 09:04:07,124 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:11,298 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:04:11,312 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 09:04:11,518 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:11,529 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 09:04:11,736 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:11,753 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 09:04:11,974 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:04:13,032 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 1
已完成題數: 3/30 | Accuracy: 0.3333 | refused: 0 | hallucination: 1
已完成題數: 4/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 1
已完成題數: 5/30 | Accuracy: 0.4000 | refused: 0 | hallucination: 1
已完成題數: 6/30 | Accuracy: 0.3333 | refused: 0 | hallucination: 1
已完成題數: 7/30 | Accuracy: 0.2857 | refused: 0 | hallucination: 1
已完成題數: 8/30 | Accuracy: 0.2500 | refused: 0 | hallucination: 1
已完成題數: 9/30 | Accuracy: 0.2222 | refused: 0 | hallucination: 1
已完成題數: 10/30 | Accuracy: 0.3000 | refused: 0 | hallucination: 1
已完成題數: 11/30 | Accuracy: 0.3636 | refused: 0 | hallucination: 1
已完成題數: 12/30 | Accuracy: 0.3333 | refused: 1 | hallucination: 1
已完成題數: 13/30 | Accuracy: 0.3077 | refused: 1 | hallucination: 1
已完成題數: 14/30 | Accuracy: 0.3571 | refused: 1 | hallucination: 1
已完成題數: 15/30 | Accuracy: 0.3333 | refused: 2 | hallucination: 1
已完成題數: 16/30 | Accuracy: 0.3750 | refused: 2 | hallucination: 1
已完成題數: 17/30 | Accuracy: 0.4118 | refused: 2 | hallucination: 1
已完成題數: 18/30 | Accuracy: 0.4444 | refused: 2 | hallucination: 1
已完成題數: 19/30 | Accuracy: 0.4737 | refused: 2 | hallucination: 1
已完成題數: 20/30 | Accuracy: 0.5000 | refused: 2 | hallucination: 1
已完成題數: 21/30 | Accuracy: 0.5238 | refused: 2 | hallucination: 1
已完成題數: 22/30 | Accuracy: 0.5000 | refused: 2 | hallucination: 1
已完成題數: 23/30 | Accuracy: 0.4783 | refused: 2 | hallucination: 1
已完成題數: 24/30 | Accuracy: 0.4583 | refused: 2 | hallucination: 1
已完成題數: 25/30 | Accuracy: 0.4400 | refused: 2 | hallucination: 1
已完成題數: 26/30 | Accuracy: 0.4231 | refused: 2 | hallucination: 1
已完成題數: 27/30 | Accuracy: 0.4444 | refused: 2 | hallucination: 1
已完成題數: 28/30 | Accuracy: 0.4286 | refused: 3 | hallucination: 1
已完成題數: 29/30 | Accuracy: 0.4138 | refused: 4 | hallucination: 1
已完成題數: 30/30 | Accuracy: 0.4333 | refused: 4 | hallucination: 1
題數: 30
correct 數: 13
accuracy: 0.4333
refused 數: 4
hallucination 數: 1
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 13
accuracy: 0.4333
error 數: 17
retrieval_error: 0
synthesis_error: 8
numeric_error: 6
multi_question_error: 2
hallucination: 1
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 09:06:23

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:06:27,065 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 09:06:27,116 | INFO | 清理後有效頁數：272
2026-03-27 09:06:27,134 | INFO | 切片完成：共 685 個 chunks
2026-03-27 09:06:27,140 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:06:27,825 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 09:06:27,825 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:06:27,829 | INFO | 已載入 chunks：685 筆
2026-03-27 09:06:28,308 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:28,452 | INFO | Embedding 進度：1/22 batches
2026-03-27 09:06:28,794 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:28,841 | INFO | Embedding 進度：2/22 batches
2026-03-27 09:06:29,152 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:29,255 | INFO | Embedding 進度：3/22 batches
2026-03-27 09:06:29,566 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:29,589 | INFO | Embedding 進度：4/22 batches
2026-03-27 09:06:29,984 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:30,069 | INFO | Embedding 進度：5/22 batches
2026-03-27 09:06:30,463 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:30,486 | INFO | Embedding 進度：6/22 batches
2026-03-27 09:06:30,929 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:31,007 | INFO | Embedding 進度：7/22 batches
2026-03-27 09:06:31,393 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:31,448 | INFO | Embedding 進度：8/22 batches
2026-03-27 09:06:31,899 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:31,947 | INFO | Embedding 進度：9/22 batches
2026-03-27 09:06:32,296 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:32,394 | INFO | Embedding 進度：10/22 batches
2026-03-27 09:06:32,714 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:32,736 | INFO | Embedding 進度：11/22 batches
2026-03-27 09:06:33,125 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:33,150 | INFO | Embedding 進度：12/22 batches
2026-03-27 09:06:33,637 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:33,687 | INFO | Embedding 進度：13/22 batches
2026-03-27 09:06:34,150 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:34,173 | INFO | Embedding 進度：14/22 batches
2026-03-27 09:06:34,619 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:34,652 | INFO | Embedding 進度：15/22 batches
2026-03-27 09:06:35,076 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:35,091 | INFO | Embedding 進度：16/22 batches
2026-03-27 09:06:35,481 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:35,502 | INFO | Embedding 進度：17/22 batches
2026-03-27 09:06:35,981 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:35,996 | INFO | Embedding 進度：18/22 batches
2026-03-27 09:06:36,316 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:36,353 | INFO | Embedding 進度：19/22 batches
2026-03-27 09:06:36,780 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:36,805 | INFO | Embedding 進度：20/22 batches
2026-03-27 09:06:37,331 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:37,354 | INFO | Embedding 進度：21/22 batches
2026-03-27 09:06:37,735 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:37,743 | INFO | Embedding 進度：22/22 batches
2026-03-27 09:06:37,817 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 09:06:37,832 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:06:37,843 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:06:38,901 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5214702832698821,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.5004899024963378,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.47846255302429197,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4527211064100265,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0270-c001",
      "page": 270,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.45075397729873656,
      "source": "113年報.pdf#page=270"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:06:39,976 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 09:06:39,976 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 09:06:40,547 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:42,813 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:42,825 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 09:06:43,046 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:47,667 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:47,676 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 09:06:47,898 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:49,306 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:49,313 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 09:06:49,520 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:50,791 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:50,800 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 09:06:51,030 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:53,197 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:53,210 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 09:06:53,451 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:06:55,243 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:06:55,254 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 09:06:55,470 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:01,921 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:01,933 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 09:07:02,144 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:03,745 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:03,755 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 09:07:04,015 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:07,017 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:07,024 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 09:07:07,231 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:08,811 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:08,820 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 09:07:09,057 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:10,807 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:10,812 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 09:07:11,004 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:13,890 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:13,897 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 09:07:14,138 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:15,668 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:15,675 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 09:07:15,900 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:18,112 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:18,119 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 09:07:18,344 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:19,515 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:19,521 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 09:07:19,742 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:20,910 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:20,923 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 09:07:21,132 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:22,953 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:22,962 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 09:07:23,197 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:24,532 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:24,541 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 09:07:24,745 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:25,760 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:25,768 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 09:07:25,978 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:27,603 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:27,612 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 09:07:27,818 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:28,981 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:28,990 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 09:07:29,249 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:30,675 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:30,683 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 09:07:30,910 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:36,206 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:36,216 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 09:07:36,402 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:39,976 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:39,980 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 09:07:40,209 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:43,784 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:43,790 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 09:07:44,024 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:46,366 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:46,374 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 09:07:46,591 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:47,893 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:07:47,903 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 09:07:48,118 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:48,130 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 09:07:48,322 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:48,337 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 09:07:48,550 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:07:50,160 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.6000 | refused: 0 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.4286 | refused: 1 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.4444 | refused: 1 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.4000 | refused: 1 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.4545 | refused: 1 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.4167 | refused: 1 | hallucination: 1
已完成題數: 13/30 | Accuracy: 0.3846 | refused: 1 | hallucination: 1
已完成題數: 14/30 | Accuracy: 0.4286 | refused: 1 | hallucination: 1
已完成題數: 15/30 | Accuracy: 0.4000 | refused: 2 | hallucination: 1
已完成題數: 16/30 | Accuracy: 0.4375 | refused: 2 | hallucination: 1
已完成題數: 17/30 | Accuracy: 0.4706 | refused: 2 | hallucination: 1
已完成題數: 18/30 | Accuracy: 0.5000 | refused: 2 | hallucination: 1
已完成題數: 19/30 | Accuracy: 0.5263 | refused: 2 | hallucination: 1
已完成題數: 20/30 | Accuracy: 0.5500 | refused: 2 | hallucination: 1
已完成題數: 21/30 | Accuracy: 0.5714 | refused: 2 | hallucination: 1
已完成題數: 22/30 | Accuracy: 0.5455 | refused: 2 | hallucination: 1
已完成題數: 23/30 | Accuracy: 0.5217 | refused: 3 | hallucination: 1
已完成題數: 24/30 | Accuracy: 0.5000 | refused: 3 | hallucination: 1
已完成題數: 25/30 | Accuracy: 0.4800 | refused: 3 | hallucination: 1
已完成題數: 26/30 | Accuracy: 0.5000 | refused: 3 | hallucination: 2
已完成題數: 27/30 | Accuracy: 0.5185 | refused: 3 | hallucination: 2
已完成題數: 28/30 | Accuracy: 0.5000 | refused: 4 | hallucination: 2
已完成題數: 29/30 | Accuracy: 0.4828 | refused: 5 | hallucination: 2
已完成題數: 30/30 | Accuracy: 0.5000 | refused: 5 | hallucination: 2
題數: 30
correct 數: 15
accuracy: 0.5000
refused 數: 5
hallucination 數: 2
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 15
accuracy: 0.5000
error 數: 16
retrieval_error: 0
synthesis_error: 7
numeric_error: 5
multi_question_error: 2
hallucination: 2
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 09:09:25

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:09:28,316 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 09:09:28,367 | INFO | 清理後有效頁數：272
2026-03-27 09:09:28,385 | INFO | 切片完成：共 685 個 chunks
2026-03-27 09:09:28,392 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:09:29,148 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 09:09:29,148 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:09:29,152 | INFO | 已載入 chunks：685 筆
2026-03-27 09:09:29,888 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:29,943 | INFO | Embedding 進度：1/22 batches
2026-03-27 09:09:30,281 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:30,323 | INFO | Embedding 進度：2/22 batches
2026-03-27 09:09:30,703 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:30,838 | INFO | Embedding 進度：3/22 batches
2026-03-27 09:09:31,253 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:31,346 | INFO | Embedding 進度：4/22 batches
2026-03-27 09:09:31,733 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:31,842 | INFO | Embedding 進度：5/22 batches
2026-03-27 09:09:32,222 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:32,265 | INFO | Embedding 進度：6/22 batches
2026-03-27 09:09:32,746 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:32,838 | INFO | Embedding 進度：7/22 batches
2026-03-27 09:09:33,240 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:33,270 | INFO | Embedding 進度：8/22 batches
2026-03-27 09:09:33,693 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:33,716 | INFO | Embedding 進度：9/22 batches
2026-03-27 09:09:34,059 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:34,092 | INFO | Embedding 進度：10/22 batches
2026-03-27 09:09:34,482 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:34,510 | INFO | Embedding 進度：11/22 batches
2026-03-27 09:09:34,895 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:34,911 | INFO | Embedding 進度：12/22 batches
2026-03-27 09:09:35,407 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:35,434 | INFO | Embedding 進度：13/22 batches
2026-03-27 09:09:35,930 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:35,940 | INFO | Embedding 進度：14/22 batches
2026-03-27 09:09:36,427 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:36,452 | INFO | Embedding 進度：15/22 batches
2026-03-27 09:09:36,836 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:36,940 | INFO | Embedding 進度：16/22 batches
2026-03-27 09:09:37,286 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:37,444 | INFO | Embedding 進度：17/22 batches
2026-03-27 09:09:37,846 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:37,974 | INFO | Embedding 進度：18/22 batches
2026-03-27 09:09:38,269 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:38,318 | INFO | Embedding 進度：19/22 batches
2026-03-27 09:09:38,785 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:38,796 | INFO | Embedding 進度：20/22 batches
2026-03-27 09:09:39,241 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:39,258 | INFO | Embedding 進度：21/22 batches
2026-03-27 09:09:39,607 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:39,610 | INFO | Embedding 進度：22/22 batches
2026-03-27 09:09:39,667 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 09:09:39,682 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 09:09:39,691 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:09:40,837 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.520561339855194,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.49994982481002803,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0155-c001",
      "page": 155,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.47830219149589537,
      "source": "113年報.pdf#page=155"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.45129698753356934,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0270-c001",
      "page": 270,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.45066873788833617,
      "source": "113年報.pdf#page=270"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 09:09:41,904 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 09:09:41,904 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 09:09:42,268 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:44,927 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:44,937 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 09:09:45,183 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:49,194 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:49,203 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 09:09:49,405 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:51,165 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:51,174 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 09:09:51,368 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:52,400 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:52,408 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 09:09:52,646 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:54,449 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:54,459 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 09:09:54,654 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:56,292 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:56,300 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 09:09:56,510 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:09:58,750 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:09:58,758 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 09:09:58,963 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:00,388 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:00,396 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 09:10:00,602 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:03,822 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:03,830 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 09:10:04,032 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:05,346 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:05,354 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 09:10:05,598 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:06,737 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:06,747 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 09:10:06,997 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:08,683 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:08,690 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 09:10:08,902 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:10,424 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:10,436 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 09:10:10,760 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:14,524 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:14,531 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 09:10:14,751 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:16,029 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:16,038 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 09:10:16,244 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:17,325 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:17,335 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 09:10:17,546 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:18,887 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:18,894 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 09:10:19,109 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:20,221 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:20,231 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 09:10:20,441 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:21,541 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:21,551 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 09:10:21,759 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:23,210 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:23,217 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 09:10:23,409 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:24,762 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:24,770 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 09:10:24,969 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:26,602 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:26,611 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 09:10:26,829 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:31,178 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:31,185 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 09:10:31,386 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:35,481 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:35,488 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 09:10:35,725 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:39,306 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:39,312 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 09:10:39,539 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:41,145 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:41,156 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 09:10:41,393 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:42,682 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 09:10:42,689 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 09:10:42,898 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:42,914 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 09:10:43,147 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:43,160 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 09:10:43,363 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 09:10:45,141 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 0
已完成題數: 5/30 | Accuracy: 0.6000 | refused: 1 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.4286 | refused: 1 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.4444 | refused: 1 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.4000 | refused: 1 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.4545 | refused: 1 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.4167 | refused: 1 | hallucination: 1
已完成題數: 13/30 | Accuracy: 0.4615 | refused: 1 | hallucination: 1
已完成題數: 14/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 1
已完成題數: 15/30 | Accuracy: 0.4667 | refused: 1 | hallucination: 1
已完成題數: 16/30 | Accuracy: 0.5000 | refused: 1 | hallucination: 1
已完成題數: 17/30 | Accuracy: 0.5294 | refused: 1 | hallucination: 1
已完成題數: 18/30 | Accuracy: 0.5556 | refused: 1 | hallucination: 1
已完成題數: 19/30 | Accuracy: 0.5789 | refused: 1 | hallucination: 1
已完成題數: 20/30 | Accuracy: 0.6000 | refused: 1 | hallucination: 1
已完成題數: 21/30 | Accuracy: 0.6190 | refused: 1 | hallucination: 1
已完成題數: 22/30 | Accuracy: 0.5909 | refused: 1 | hallucination: 1
已完成題數: 23/30 | Accuracy: 0.5652 | refused: 1 | hallucination: 1
已完成題數: 24/30 | Accuracy: 0.5833 | refused: 1 | hallucination: 1
已完成題數: 25/30 | Accuracy: 0.5600 | refused: 1 | hallucination: 1
已完成題數: 26/30 | Accuracy: 0.5769 | refused: 1 | hallucination: 2
已完成題數: 27/30 | Accuracy: 0.5926 | refused: 1 | hallucination: 2
已完成題數: 28/30 | Accuracy: 0.6071 | refused: 2 | hallucination: 2
已完成題數: 29/30 | Accuracy: 0.6207 | refused: 3 | hallucination: 2
已完成題數: 30/30 | Accuracy: 0.6000 | refused: 3 | hallucination: 2
題數: 30
correct 數: 18
accuracy: 0.6000
refused 數: 3
hallucination 數: 2
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 18
accuracy: 0.6000
error 數: 13
retrieval_error: 0
synthesis_error: 4
numeric_error: 5
multi_question_error: 2
hallucination: 2
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

## Run Record - 2026-03-27 11:29:35

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:29:38,959 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 11:29:39,011 | INFO | 清理後有效頁數：272
2026-03-27 11:29:39,028 | INFO | 切片完成：共 685 個 chunks
2026-03-27 11:29:39,035 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:29:39,770 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 11:29:39,770 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 11:29:39,774 | INFO | 已載入 chunks：685 筆
2026-03-27 11:29:42,387 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:42,518 | INFO | Embedding 進度：1/22 batches
2026-03-27 11:29:44,497 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:44,604 | INFO | Embedding 進度：2/22 batches
2026-03-27 11:29:44,979 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:45,102 | INFO | Embedding 進度：3/22 batches
2026-03-27 11:29:45,437 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:45,545 | INFO | Embedding 進度：4/22 batches
2026-03-27 11:29:45,930 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:46,033 | INFO | Embedding 進度：5/22 batches
2026-03-27 11:29:46,432 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:46,583 | INFO | Embedding 進度：6/22 batches
2026-03-27 11:29:47,016 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:47,059 | INFO | Embedding 進度：7/22 batches
2026-03-27 11:29:47,473 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:47,611 | INFO | Embedding 進度：8/22 batches
2026-03-27 11:29:48,009 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:48,104 | INFO | Embedding 進度：9/22 batches
2026-03-27 11:29:48,420 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:48,581 | INFO | Embedding 進度：10/22 batches
2026-03-27 11:29:48,950 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:49,036 | INFO | Embedding 進度：11/22 batches
2026-03-27 11:29:49,366 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:49,502 | INFO | Embedding 進度：12/22 batches
2026-03-27 11:29:49,916 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:50,066 | INFO | Embedding 進度：13/22 batches
2026-03-27 11:29:50,509 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:50,633 | INFO | Embedding 進度：14/22 batches
2026-03-27 11:29:51,049 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:51,187 | INFO | Embedding 進度：15/22 batches
2026-03-27 11:29:51,618 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:51,740 | INFO | Embedding 進度：16/22 batches
2026-03-27 11:29:52,112 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:52,253 | INFO | Embedding 進度：17/22 batches
2026-03-27 11:29:52,647 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:52,754 | INFO | Embedding 進度：18/22 batches
2026-03-27 11:29:53,045 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:53,200 | INFO | Embedding 進度：19/22 batches
2026-03-27 11:29:53,634 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:53,771 | INFO | Embedding 進度：20/22 batches
2026-03-27 11:29:54,084 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:54,222 | INFO | Embedding 進度：21/22 batches
2026-03-27 11:29:54,520 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:54,627 | INFO | Embedding 進度：22/22 batches
2026-03-27 11:29:54,706 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 11:29:54,732 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 11:29:54,743 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:29:55,801 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5221868515014648,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.4995294439792633,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4777773630619049,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.45179212391376494,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0269-c001",
      "page": 269,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.45134908914566035,
      "source": "113年報.pdf#page=269"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:29:56,814 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 11:29:56,815 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 11:29:57,175 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:29:59,709 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:29:59,727 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 11:29:59,974 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:05,220 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:05,246 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 11:30:05,498 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:07,571 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:07,582 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 11:30:07,823 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:10,081 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:10,087 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 11:30:10,332 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:12,379 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:12,388 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 11:30:12,607 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:15,281 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:15,291 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 11:30:15,475 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:34,874 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:34,887 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 11:30:35,174 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:36,747 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:36,757 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 11:30:36,971 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:40,742 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:40,752 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 11:30:40,980 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:43,065 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:43,076 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 11:30:43,281 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:44,858 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:44,868 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 11:30:45,152 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:48,175 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:48,189 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 11:30:48,429 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:50,542 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:50,552 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 11:30:50,811 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:55,016 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:55,023 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 11:30:55,290 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:30:58,226 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:30:58,239 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 11:30:58,488 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:00,098 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:00,112 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 11:31:00,404 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:02,314 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:02,323 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 11:31:02,530 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:03,841 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:03,850 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 11:31:04,099 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:05,224 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:05,241 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 11:31:05,508 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:06,739 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:06,748 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 11:31:06,984 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:09,280 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:09,289 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 11:31:09,529 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:11,017 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:11,026 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 11:31:11,251 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:15,884 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:15,894 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 11:31:16,155 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:27,128 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:27,137 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 11:31:27,378 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:30,865 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:30,872 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 11:31:31,097 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:36,411 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:36,417 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 11:31:36,636 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:37,874 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:31:37,886 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 11:31:38,100 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:38,115 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 11:31:38,321 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:38,337 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 11:31:38,526 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:31:39,905 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 1
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 2
已完成題數: 4/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 2
已完成題數: 5/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 2
已完成題數: 6/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 3
已完成題數: 7/30 | Accuracy: 0.7143 | refused: 0 | hallucination: 3
已完成題數: 8/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 3
已完成題數: 9/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 3
已完成題數: 10/30 | Accuracy: 0.7000 | refused: 0 | hallucination: 3
已完成題數: 11/30 | Accuracy: 0.7273 | refused: 0 | hallucination: 3
已完成題數: 12/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 4
已完成題數: 13/30 | Accuracy: 0.6154 | refused: 0 | hallucination: 4
已完成題數: 14/30 | Accuracy: 0.6429 | refused: 0 | hallucination: 4
已完成題數: 15/30 | Accuracy: 0.6000 | refused: 1 | hallucination: 4
已完成題數: 16/30 | Accuracy: 0.6250 | refused: 1 | hallucination: 4
已完成題數: 17/30 | Accuracy: 0.6471 | refused: 1 | hallucination: 4
已完成題數: 18/30 | Accuracy: 0.6667 | refused: 1 | hallucination: 4
已完成題數: 19/30 | Accuracy: 0.6842 | refused: 1 | hallucination: 4
已完成題數: 20/30 | Accuracy: 0.7000 | refused: 1 | hallucination: 4
已完成題數: 21/30 | Accuracy: 0.7143 | refused: 1 | hallucination: 4
已完成題數: 22/30 | Accuracy: 0.6818 | refused: 1 | hallucination: 4
已完成題數: 23/30 | Accuracy: 0.6522 | refused: 1 | hallucination: 5
已完成題數: 24/30 | Accuracy: 0.6667 | refused: 1 | hallucination: 5
已完成題數: 25/30 | Accuracy: 0.6800 | refused: 1 | hallucination: 5
已完成題數: 26/30 | Accuracy: 0.6923 | refused: 1 | hallucination: 6
已完成題數: 27/30 | Accuracy: 0.7037 | refused: 1 | hallucination: 6
已完成題數: 28/30 | Accuracy: 0.7143 | refused: 2 | hallucination: 6
已完成題數: 29/30 | Accuracy: 0.7241 | refused: 3 | hallucination: 6
已完成題數: 30/30 | Accuracy: 0.7333 | refused: 3 | hallucination: 6
題數: 30
correct 數: 22
accuracy: 0.7333
refused 數: 3
hallucination 數: 6
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 22
accuracy: 0.7333
error 數: 11
retrieval_error: 0
synthesis_error: 3
numeric_error: 1
multi_question_error: 1
hallucination: 6
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 12
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 11:32:42

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:32:46,192 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 11:32:46,243 | INFO | 清理後有效頁數：272
2026-03-27 11:32:46,261 | INFO | 切片完成：共 685 個 chunks
2026-03-27 11:32:46,266 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:32:46,861 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 11:32:46,861 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 11:32:46,864 | INFO | 已載入 chunks：685 筆
2026-03-27 11:32:47,611 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:47,751 | INFO | Embedding 進度：1/22 batches
2026-03-27 11:32:48,066 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:48,212 | INFO | Embedding 進度：2/22 batches
2026-03-27 11:32:48,545 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:48,571 | INFO | Embedding 進度：3/22 batches
2026-03-27 11:32:48,896 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:49,035 | INFO | Embedding 進度：4/22 batches
2026-03-27 11:32:49,444 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:49,568 | INFO | Embedding 進度：5/22 batches
2026-03-27 11:32:49,955 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:50,082 | INFO | Embedding 進度：6/22 batches
2026-03-27 11:32:50,524 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:50,663 | INFO | Embedding 進度：7/22 batches
2026-03-27 11:32:51,061 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:51,200 | INFO | Embedding 進度：8/22 batches
2026-03-27 11:32:51,608 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:51,720 | INFO | Embedding 進度：9/22 batches
2026-03-27 11:32:52,227 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:52,270 | INFO | Embedding 進度：10/22 batches
2026-03-27 11:32:52,604 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:52,719 | INFO | Embedding 進度：11/22 batches
2026-03-27 11:32:53,076 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:53,198 | INFO | Embedding 進度：12/22 batches
2026-03-27 11:32:53,658 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:53,744 | INFO | Embedding 進度：13/22 batches
2026-03-27 11:32:54,163 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:54,174 | INFO | Embedding 進度：14/22 batches
2026-03-27 11:32:54,666 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:54,688 | INFO | Embedding 進度：15/22 batches
2026-03-27 11:32:55,083 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:55,168 | INFO | Embedding 進度：16/22 batches
2026-03-27 11:32:55,546 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:55,571 | INFO | Embedding 進度：17/22 batches
2026-03-27 11:32:55,974 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:55,995 | INFO | Embedding 進度：18/22 batches
2026-03-27 11:32:56,295 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:56,319 | INFO | Embedding 進度：19/22 batches
2026-03-27 11:32:56,758 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:56,787 | INFO | Embedding 進度：20/22 batches
2026-03-27 11:32:57,238 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:57,263 | INFO | Embedding 進度：21/22 batches
2026-03-27 11:32:57,543 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:32:57,582 | INFO | Embedding 進度：22/22 batches
2026-03-27 11:32:57,652 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 11:32:57,667 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 11:32:57,679 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:32:58,736 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5218232154846192,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0007-c002",
      "page": 7,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.49795745134353636,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0155-c001",
      "page": 155,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.47826353073120115,
      "source": "113年報.pdf#page=155"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.45626470029354094,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0269-c001",
      "page": 269,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.4516989666223526,
      "source": "113年報.pdf#page=269"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 11:32:59,832 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 11:32:59,832 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 11:33:00,175 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:01,506 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:01,522 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 11:33:01,736 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:06,081 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:06,089 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 11:33:06,340 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:08,113 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:08,122 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 11:33:08,381 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:10,944 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:10,953 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 11:33:11,161 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:12,723 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:12,737 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 11:33:12,936 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:16,490 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:16,499 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 11:33:16,727 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:27,000 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:27,007 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 11:33:27,234 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:28,721 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:28,730 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 11:33:28,942 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:32,915 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:32,925 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 11:33:33,160 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:35,869 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:35,878 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 11:33:36,077 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:37,508 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:37,517 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 11:33:37,711 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:39,458 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:39,466 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 11:33:39,693 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:40,976 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:40,986 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 11:33:41,222 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:44,459 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:44,470 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 11:33:44,675 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:46,043 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:46,051 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 11:33:46,257 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:47,954 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:47,967 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 11:33:48,240 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:49,554 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:49,563 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 11:33:49,793 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:51,017 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:51,025 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 11:33:51,259 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:52,551 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:52,560 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 11:33:52,795 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:54,170 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:54,178 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 11:33:54,363 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:55,686 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:55,693 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 11:33:55,967 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:33:57,661 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:33:57,670 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 11:33:57,910 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:03,441 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:34:03,450 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 11:34:03,659 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:10,653 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:34:10,662 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 11:34:10,858 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:14,091 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:34:14,101 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 11:34:14,287 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:16,307 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:34:16,318 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 11:34:16,576 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:19,366 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 11:34:19,378 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 11:34:19,587 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:19,603 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 11:34:19,948 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:19,967 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 11:34:20,174 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 11:34:21,416 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 5/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 6/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 0
已完成題數: 7/30 | Accuracy: 0.8571 | refused: 0 | hallucination: 0
已完成題數: 8/30 | Accuracy: 0.8750 | refused: 0 | hallucination: 0
已完成題數: 9/30 | Accuracy: 0.7778 | refused: 0 | hallucination: 0
已完成題數: 10/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 0
已完成題數: 11/30 | Accuracy: 0.8182 | refused: 0 | hallucination: 0
已完成題數: 12/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 1
已完成題數: 13/30 | Accuracy: 0.7692 | refused: 0 | hallucination: 1
已完成題數: 14/30 | Accuracy: 0.7857 | refused: 0 | hallucination: 1
已完成題數: 15/30 | Accuracy: 0.7333 | refused: 1 | hallucination: 1
已完成題數: 16/30 | Accuracy: 0.7500 | refused: 1 | hallucination: 1
已完成題數: 17/30 | Accuracy: 0.7647 | refused: 1 | hallucination: 1
已完成題數: 18/30 | Accuracy: 0.7778 | refused: 1 | hallucination: 1
已完成題數: 19/30 | Accuracy: 0.7895 | refused: 1 | hallucination: 1
已完成題數: 20/30 | Accuracy: 0.8000 | refused: 1 | hallucination: 1
已完成題數: 21/30 | Accuracy: 0.8095 | refused: 1 | hallucination: 1
已完成題數: 22/30 | Accuracy: 0.7727 | refused: 1 | hallucination: 1
已完成題數: 23/30 | Accuracy: 0.7391 | refused: 1 | hallucination: 1
已完成題數: 24/30 | Accuracy: 0.7500 | refused: 1 | hallucination: 1
已完成題數: 25/30 | Accuracy: 0.7200 | refused: 1 | hallucination: 1
已完成題數: 26/30 | Accuracy: 0.7308 | refused: 1 | hallucination: 2
已完成題數: 27/30 | Accuracy: 0.7407 | refused: 1 | hallucination: 2
已完成題數: 28/30 | Accuracy: 0.7500 | refused: 2 | hallucination: 2
已完成題數: 29/30 | Accuracy: 0.7586 | refused: 3 | hallucination: 2
已完成題數: 30/30 | Accuracy: 0.7667 | refused: 3 | hallucination: 2
題數: 30
correct 數: 23
accuracy: 0.7667
refused 數: 3
hallucination 數: 2
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 23
accuracy: 0.7667
error 數: 9
retrieval_error: 0
synthesis_error: 3
numeric_error: 3
multi_question_error: 1
hallucination: 2
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 13
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 12:04:38

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:04:41,763 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 12:04:41,815 | INFO | 清理後有效頁數：272
2026-03-27 12:04:41,833 | INFO | 切片完成：共 685 個 chunks
2026-03-27 12:04:41,839 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:04:42,485 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 12:04:42,485 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:04:42,489 | INFO | 已載入 chunks：685 筆
2026-03-27 12:04:43,979 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:44,090 | INFO | Embedding 進度：1/22 batches
2026-03-27 12:04:44,976 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:45,110 | INFO | Embedding 進度：2/22 batches
2026-03-27 12:04:45,465 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:45,598 | INFO | Embedding 進度：3/22 batches
2026-03-27 12:04:45,960 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:46,093 | INFO | Embedding 進度：4/22 batches
2026-03-27 12:04:46,475 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:46,588 | INFO | Embedding 進度：5/22 batches
2026-03-27 12:04:46,959 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:47,033 | INFO | Embedding 進度：6/22 batches
2026-03-27 12:04:47,474 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:47,526 | INFO | Embedding 進度：7/22 batches
2026-03-27 12:04:47,912 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:47,934 | INFO | Embedding 進度：8/22 batches
2026-03-27 12:04:48,336 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:48,356 | INFO | Embedding 進度：9/22 batches
2026-03-27 12:04:48,742 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:48,770 | INFO | Embedding 進度：10/22 batches
2026-03-27 12:04:49,111 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:49,133 | INFO | Embedding 進度：11/22 batches
2026-03-27 12:04:49,458 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:49,520 | INFO | Embedding 進度：12/22 batches
2026-03-27 12:04:49,927 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:49,946 | INFO | Embedding 進度：13/22 batches
2026-03-27 12:04:50,356 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:50,451 | INFO | Embedding 進度：14/22 batches
2026-03-27 12:04:50,910 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:51,041 | INFO | Embedding 進度：15/22 batches
2026-03-27 12:04:51,438 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:51,567 | INFO | Embedding 進度：16/22 batches
2026-03-27 12:04:51,914 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:52,065 | INFO | Embedding 進度：17/22 batches
2026-03-27 12:04:52,520 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:52,652 | INFO | Embedding 進度：18/22 batches
2026-03-27 12:04:52,959 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:53,090 | INFO | Embedding 進度：19/22 batches
2026-03-27 12:04:53,517 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:53,652 | INFO | Embedding 進度：20/22 batches
2026-03-27 12:04:54,151 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:54,276 | INFO | Embedding 進度：21/22 batches
2026-03-27 12:04:54,583 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:04:54,659 | INFO | Embedding 進度：22/22 batches
2026-03-27 12:04:54,731 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 12:04:54,747 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:04:54,759 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:04:55,875 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5197538137435913,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.5005240178108215,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4810630393028259,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4532491850852966,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0154-c002",
      "page": 154,
      "text": "交換或 認股)普通股、海 外存託憑證或其 他有價證券之金 額 無 無 發行及轉換 (交換 或認股)辦法 無 無 發行及轉換 、 交換或認股辦法 、 發行條件對股權可能稀釋情形 及對現有股東權益影響 無 無 交換標的委託保管機構名稱 無 無 - 148 - 3.3 特特別別股股發發行行情情形形 1. 富邦金控甲種特別股 發行(辦理)日期 項 目 2016 年 4 月 22 日 (富邦金控甲種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 600,000 千股 總額 新台幣 36,000,000,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：甲種特別股年率 4.10%(七年期 IRS 0.885%+3.215%)，按每股發行價 格計算。 七年期 IRS 利率將於發行日起滿七年之次日及其後每七年重設。 甲種特別股自 2023 年 4 月 22 日起重設年率為 4.58125%。 2. 股息發放：本公司對於甲種特別股之股息分派具自主裁量權，包括但不限 於因年度決算無盈餘或盈餘不足分派特別股股息，或因特別股股息之分派 將使本公司資本適足率低於法令或主管機關所定最低要求。 本公司決議取 消特別股之股息分派，將不構成違約事件。 其未分派或分派不足額之股 息，不累積於以後有盈餘年度遞延償付。 本公司決算如有盈餘，應先完納 稅捐、彌補虧損，依法令規定提列法定盈餘公積並依法令規定或實際需要 提列特別盈餘公積，並得分派本公司甲種特別股股息。 甲種特別股股息每 年以現金一次發放，於每年股東常會承認財務報告後，由董事會訂定基準 日支付前一年度得發放之股息。 發行年度及收回年度股息之發放，按當年 度實際發行天數計算，所分配股息將認列於股利憑單。 3. 超額股利分配：甲種特別股除依前述所定之股息率領取股息外，不得參加",
      "score": 0.45179718255996704,
      "source": "113年報.pdf#page=154"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:04:56,863 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 12:04:56,864 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 12:04:57,260 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:01,445 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:01,464 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 12:05:01,684 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:05,910 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:05,923 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 12:05:06,150 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:08,269 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:08,278 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 12:05:08,492 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:09,978 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:09,987 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 12:05:10,215 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:12,149 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:12,166 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 12:05:12,392 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:14,992 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:15,002 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 12:05:15,220 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:18,236 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:18,250 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 12:05:18,449 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:19,973 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:19,982 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 12:05:20,171 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:24,926 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:24,930 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 12:05:25,184 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:26,996 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:27,008 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 12:05:27,230 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:28,641 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:28,651 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 12:05:28,881 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:31,108 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:31,117 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 12:05:31,324 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:33,354 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:33,364 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 12:05:33,600 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:37,438 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:37,449 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 12:05:37,678 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:39,194 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:39,205 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 12:05:39,400 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:41,031 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:41,049 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 12:05:41,285 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:44,409 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:44,418 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 12:05:44,768 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:46,126 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:46,136 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 12:05:46,377 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:47,576 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:47,587 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 12:05:47,827 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:49,874 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:49,886 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 12:05:50,127 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:52,627 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:52,637 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 12:05:52,893 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:05:54,293 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:05:54,302 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 12:05:54,551 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:01,418 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:06:01,430 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 12:06:01,659 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:09,086 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:06:09,098 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 12:06:09,339 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:14,492 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:06:14,505 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 12:06:14,762 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:16,796 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:06:16,803 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 12:06:17,044 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:18,708 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:06:18,721 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 12:06:18,949 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:18,970 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 12:06:19,235 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:19,258 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 12:06:19,490 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:06:21,252 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 1
已完成題數: 5/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 1
已完成題數: 6/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 1
已完成題數: 7/30 | Accuracy: 0.7143 | refused: 0 | hallucination: 1
已完成題數: 8/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 1
已完成題數: 9/30 | Accuracy: 0.7778 | refused: 0 | hallucination: 1
已完成題數: 10/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 1
已完成題數: 11/30 | Accuracy: 0.8182 | refused: 0 | hallucination: 1
已完成題數: 12/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 2
已完成題數: 13/30 | Accuracy: 0.8462 | refused: 0 | hallucination: 2
已完成題數: 14/30 | Accuracy: 0.8571 | refused: 0 | hallucination: 2
已完成題數: 15/30 | Accuracy: 0.8000 | refused: 1 | hallucination: 2
已完成題數: 16/30 | Accuracy: 0.8125 | refused: 1 | hallucination: 2
已完成題數: 17/30 | Accuracy: 0.8235 | refused: 1 | hallucination: 2
已完成題數: 18/30 | Accuracy: 0.8333 | refused: 1 | hallucination: 2
已完成題數: 19/30 | Accuracy: 0.8421 | refused: 1 | hallucination: 2
已完成題數: 20/30 | Accuracy: 0.8500 | refused: 1 | hallucination: 2
已完成題數: 21/30 | Accuracy: 0.8571 | refused: 1 | hallucination: 2
已完成題數: 22/30 | Accuracy: 0.8182 | refused: 1 | hallucination: 2
已完成題數: 23/30 | Accuracy: 0.7826 | refused: 1 | hallucination: 2
已完成題數: 24/30 | Accuracy: 0.7500 | refused: 1 | hallucination: 2
已完成題數: 25/30 | Accuracy: 0.7600 | refused: 1 | hallucination: 2
已完成題數: 26/30 | Accuracy: 0.7692 | refused: 1 | hallucination: 3
已完成題數: 27/30 | Accuracy: 0.7778 | refused: 1 | hallucination: 3
已完成題數: 28/30 | Accuracy: 0.7857 | refused: 2 | hallucination: 3
已完成題數: 29/30 | Accuracy: 0.7931 | refused: 3 | hallucination: 3
已完成題數: 30/30 | Accuracy: 0.8000 | refused: 3 | hallucination: 3
題數: 30
correct 數: 24
accuracy: 0.8000
refused 數: 3
hallucination 數: 3
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 24
accuracy: 0.8000
error 數: 9
retrieval_error: 0
synthesis_error: 2
numeric_error: 3
multi_question_error: 1
hallucination: 3
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 14
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 12:10:08

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:10:11,507 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 12:10:11,558 | INFO | 清理後有效頁數：272
2026-03-27 12:10:11,576 | INFO | 切片完成：共 685 個 chunks
2026-03-27 12:10:11,581 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:10:12,217 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 12:10:12,217 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:10:12,220 | INFO | 已載入 chunks：685 筆
2026-03-27 12:10:13,113 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:13,158 | INFO | Embedding 進度：1/22 batches
2026-03-27 12:10:13,717 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:13,871 | INFO | Embedding 進度：2/22 batches
2026-03-27 12:10:14,222 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:14,319 | INFO | Embedding 進度：3/22 batches
2026-03-27 12:10:14,652 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:14,795 | INFO | Embedding 進度：4/22 batches
2026-03-27 12:10:15,270 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:15,295 | INFO | Embedding 進度：5/22 batches
2026-03-27 12:10:15,745 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:15,772 | INFO | Embedding 進度：6/22 batches
2026-03-27 12:10:16,217 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:16,360 | INFO | Embedding 進度：7/22 batches
2026-03-27 12:10:16,755 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:16,789 | INFO | Embedding 進度：8/22 batches
2026-03-27 12:10:17,206 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:17,349 | INFO | Embedding 進度：9/22 batches
2026-03-27 12:10:17,675 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:17,781 | INFO | Embedding 進度：10/22 batches
2026-03-27 12:10:18,077 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:18,100 | INFO | Embedding 進度：11/22 batches
2026-03-27 12:10:18,431 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:18,554 | INFO | Embedding 進度：12/22 batches
2026-03-27 12:10:18,978 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:19,115 | INFO | Embedding 進度：13/22 batches
2026-03-27 12:10:19,548 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:19,674 | INFO | Embedding 進度：14/22 batches
2026-03-27 12:10:20,076 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:20,149 | INFO | Embedding 進度：15/22 batches
2026-03-27 12:10:20,465 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:20,479 | INFO | Embedding 進度：16/22 batches
2026-03-27 12:10:20,848 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:20,915 | INFO | Embedding 進度：17/22 batches
2026-03-27 12:10:21,303 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:21,328 | INFO | Embedding 進度：18/22 batches
2026-03-27 12:10:21,615 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:21,688 | INFO | Embedding 進度：19/22 batches
2026-03-27 12:10:22,126 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:22,190 | INFO | Embedding 進度：20/22 batches
2026-03-27 12:10:22,619 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:22,769 | INFO | Embedding 進度：21/22 batches
2026-03-27 12:10:23,159 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:23,198 | INFO | Embedding 進度：22/22 batches
2026-03-27 12:10:23,270 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 12:10:23,301 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:10:23,314 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:10:24,346 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5207681822776794,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0007-c002",
      "page": 7,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.4999330604076385,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0155-c001",
      "page": 155,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4774671971797943,
      "source": "113年報.pdf#page=155"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4520264589786529,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0269-c001",
      "page": 269,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.45138051629066467,
      "source": "113年報.pdf#page=269"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:10:25,335 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 12:10:25,335 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 12:10:25,653 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:27,030 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:27,045 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 12:10:27,311 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:31,261 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:31,272 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 12:10:31,561 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:33,867 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:33,878 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 12:10:34,129 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:35,494 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:35,501 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 12:10:35,718 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:37,855 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:37,869 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 12:10:38,083 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:40,951 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:40,961 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 12:10:41,178 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:49,297 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:49,308 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 12:10:49,612 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:51,081 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:51,093 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 12:10:51,303 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:56,968 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:56,979 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 12:10:57,197 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:10:58,661 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:10:58,671 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 12:10:58,907 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:00,135 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:00,144 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 12:11:00,372 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:07,379 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:07,388 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 12:11:07,617 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:08,773 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:08,786 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 12:11:09,011 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:11,172 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:11,180 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 12:11:11,394 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:12,517 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:12,525 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 12:11:12,763 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:14,114 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:14,127 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 12:11:14,633 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:16,171 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:16,179 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 12:11:16,466 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:18,215 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:18,221 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 12:11:19,008 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:20,162 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:20,171 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 12:11:20,399 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:21,765 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:21,778 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 12:11:22,249 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:24,393 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:24,403 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 12:11:24,621 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:26,143 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:26,151 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 12:11:26,352 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:32,686 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:32,697 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 12:11:32,919 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:37,597 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:37,606 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 12:11:37,868 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:42,112 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:42,122 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 12:11:42,344 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:45,461 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:45,472 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 12:11:45,702 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:46,890 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:11:46,903 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 12:11:47,129 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:47,150 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 12:11:47,354 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:47,373 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 12:11:47,628 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:11:49,091 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 1
已完成題數: 5/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 1
已完成題數: 6/30 | Accuracy: 0.6667 | refused: 1 | hallucination: 1
已完成題數: 7/30 | Accuracy: 0.5714 | refused: 1 | hallucination: 1
已完成題數: 8/30 | Accuracy: 0.6250 | refused: 1 | hallucination: 1
已完成題數: 9/30 | Accuracy: 0.6667 | refused: 1 | hallucination: 1
已完成題數: 10/30 | Accuracy: 0.7000 | refused: 1 | hallucination: 1
已完成題數: 11/30 | Accuracy: 0.7273 | refused: 1 | hallucination: 1
已完成題數: 12/30 | Accuracy: 0.6667 | refused: 1 | hallucination: 2
已完成題數: 13/30 | Accuracy: 0.6923 | refused: 1 | hallucination: 2
已完成題數: 14/30 | Accuracy: 0.7143 | refused: 1 | hallucination: 2
已完成題數: 15/30 | Accuracy: 0.6667 | refused: 2 | hallucination: 2
已完成題數: 16/30 | Accuracy: 0.6875 | refused: 2 | hallucination: 2
已完成題數: 17/30 | Accuracy: 0.7059 | refused: 2 | hallucination: 2
已完成題數: 18/30 | Accuracy: 0.7222 | refused: 2 | hallucination: 2
已完成題數: 19/30 | Accuracy: 0.7368 | refused: 2 | hallucination: 2
已完成題數: 20/30 | Accuracy: 0.7500 | refused: 2 | hallucination: 2
已完成題數: 21/30 | Accuracy: 0.7619 | refused: 2 | hallucination: 2
已完成題數: 22/30 | Accuracy: 0.7273 | refused: 2 | hallucination: 2
已完成題數: 23/30 | Accuracy: 0.6957 | refused: 2 | hallucination: 2
已完成題數: 24/30 | Accuracy: 0.7083 | refused: 2 | hallucination: 2
已完成題數: 25/30 | Accuracy: 0.7200 | refused: 2 | hallucination: 2
已完成題數: 26/30 | Accuracy: 0.7308 | refused: 2 | hallucination: 3
已完成題數: 27/30 | Accuracy: 0.7407 | refused: 2 | hallucination: 3
已完成題數: 28/30 | Accuracy: 0.7500 | refused: 3 | hallucination: 3
已完成題數: 29/30 | Accuracy: 0.7586 | refused: 4 | hallucination: 3
已完成題數: 30/30 | Accuracy: 0.7667 | refused: 4 | hallucination: 3
題數: 30
correct 數: 23
accuracy: 0.7667
refused 數: 4
hallucination 數: 3
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 23
accuracy: 0.7667
error 數: 9
retrieval_error: 0
synthesis_error: 2
numeric_error: 3
multi_question_error: 1
hallucination: 3
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 15
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 12:12:29

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:12:32,663 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 12:12:32,714 | INFO | 清理後有效頁數：272
2026-03-27 12:12:32,732 | INFO | 切片完成：共 685 個 chunks
2026-03-27 12:12:32,739 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:12:33,369 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 12:12:33,370 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:12:33,373 | INFO | 已載入 chunks：685 筆
2026-03-27 12:12:34,137 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:34,277 | INFO | Embedding 進度：1/22 batches
2026-03-27 12:12:34,636 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:34,711 | INFO | Embedding 進度：2/22 batches
2026-03-27 12:12:35,039 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:35,060 | INFO | Embedding 進度：3/22 batches
2026-03-27 12:12:35,395 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:35,432 | INFO | Embedding 進度：4/22 batches
2026-03-27 12:12:35,972 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:36,028 | INFO | Embedding 進度：5/22 batches
2026-03-27 12:12:36,314 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:36,337 | INFO | Embedding 進度：6/22 batches
2026-03-27 12:12:36,815 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:36,878 | INFO | Embedding 進度：7/22 batches
2026-03-27 12:12:37,263 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:37,350 | INFO | Embedding 進度：8/22 batches
2026-03-27 12:12:37,772 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:37,818 | INFO | Embedding 進度：9/22 batches
2026-03-27 12:12:38,169 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:38,303 | INFO | Embedding 進度：10/22 batches
2026-03-27 12:12:38,597 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:38,635 | INFO | Embedding 進度：11/22 batches
2026-03-27 12:12:38,962 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:39,103 | INFO | Embedding 進度：12/22 batches
2026-03-27 12:12:39,510 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:39,636 | INFO | Embedding 進度：13/22 batches
2026-03-27 12:12:40,061 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:40,125 | INFO | Embedding 進度：14/22 batches
2026-03-27 12:12:40,515 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:40,617 | INFO | Embedding 進度：15/22 batches
2026-03-27 12:12:41,063 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:41,201 | INFO | Embedding 進度：16/22 batches
2026-03-27 12:12:41,563 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:41,695 | INFO | Embedding 進度：17/22 batches
2026-03-27 12:12:42,339 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:42,472 | INFO | Embedding 進度：18/22 batches
2026-03-27 12:12:43,011 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:43,140 | INFO | Embedding 進度：19/22 batches
2026-03-27 12:12:43,551 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:43,573 | INFO | Embedding 進度：20/22 batches
2026-03-27 12:12:44,016 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:44,134 | INFO | Embedding 進度：21/22 batches
2026-03-27 12:12:44,397 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:44,430 | INFO | Embedding 進度：22/22 batches
2026-03-27 12:12:44,504 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 12:12:44,521 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 12:12:44,533 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:12:45,601 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5218633913993835,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.49983120322227476,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4815068316459655,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.452912186384201,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0154-c002",
      "page": 154,
      "text": "交換或 認股)普通股、海 外存託憑證或其 他有價證券之金 額 無 無 發行及轉換 (交換 或認股)辦法 無 無 發行及轉換 、 交換或認股辦法 、 發行條件對股權可能稀釋情形 及對現有股東權益影響 無 無 交換標的委託保管機構名稱 無 無 - 148 - 3.3 特特別別股股發發行行情情形形 1. 富邦金控甲種特別股 發行(辦理)日期 項 目 2016 年 4 月 22 日 (富邦金控甲種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 600,000 千股 總額 新台幣 36,000,000,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：甲種特別股年率 4.10%(七年期 IRS 0.885%+3.215%)，按每股發行價 格計算。 七年期 IRS 利率將於發行日起滿七年之次日及其後每七年重設。 甲種特別股自 2023 年 4 月 22 日起重設年率為 4.58125%。 2. 股息發放：本公司對於甲種特別股之股息分派具自主裁量權，包括但不限 於因年度決算無盈餘或盈餘不足分派特別股股息，或因特別股股息之分派 將使本公司資本適足率低於法令或主管機關所定最低要求。 本公司決議取 消特別股之股息分派，將不構成違約事件。 其未分派或分派不足額之股 息，不累積於以後有盈餘年度遞延償付。 本公司決算如有盈餘，應先完納 稅捐、彌補虧損，依法令規定提列法定盈餘公積並依法令規定或實際需要 提列特別盈餘公積，並得分派本公司甲種特別股股息。 甲種特別股股息每 年以現金一次發放，於每年股東常會承認財務報告後，由董事會訂定基準 日支付前一年度得發放之股息。 發行年度及收回年度股息之發放，按當年 度實際發行天數計算，所分配股息將認列於股利憑單。 3. 超額股利分配：甲種特別股除依前述所定之股息率領取股息外，不得參加",
      "score": 0.45202127814292903,
      "source": "113年報.pdf#page=154"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 12:12:46,665 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 12:12:46,665 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 12:12:47,069 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:49,481 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:12:49,495 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 12:12:49,732 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:55,063 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:12:55,074 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 12:12:55,315 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:56,830 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:12:56,842 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 12:12:57,066 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:12:58,547 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:12:58,557 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 12:12:58,768 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:00,229 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:00,248 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 12:13:00,437 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:02,289 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:02,302 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 12:13:02,505 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:10,199 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:10,210 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 12:13:10,430 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:12,184 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:12,193 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 12:13:12,433 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:22,477 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:22,487 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 12:13:22,681 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:24,294 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:24,302 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 12:13:24,513 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:26,121 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:26,132 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 12:13:26,352 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:29,796 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:29,805 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 12:13:30,016 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:31,576 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:31,584 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 12:13:31,798 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:34,486 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:34,496 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 12:13:34,689 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:36,471 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:36,477 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 12:13:36,677 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:38,064 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:38,075 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 12:13:38,292 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:39,670 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:39,682 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 12:13:39,967 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:41,532 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:41,541 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 12:13:41,773 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:43,813 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:43,822 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 12:13:44,038 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:45,363 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:45,370 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 12:13:45,672 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:47,044 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:47,067 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 12:13:47,265 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:50,334 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:50,338 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 12:13:50,549 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:13:56,897 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:13:56,907 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 12:13:57,119 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:04,639 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:14:04,647 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 12:14:04,896 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:09,154 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:14:09,165 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 12:14:09,364 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:11,856 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:14:11,866 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 12:14:12,099 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:13,880 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 12:14:13,892 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 12:14:14,113 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:14,133 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 12:14:14,346 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:14,366 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 12:14:14,603 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 12:14:17,413 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 0.5000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 0.6667 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 0.7500 | refused: 0 | hallucination: 1
已完成題數: 5/30 | Accuracy: 0.8000 | refused: 0 | hallucination: 1
已完成題數: 6/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 1
已完成題數: 7/30 | Accuracy: 0.8571 | refused: 0 | hallucination: 1
已完成題數: 8/30 | Accuracy: 0.8750 | refused: 0 | hallucination: 1
已完成題數: 9/30 | Accuracy: 0.8889 | refused: 0 | hallucination: 1
已完成題數: 10/30 | Accuracy: 0.9000 | refused: 0 | hallucination: 1
已完成題數: 11/30 | Accuracy: 0.9091 | refused: 0 | hallucination: 1
已完成題數: 12/30 | Accuracy: 0.8333 | refused: 0 | hallucination: 2
已完成題數: 13/30 | Accuracy: 0.8462 | refused: 0 | hallucination: 2
已完成題數: 14/30 | Accuracy: 0.8571 | refused: 0 | hallucination: 2
已完成題數: 15/30 | Accuracy: 0.8000 | refused: 1 | hallucination: 2
已完成題數: 16/30 | Accuracy: 0.8125 | refused: 1 | hallucination: 2
已完成題數: 17/30 | Accuracy: 0.8235 | refused: 1 | hallucination: 2
已完成題數: 18/30 | Accuracy: 0.8333 | refused: 1 | hallucination: 2
已完成題數: 19/30 | Accuracy: 0.8421 | refused: 1 | hallucination: 2
已完成題數: 20/30 | Accuracy: 0.8500 | refused: 1 | hallucination: 2
已完成題數: 21/30 | Accuracy: 0.8571 | refused: 1 | hallucination: 2
已完成題數: 22/30 | Accuracy: 0.8182 | refused: 1 | hallucination: 2
已完成題數: 23/30 | Accuracy: 0.7826 | refused: 1 | hallucination: 2
已完成題數: 24/30 | Accuracy: 0.7500 | refused: 1 | hallucination: 2
已完成題數: 25/30 | Accuracy: 0.7200 | refused: 1 | hallucination: 2
已完成題數: 26/30 | Accuracy: 0.7308 | refused: 1 | hallucination: 3
已完成題數: 27/30 | Accuracy: 0.7407 | refused: 1 | hallucination: 3
已完成題數: 28/30 | Accuracy: 0.7500 | refused: 2 | hallucination: 3
已完成題數: 29/30 | Accuracy: 0.7586 | refused: 3 | hallucination: 3
已完成題數: 30/30 | Accuracy: 0.7667 | refused: 3 | hallucination: 3
題數: 30
correct 數: 23
accuracy: 0.7667
refused 數: 3
hallucination 數: 3
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 23
accuracy: 0.7667
error 數: 9
retrieval_error: 0
synthesis_error: 1
numeric_error: 3
multi_question_error: 2
hallucination: 3
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 16
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 15:04:17

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:04:20,490 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 15:04:20,542 | INFO | 清理後有效頁數：272
2026-03-27 15:04:20,560 | INFO | 切片完成：共 685 個 chunks
2026-03-27 15:04:20,567 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:04:21,201 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 15:04:21,202 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:04:21,205 | INFO | 已載入 chunks：685 筆
2026-03-27 15:04:22,814 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:22,844 | INFO | Embedding 進度：1/22 batches
2026-03-27 15:04:23,193 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:23,207 | INFO | Embedding 進度：2/22 batches
2026-03-27 15:04:23,517 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:23,556 | INFO | Embedding 進度：3/22 batches
2026-03-27 15:04:23,890 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:23,959 | INFO | Embedding 進度：4/22 batches
2026-03-27 15:04:24,352 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:24,387 | INFO | Embedding 進度：5/22 batches
2026-03-27 15:04:24,753 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:24,775 | INFO | Embedding 進度：6/22 batches
2026-03-27 15:04:25,937 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:25,968 | INFO | Embedding 進度：7/22 batches
2026-03-27 15:04:26,456 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:26,480 | INFO | Embedding 進度：8/22 batches
2026-03-27 15:04:26,919 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:26,993 | INFO | Embedding 進度：9/22 batches
2026-03-27 15:04:27,319 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:27,383 | INFO | Embedding 進度：10/22 batches
2026-03-27 15:04:27,684 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:27,700 | INFO | Embedding 進度：11/22 batches
2026-03-27 15:04:28,009 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:28,077 | INFO | Embedding 進度：12/22 batches
2026-03-27 15:04:28,498 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:28,569 | INFO | Embedding 進度：13/22 batches
2026-03-27 15:04:28,979 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:28,990 | INFO | Embedding 進度：14/22 batches
2026-03-27 15:04:29,367 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:29,385 | INFO | Embedding 進度：15/22 batches
2026-03-27 15:04:29,924 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:30,017 | INFO | Embedding 進度：16/22 batches
2026-03-27 15:04:30,395 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:30,527 | INFO | Embedding 進度：17/22 batches
2026-03-27 15:04:30,908 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:30,955 | INFO | Embedding 進度：18/22 batches
2026-03-27 15:04:31,263 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:31,366 | INFO | Embedding 進度：19/22 batches
2026-03-27 15:04:31,770 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:31,846 | INFO | Embedding 進度：20/22 batches
2026-03-27 15:04:32,328 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:32,362 | INFO | Embedding 進度：21/22 batches
2026-03-27 15:04:32,634 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:32,641 | INFO | Embedding 進度：22/22 batches
2026-03-27 15:04:32,717 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 15:04:32,734 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:04:32,746 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:04:33,789 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.521725708246231,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.49998232722282404,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4808713972568512,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.45349556803703306,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0154-c002",
      "page": 154,
      "text": "交換或 認股)普通股、海 外存託憑證或其 他有價證券之金 額 無 無 發行及轉換 (交換 或認股)辦法 無 無 發行及轉換 、 交換或認股辦法 、 發行條件對股權可能稀釋情形 及對現有股東權益影響 無 無 交換標的委託保管機構名稱 無 無 - 148 - 3.3 特特別別股股發發行行情情形形 1. 富邦金控甲種特別股 發行(辦理)日期 項 目 2016 年 4 月 22 日 (富邦金控甲種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 600,000 千股 總額 新台幣 36,000,000,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：甲種特別股年率 4.10%(七年期 IRS 0.885%+3.215%)，按每股發行價 格計算。 七年期 IRS 利率將於發行日起滿七年之次日及其後每七年重設。 甲種特別股自 2023 年 4 月 22 日起重設年率為 4.58125%。 2. 股息發放：本公司對於甲種特別股之股息分派具自主裁量權，包括但不限 於因年度決算無盈餘或盈餘不足分派特別股股息，或因特別股股息之分派 將使本公司資本適足率低於法令或主管機關所定最低要求。 本公司決議取 消特別股之股息分派，將不構成違約事件。 其未分派或分派不足額之股 息，不累積於以後有盈餘年度遞延償付。 本公司決算如有盈餘，應先完納 稅捐、彌補虧損，依法令規定提列法定盈餘公積並依法令規定或實際需要 提列特別盈餘公積，並得分派本公司甲種特別股股息。 甲種特別股股息每 年以現金一次發放，於每年股東常會承認財務報告後，由董事會訂定基準 日支付前一年度得發放之股息。 發行年度及收回年度股息之發放，按當年 度實際發行天數計算，所分配股息將認列於股利憑單。 3. 超額股利分配：甲種特別股除依前述所定之股息率領取股息外，不得參加",
      "score": 0.45221211373806,
      "source": "113年報.pdf#page=154"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:04:34,826 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 15:04:34,826 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 15:04:35,163 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:37,569 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:37,587 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 15:04:37,819 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:37,900 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 15:04:38,127 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:40,303 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:40,312 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 15:04:40,534 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:42,907 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:42,922 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 15:04:43,133 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:44,515 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:44,526 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 15:04:44,746 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:46,542 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:46,548 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 15:04:46,744 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:53,624 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:53,631 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 15:04:53,820 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:55,345 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:55,352 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 15:04:55,577 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:04:59,399 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:04:59,413 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 15:04:59,626 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:01,520 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:01,529 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 15:05:01,730 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:03,169 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:03,178 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 15:05:03,424 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:03,470 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 15:05:03,715 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:05,097 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:05,106 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 15:05:05,587 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:07,580 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:07,588 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 15:05:07,807 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:07,889 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 15:05:08,062 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:09,534 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:09,546 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 15:05:09,777 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:11,227 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:11,237 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 15:05:11,461 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:12,762 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:12,771 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 15:05:13,007 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:15,102 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:15,108 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 15:05:15,338 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:16,446 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:16,457 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 15:05:16,649 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:18,891 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:18,899 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 15:05:19,098 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:19,123 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 15:05:19,877 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:27,104 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:27,115 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 15:05:27,324 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:27,378 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 15:05:27,577 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:27,672 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 15:05:27,863 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:29,890 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:29,900 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 15:05:30,097 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:31,535 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:05:31,545 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 15:05:31,730 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:31,750 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 15:05:31,983 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:32,064 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 15:05:32,344 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:05:33,568 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 5/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 6/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 7/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 8/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 9/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 10/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 11/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 12/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 13/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 14/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 15/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 16/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 17/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 18/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 19/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 20/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 21/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 22/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 23/30 | Accuracy: 0.9565 | refused: 0 | hallucination: 2
已完成題數: 24/30 | Accuracy: 0.9583 | refused: 0 | hallucination: 2
已完成題數: 25/30 | Accuracy: 0.9600 | refused: 0 | hallucination: 2
已完成題數: 26/30 | Accuracy: 0.9615 | refused: 0 | hallucination: 3
已完成題數: 27/30 | Accuracy: 0.9630 | refused: 0 | hallucination: 3
已完成題數: 28/30 | Accuracy: 0.9643 | refused: 1 | hallucination: 3
已完成題數: 29/30 | Accuracy: 0.9655 | refused: 2 | hallucination: 3
已完成題數: 30/30 | Accuracy: 0.9667 | refused: 2 | hallucination: 3
題數: 30
correct 數: 29
accuracy: 0.9667
refused 數: 2
hallucination 數: 3
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 29
accuracy: 0.9667
error 數: 4
retrieval_error: 0
synthesis_error: 0
numeric_error: 1
multi_question_error: 0
hallucination: 3
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 17
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 15:12:32

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:12:36,088 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 15:12:36,142 | INFO | 清理後有效頁數：272
2026-03-27 15:12:36,160 | INFO | 切片完成：共 685 個 chunks
2026-03-27 15:12:36,167 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:12:36,819 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 15:12:36,819 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:12:36,823 | INFO | 已載入 chunks：685 筆
2026-03-27 15:12:37,617 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:37,676 | INFO | Embedding 進度：1/22 batches
2026-03-27 15:12:38,051 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:38,156 | INFO | Embedding 進度：2/22 batches
2026-03-27 15:12:38,458 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:38,594 | INFO | Embedding 進度：3/22 batches
2026-03-27 15:12:38,923 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:39,060 | INFO | Embedding 進度：4/22 batches
2026-03-27 15:12:39,378 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:39,502 | INFO | Embedding 進度：5/22 batches
2026-03-27 15:12:39,861 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:40,004 | INFO | Embedding 進度：6/22 batches
2026-03-27 15:12:40,582 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:40,606 | INFO | Embedding 進度：7/22 batches
2026-03-27 15:12:41,008 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:41,026 | INFO | Embedding 進度：8/22 batches
2026-03-27 15:12:41,464 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:41,613 | INFO | Embedding 進度：9/22 batches
2026-03-27 15:12:41,939 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:42,039 | INFO | Embedding 進度：10/22 batches
2026-03-27 15:12:42,608 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:42,711 | INFO | Embedding 進度：11/22 batches
2026-03-27 15:12:43,026 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:43,121 | INFO | Embedding 進度：12/22 batches
2026-03-27 15:12:43,491 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:43,515 | INFO | Embedding 進度：13/22 batches
2026-03-27 15:12:43,935 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:43,946 | INFO | Embedding 進度：14/22 batches
2026-03-27 15:12:44,355 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:44,492 | INFO | Embedding 進度：15/22 batches
2026-03-27 15:12:45,068 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:45,094 | INFO | Embedding 進度：16/22 batches
2026-03-27 15:12:45,441 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:45,572 | INFO | Embedding 進度：17/22 batches
2026-03-27 15:12:45,957 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:46,068 | INFO | Embedding 進度：18/22 batches
2026-03-27 15:12:46,378 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:46,399 | INFO | Embedding 進度：19/22 batches
2026-03-27 15:12:46,809 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:46,829 | INFO | Embedding 進度：20/22 batches
2026-03-27 15:12:47,264 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:47,330 | INFO | Embedding 進度：21/22 batches
2026-03-27 15:12:47,607 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:47,635 | INFO | Embedding 進度：22/22 batches
2026-03-27 15:12:47,709 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 15:12:47,734 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:12:47,746 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:12:48,861 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0007-c001",
      "page": 7,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5246293711662292,
      "source": "113年報.pdf#page=7"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.4998526108264923,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4802847409248352,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4532244539260864,
      "source": "113年報.pdf#page=160"
    },
    {
      "chunk_id": "113年報.pdf-p0154-c002",
      "page": 154,
      "text": "交換或 認股)普通股、海 外存託憑證或其 他有價證券之金 額 無 無 發行及轉換 (交換 或認股)辦法 無 無 發行及轉換 、 交換或認股辦法 、 發行條件對股權可能稀釋情形 及對現有股東權益影響 無 無 交換標的委託保管機構名稱 無 無 - 148 - 3.3 特特別別股股發發行行情情形形 1. 富邦金控甲種特別股 發行(辦理)日期 項 目 2016 年 4 月 22 日 (富邦金控甲種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 600,000 千股 總額 新台幣 36,000,000,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：甲種特別股年率 4.10%(七年期 IRS 0.885%+3.215%)，按每股發行價 格計算。 七年期 IRS 利率將於發行日起滿七年之次日及其後每七年重設。 甲種特別股自 2023 年 4 月 22 日起重設年率為 4.58125%。 2. 股息發放：本公司對於甲種特別股之股息分派具自主裁量權，包括但不限 於因年度決算無盈餘或盈餘不足分派特別股股息，或因特別股股息之分派 將使本公司資本適足率低於法令或主管機關所定最低要求。 本公司決議取 消特別股之股息分派，將不構成違約事件。 其未分派或分派不足額之股 息，不累積於以後有盈餘年度遞延償付。 本公司決算如有盈餘，應先完納 稅捐、彌補虧損，依法令規定提列法定盈餘公積並依法令規定或實際需要 提列特別盈餘公積，並得分派本公司甲種特別股股息。 甲種特別股股息每 年以現金一次發放，於每年股東常會承認財務報告後，由董事會訂定基準 日支付前一年度得發放之股息。 發行年度及收回年度股息之發放，按當年 度實際發行天數計算，所分配股息將認列於股利憑單。 3. 超額股利分配：甲種特別股除依前述所定之股息率領取股息外，不得參加",
      "score": 0.4514783900976181,
      "source": "113年報.pdf#page=154"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:12:49,910 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 15:12:49,910 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 15:12:50,298 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:51,573 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:12:51,590 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 15:12:51,791 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:51,874 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 15:12:52,105 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:53,399 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:12:53,412 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 15:12:53,649 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:55,595 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:12:55,610 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 15:12:55,805 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:57,036 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:12:57,048 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 15:12:57,283 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:12:59,759 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:12:59,769 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 15:12:59,971 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:07,414 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:07,425 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 15:13:07,617 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:09,423 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:09,432 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 15:13:09,619 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:13,107 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:13,120 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 15:13:13,358 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:15,723 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:15,733 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 15:13:15,997 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:17,651 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:17,660 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 15:13:17,889 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:17,942 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 15:13:18,151 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:19,830 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:19,897 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 15:13:20,106 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:22,485 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:22,498 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 15:13:22,706 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:22,788 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 15:13:23,046 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:25,162 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:25,174 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 15:13:25,427 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:26,858 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:26,868 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 15:13:27,113 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:29,107 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:29,113 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 15:13:29,343 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:30,525 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:30,533 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 15:13:30,761 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:31,794 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:31,804 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 15:13:32,039 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:34,825 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:34,832 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 15:13:35,057 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:35,079 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 15:13:35,285 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:35,319 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 15:13:35,548 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:35,582 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 15:13:35,780 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:35,870 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 15:13:36,074 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:38,039 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:38,049 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 15:13:38,255 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:40,042 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:13:40,050 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 15:13:40,246 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:40,265 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 15:13:40,471 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:40,492 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 15:13:40,718 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:13:41,942 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 5/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 6/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 7/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 8/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 9/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 10/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 11/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 1
已完成題數: 12/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 13/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 14/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 2
已完成題數: 15/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 16/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 17/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 18/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 19/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 20/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 21/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 22/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 23/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 24/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 25/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 3
已完成題數: 26/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 4
已完成題數: 27/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 4
已完成題數: 28/30 | Accuracy: 1.0000 | refused: 1 | hallucination: 4
已完成題數: 29/30 | Accuracy: 1.0000 | refused: 2 | hallucination: 4
已完成題數: 30/30 | Accuracy: 1.0000 | refused: 2 | hallucination: 4
題數: 30
correct 數: 30
accuracy: 1.0000
refused 數: 2
hallucination 數: 4
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 0

```text
題數: 30
correct 數: 30
accuracy: 1.0000
error 數: 4
retrieval_error: 0
synthesis_error: 0
numeric_error: 0
multi_question_error: 0
hallucination: 4
refusal_needed_but_not_triggered: 0
error_analysis.md: outputs/error_analysis.md
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 18
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

## Run Record - 2026-03-27 15:15:08

- workspace: /Users/liuyenzhen/Desktop/Fubon_codex

### Ingest PDF

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:15:11,423 | INFO | PDF 抽取完成：共 272 頁
2026-03-27 15:15:11,475 | INFO | 清理後有效頁數：272
2026-03-27 15:15:11,493 | INFO | 切片完成：共 685 個 chunks
2026-03-27 15:15:11,499 | INFO | 已輸出 chunks：data/processed/chunks.jsonl
```

### Build Index

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:15:12,112 | INFO | chunks_path: /Users/liuyenzhen/Desktop/Fubon_codex/data/processed/chunks.jsonl
2026-03-27 15:15:12,112 | INFO | index_output_dir: /Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:15:12,116 | INFO | 已載入 chunks：685 筆
2026-03-27 15:15:12,848 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:12,921 | INFO | Embedding 進度：1/22 batches
2026-03-27 15:15:13,265 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:13,362 | INFO | Embedding 進度：2/22 batches
2026-03-27 15:15:13,709 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:13,844 | INFO | Embedding 進度：3/22 batches
2026-03-27 15:15:14,168 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:14,300 | INFO | Embedding 進度：4/22 batches
2026-03-27 15:15:14,687 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:14,817 | INFO | Embedding 進度：5/22 batches
2026-03-27 15:15:15,169 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:15,206 | INFO | Embedding 進度：6/22 batches
2026-03-27 15:15:15,746 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:15,832 | INFO | Embedding 進度：7/22 batches
2026-03-27 15:15:16,233 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:16,275 | INFO | Embedding 進度：8/22 batches
2026-03-27 15:15:16,699 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:16,718 | INFO | Embedding 進度：9/22 batches
2026-03-27 15:15:17,069 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:17,087 | INFO | Embedding 進度：10/22 batches
2026-03-27 15:15:17,370 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:17,392 | INFO | Embedding 進度：11/22 batches
2026-03-27 15:15:17,701 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:17,721 | INFO | Embedding 進度：12/22 batches
2026-03-27 15:15:18,143 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:18,163 | INFO | Embedding 進度：13/22 batches
2026-03-27 15:15:18,620 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:18,631 | INFO | Embedding 進度：14/22 batches
2026-03-27 15:15:19,017 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:19,091 | INFO | Embedding 進度：15/22 batches
2026-03-27 15:15:19,453 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:19,469 | INFO | Embedding 進度：16/22 batches
2026-03-27 15:15:19,934 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:20,028 | INFO | Embedding 進度：17/22 batches
2026-03-27 15:15:20,411 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:20,448 | INFO | Embedding 進度：18/22 batches
2026-03-27 15:15:20,777 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:20,911 | INFO | Embedding 進度：19/22 batches
2026-03-27 15:15:21,335 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:21,468 | INFO | Embedding 進度：20/22 batches
2026-03-27 15:15:21,909 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:22,042 | INFO | Embedding 進度：21/22 batches
2026-03-27 15:15:22,292 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:22,351 | INFO | Embedding 進度：22/22 batches
2026-03-27 15:15:22,427 | INFO | FAISS 索引建立完成：ntotal=685, dim=3072
2026-03-27 15:15:22,445 | INFO | 索引輸出完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
2026-03-27 15:15:22,458 | INFO | 完成：/Users/liuyenzhen/Desktop/Fubon_codex/outputs
```

### Retrieve Smoke Test

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:15:23,582 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
{
  "insufficient_evidence": false,
  "results": [
    {
      "chunk_id": "113年報.pdf-p0008-c001",
      "page": 8,
      "text": "- 1 - 1. 致致股股東東報報告告書書 各各位位親親愛愛的的股股東東：： 回顧 2024 年全球經濟情勢，通膨壓力減緩，經濟呈現溫和復甦，惟產業表現分歧，牽制全球經濟成 長動能，使各國景氣及通膨變化出現差異，台灣則受惠出口及生產動能增溫，加上消費動能穩定，推 升經濟成長 ，2024 年台灣金控業整體獲利表現亮眼 ， 富邦金控稅後淨利亦創歷史新高達1,508.2 億 元， 每股盈餘 10.77 元，連續十六年蟬聯台灣金融業每股獲利龍頭，金控合併總資產逾 12 兆。 富邦金控除深耕台灣市場，亦持續推動區域佈局並透過異業結盟開啟創新金融模式，以自身優勢為基 礎，結合同業及跨業資源，增強金融服務實力，持續為新舊客戶提供金融百貨服務，並透過金融科技 挹注創新能量，推動金控資源整合，業務範疇涵蓋銀行、保險與資產管理，打造多元金融服務平台， 將觸角延伸至亞洲其他區域，未來將持續尋求各項合作機會，除致力於提升現有海外事業營運成果， 並以亞洲為重心，持續評估併購及參股機會，穩定朝向成為「亞洲一流金融機構」的目標邁進。 台台灣灣經經濟濟展展現現強強勁勁動動能能 連連續續十十六六年年榮榮登登金金控控每每股股獲獲利利龍龍頭頭 回顧 2024 年，台 灣 受 惠 於AI 發展浪潮 ， 帶動電子 、 資通訊產品強勁需求 ， 使整體出口成長明顯回升 。 隨著產業庫存去化改善，新興科技蓬勃商機提振企業投資意願，使民間投資快速復甦，加上製造業景 氣好轉帶動企業調薪意願 ， 支持民間消費穩健成長 。 在內 、 外需同步擴張下 ， 台灣經濟展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！",
      "score": 0.5219211137294769,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0008-c002",
      "page": 8,
      "text": "展現強勁動能 。 2024 年台灣經濟動能強勁，加上股市熱絡，台灣金融業獲利表現亮眼，富邦金控旗下各子公司持續有 傑出表現，全年稅後淨利達1,508.2 億元，獲利創歷史新高紀錄，每股盈餘10.77 元，連續十六年位居 金控業每股獲利龍頭！ 獲利來源主要來自富邦人壽與台北富邦銀行。 富邦金控資產報酬率(ROA)及股 東權益報酬率(ROE)分別為 1.30%和 17.20%。 富邦金控除獲利創歷史新高外，合併總資產亦維持成長動能，至 2024 年 12 月底已逾 12 兆大關，達 12 兆 673 億元，較2023 年底成長 9%，穩居國內第二大金控公司。 子公司富邦人壽、台北富邦銀行、 富邦證券及富邦投信 2024 年全年獲利亦皆創下歷史新高紀錄。 富富邦邦人人壽壽財財務務穩穩健健 展展現現亮亮眼眼經經營營績績效效 2024 年利率仍維持較高水準，第三季起美國聯準會啟動降息循環，對壽險公司有望帶來正面影響； 主 管機關強化商品監理，如強化分紅商品審核及規範實支實付型商品回歸損害填補原則，富邦人壽秉持 彈性商品及多元通路策略，聚焦保障型與分期繳商品銷售，並持續推出多元分紅商品，以創造亮眼績 效表現。 業務面，2024 年初年度保費收入約 1,100.8 億元，業界排名第二，排除投資型之初年度保費 收入約 802.5 億元，業界排名第一； 總保費收入 3,643 億元，業界排名第二。 財務面，總資產穩定成 長，2024 年合併總資產超過 6.2 兆元，位居業界第二，稅後淨利約 1,026.6 億元，為富邦金控重要獲 利引擎。 客戶服務面，富邦人壽強化保險科技運用，推動數位化服務，如運用資通訊技術導入 「68999」 企業官 方簡訊發送碼 ， 以科技防詐 、 杜絕假冒簡訊詐騙 ； 擴大行動身分識別服務 （Mobile ID, MID）， 推 出 「 身",
      "score": 0.4979210877418518,
      "source": "113年報.pdf#page=8"
    },
    {
      "chunk_id": "113年報.pdf-p0156-c001",
      "page": 156,
      "text": "- 149 - 2. 富邦金控乙種特別股 發行(辦理)日期 項 目 2018 年 3 月 16 日 (富邦金控乙種特別股) 面額 新台幣 10 元 發行價格 每股 60 元 股數 總股數 666,660 千股 總額 新台幣 39,999,600,000 元 權 利 義 務 事 項 股息及紅利之分派 1. 股息：乙種特別股年率 3.6%(七年期 IRS 1.17%+2.43%) ，按每股發行價格 計算。 七年期 IRS 利率將於發行日起滿七年之次一營業日及其後每七年重 設。 2. 股息發放：乙種特別股股息每年以現金一次發放，於每年股東常會承認財 務報告後，由董事會訂定基準日支付前一年度得發放之股息。 發行年度及 收回年度股息之發放，依當年度實際發行天數計算。 本公司年度決算後如 有盈餘，應先依法完納稅捐、彌補虧損、提列法定盈餘公積，並依法令規 定或實際需要提列特別盈餘公積，如尚有餘額，得分派乙種特別股股息。 本公司對於乙種特別股之股息分派具自主裁量權，倘因年度決算無盈餘或 盈餘不足分派乙種特別股股息，或因乙種特別股股息之分派將使本公司資 本適足率低於法令或主管機關所定最低要求，本公司決議取消乙種特別股 之股息分派，將不構成違約事件。 乙種特別股為非累積型，其未分派或分 派不足額之股息，不累積於以後有盈餘年度遞延償付。 3. 超額股利分配：乙種特別股股東除依本項第一款所訂之股息率領取股息 外，不得參加普通股關於盈餘及資本公積為現金及撥充資本之分派。 剩餘財產之分派 乙種特別股股東分派本公司剩餘財產之順序優於普通股股東，且與本公司所 發行之各種特別股股東受償順序相同，但以不超過發行金額為限。 表決權之行使 乙種特別股股東於股東會無表決權、亦無選舉董事之權利； 但得被選舉為董 事。 於乙種特別股股東會及關係乙種特別股股東權利事項之股東會有表決 權。",
      "score": 0.4780631399154663,
      "source": "113年報.pdf#page=156"
    },
    {
      "chunk_id": "113年報.pdf-p0269-c001",
      "page": 269,
      "text": "- 263 - 5.6.7 本公司及子公司形象改變對企業危機管理之影響及因應措施 富邦金控長期以來積極實踐企業社會責任，致力維護投資人、股東及各利害關係人之權益，落 實企業的永續經營與穩健發展。 本公司訂定「富邦金融控股股份有限公司暨子公司媒體公關處理準則」及「富邦金融控股股份 有限公司暨子公司媒體危機處理準則」 ，以因應媒體相關的日常採訪及危機突發狀況。 依據 「富邦金融控股股份有限公司暨子公司媒體公關處理準則」 ，明確落實發言人機制及各項媒 體相關事務的處理準則，以傳達正確一致的訊息，協助業務推廣，並維護企業品牌形象。 依據 「富邦金融控股股份有限公司暨子公司媒體危機處理準則」 ， 在涉及影響公司聲望和品牌形象之 媒體危機發生時，將依此準則以最迅速、有效的機制進行通報及媒體危機處理，並評估是否啟 動「媒體危機處理小組」 ，後續由其執行各項因應措施，防止危機擴大並儘速平息，以降低負面 衝擊，確保本公司及子公司品牌聲譽與資產。 展望未來，本公司將持續透過嚴謹的風險控管機制，落實媒體公關處理及媒體危機處理，以維 護公司形象，鞏固經營發展的穩健基礎。 同時，亦將持續關注各方利害關係人意見，致力維護 各利害關係人之權益，並追求企業之永續發展。 5.6.8 進行併購之預期效益、可能風險及因應措施 (1) 進行併購之預期效益 a. 擴大經濟規模：藉由合併增加營業據點，擴展國際服務版圖。 b. 增加經濟範疇：提供全方位服務，提升市場競爭力。 c. 提升管理績效：擴大資源共享利益。 d. 提高股東權益報酬：產生併購之營運綜效，替股東創造獲利收益。 (2) 進行併購之可能風險 a. 在資訊不對稱下，須承受併購金融機構之資產負債風險。 b. 併購對象之獲利能力及前景不如預期，高估併購價值。 c. 併購後，企業文化與組織架構之整合，延後併購綜效產生的時間。",
      "score": 0.4513849151134491,
      "source": "113年報.pdf#page=269"
    },
    {
      "chunk_id": "113年報.pdf-p0160-c002",
      "page": 160,
      "text": "。 - 154 - 4.1.2 本年度經營計畫 回顧 2024 年全球經濟情勢，隨著通膨壓力減緩，經濟呈現溫和復甦，製造業活動除資通訊產業 受惠於人工智慧等新興科技應用需求復甦較為強勁外，其他產業表現相對落後，服務業活動則 維持擴張格局 。 由於產業表現分歧 ， 牽制全球經濟成長動能 ， 使各國景氣及通膨變化出現差異 。 其中，美國民間消費及投資穩健成長，經濟表現具韌性； 歐元區製造業景氣維持低迷，造成經 濟活動疲軟； 日本民間消費及投資好轉，內需復甦提振經濟動能； 中國房市疲弱及消費復甦乏 力，政府加大刺激力道期提振民間信心； 台灣受惠於人工智慧等新興科技應用需求熱絡，出口 及生產動能增溫，加上企業投資意願改善，及消費動能穩定， 推升經濟成長 。 在金融市場方面， 主要央行貨幣政策因為基本面差異而出現明顯落差，歐、美主要央行隨著通膨逐步改善於2024 年陸續啟動降息，日本央行結束負利率政策，朝貨幣政策正常化目標邁進，國際資金隨著市場 氛圍情緒變化而快速移轉 ， 全球金融市場穩定因此受到影響 。 值此全球政經情勢多變之環境下 ， 富邦金控旗下各子公司仍持續有傑出表現，全年稅後淨利達 1,508.2 億元，每股盈餘 10.77 元， 連續十六年蟬聯台灣金融業每股獲利龍頭。 展望 2025 年，隨著美國新任總統 D. Trump 上任，其各項政策轉變將影響全球經貿活動及區域 政治發展，增添全球政經環境之不確定性。 假若美國經貿政策調整幅度有所控制，隨著各國服 務業活動持續擴張，終端需求復甦推動製造業廠商加快回補庫存，全球經濟將持續溫和成長。 各主要經濟體中 ， 預期美國經濟將保持韌性 ， 實現軟著陸目標 ； 歐洲及日本經濟有望緩步復甦 ， 若俄烏戰爭停火並進入協商談判，將有助進一步提振歐洲景氣。 隨著美國陸續與其他國家達成 經貿共識，產業庫存回補將支撐亞洲出口國家貿易動能；",
      "score": 0.4509789526462555,
      "source": "113年報.pdf#page=160"
    }
  ]
}
```

### Batch Evaluate

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO`
- exit_code: 0

```text
2026-03-27 15:15:24,629 | INFO | 問答集讀取完成：30 題，工作表偵測：題目(Q=題目,A=答案,ID=題號,PAGE=來源頁數（PDF）)
2026-03-27 15:15:24,629 | INFO | 評估中：1/30 | 富邦金控 113 年度合併稅後淨利是多少？
2026-03-27 15:15:25,059 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:26,650 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:26,666 | INFO | 評估中：2/30 | 請簡述富邦人壽與富邦產險在2025年於國內的發展策略各是什麼？
2026-03-27 15:15:26,860 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:26,940 | INFO | 評估中：3/30 | 富邦金控合併總資產大約是多少？113年度的每股盈餘為多少？
2026-03-27 15:15:27,137 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:28,926 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:28,938 | INFO | 評估中：4/30 | 富邦金控連續幾年成為每股盈餘獲利王？
2026-03-27 15:15:29,128 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:30,557 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:30,569 | INFO | 評估中：5/30 | 富邦金控總資產報酬率（ROA）和股東權益報酬率（ROE）大約為何？
2026-03-27 15:15:30,764 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:34,282 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:34,292 | INFO | 評估中：6/30 | 2024年富邦人壽、北富銀、富邦證券的前度稅後淨利是多少？
2026-03-27 15:15:34,523 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:36,080 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:36,092 | INFO | 評估中：7/30 | 富邦金控旗下主要子公司有哪些？
2026-03-27 15:15:36,293 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:42,286 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:42,303 | INFO | 評估中：8/30 | 請列出富邦金融控股股份有限公司的電話和地址
2026-03-27 15:15:42,560 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:43,877 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:43,885 | INFO | 評估中：9/30 | 請問公司針對健康安全計劃的壓力管理措施有哪幾項
2026-03-27 15:15:44,154 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:47,494 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:47,505 | INFO | 評估中：10/30 | 2024年普通股現金股利發放總和為多少？
2026-03-27 15:15:47,710 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:15:59,970 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:15:59,983 | INFO | 評估中：11/30 | 2024 年度普通股現金股利每股為多少元？
2026-03-27 15:16:00,228 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:01,486 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:01,506 | INFO | 評估中：12/30 | 根據年報中「最近二年度公司溫室氣體盤查」數據，請計算富邦金控 2024 年度之營運排放總量（範疇一與範疇二之合計），相較
2026-03-27 15:16:01,771 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:01,806 | INFO | 評估中：13/30 | 富邦人壽 2024 年初年度保費收入 (FYP) 在業界的排名為何？
2026-03-27 15:16:02,231 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:03,816 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:03,825 | INFO | 評估中：14/30 | 橫跨各子公司當中，年報中有哪些共同考量的風險類型？
2026-03-27 15:16:04,076 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:06,552 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:06,561 | INFO | 評估中：15/30 | 台北富邦銀行 2024 年底的逾放比是多少？
2026-03-27 15:16:06,782 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:06,858 | INFO | 評估中：16/30 | 富邦金控 2024 年底的資本適足率 (CAR) 約為多少？
2026-03-27 15:16:07,102 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:08,192 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:08,202 | INFO | 評估中：17/30 | 截至 2024 年底，富邦產險累積擁有的發明專利與新型專利各是多少？
2026-03-27 15:16:08,437 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:10,012 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:10,021 | INFO | 評估中：18/30 | 富邦金控承諾海內外營運據點百分之百使用綠電的目標年份為何？
2026-03-27 15:16:10,227 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:11,468 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:11,474 | INFO | 評估中：19/30 | 富邦金控目前設有幾名女性董事？
2026-03-27 15:16:11,707 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:13,421 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:13,429 | INFO | 評估中：20/30 | 富邦金控董事會成員目前平均任期為多少年？
2026-03-27 15:16:13,643 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:15,346 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:15,355 | INFO | 評估中：21/30 | 穆迪 (Moody's) 給予富邦金控的國際長期信用評等為何？
2026-03-27 15:16:15,599 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:16,994 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:17,003 | INFO | 評估中：22/30 | 113 年度最主要的獲利來源是什麼？
2026-03-27 15:16:17,213 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:17,236 | INFO | 評估中：23/30 | 總結富邦金控 2024 年在防詐與金融安全方面的具體具體行動。
2026-03-27 15:16:17,472 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:17,509 | INFO | 評估中：24/30 | 請彙整富邦金控 2025 年針對人壽、銀行、證券這三大子公司的核心發展策略。
2026-03-27 15:16:17,717 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:17,749 | INFO | 評估中：25/30 | 說明富邦金控董事會成員在「多元化政策」上的具體目標，以及目前女性董事的比例與未來規劃。
2026-03-27 15:16:17,957 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:18,047 | INFO | 評估中：26/30 | 請比較 2023 年與 2024 年富邦金控給付「一般董事及獨立董事」的酬金總額占稅後純益之比例變化。
2026-03-27 15:16:18,256 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:21,947 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:21,957 | INFO | 評估中：27/30 | 富邦金控 2024 年度在合併資產負債表中的現金及約當現金總額是多少？
2026-03-27 15:16:22,228 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:23,685 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
2026-03-27 15:16:23,700 | INFO | 評估中：28/30 | 根據 113 年度年報，國泰金控 2024 年的合併稅後淨利是多少？
2026-03-27 15:16:24,014 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:24,033 | INFO | 評估中：29/30 | 根據年報，預測 114 年富邦金控 EPS
2026-03-27 15:16:24,277 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:24,292 | INFO | 評估中：30/30 | 富邦慈善基金會 2024 年「用愛心做朋友」助學活動的捐款總額超過多少？
2026-03-27 15:16:24,507 | INFO | HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
2026-03-27 15:16:26,103 | INFO | HTTP Request: POST https://api.openai.com/v1/responses "HTTP/1.1 200 OK"
總題數: 30
已完成題數: 1/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 2/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 3/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 4/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 5/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 6/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 7/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 8/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 9/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 10/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 11/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 12/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 13/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 14/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 15/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 16/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 17/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 18/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 19/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 20/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 21/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 22/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 23/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 24/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 25/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 26/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 27/30 | Accuracy: 1.0000 | refused: 0 | hallucination: 0
已完成題數: 28/30 | Accuracy: 1.0000 | refused: 1 | hallucination: 0
已完成題數: 29/30 | Accuracy: 1.0000 | refused: 2 | hallucination: 0
已完成題數: 30/30 | Accuracy: 1.0000 | refused: 2 | hallucination: 0
題數: 30
correct 數: 30
accuracy: 1.0000
refused 數: 2
hallucination 數: 0
predictions.csv: outputs/predictions.csv
```

### Error Analysis

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md`
- exit_code: 1

```text
2026-03-27 15:16:26,811 | ERROR | 產生錯誤分析失敗：'error_category'
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3791, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "index.pyx", line 152, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 181, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'error_category'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/liuyenzhen/Desktop/Fubon_codex/src/error_analysis.py", line 348, in main
    generate_error_analysis(
  File "/Users/liuyenzhen/Desktop/Fubon_codex/src/error_analysis.py", line 288, in generate_error_analysis
    report_text = build_error_analysis_md(
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/liuyenzhen/Desktop/Fubon_codex/src/error_analysis.py", line 275, in build_error_analysis_md
    lines.append(_render_cases_md(error_df=error_df, category=category, max_cases=max_cases_per_category))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/liuyenzhen/Desktop/Fubon_codex/src/error_analysis.py", line 220, in _render_cases_md
    category_df = error_df[error_df["error_category"] == category].head(max_cases)
                           ~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/core/frame.py", line 3893, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3798, in get_loc
    raise KeyError(key) from err
KeyError: 'error_category'
```

### Progress Report

- command: `cd /Users/liuyenzhen/Desktop/Fubon_codex && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md`
- exit_code: 0

```text
rows: 19
csv: outputs/progress_history.csv
md: outputs/progress_history.md
```

