# 富邦金控年報 RAG 問答系統

本專案為「先檢索、再作答」的年報問答系統，重點如下：

- 只根據檢索證據回答，不使用外部知識補答案
- 證據不足時拒答（含預測題與非富邦主體題）
- 回答附頁碼
- 支援 Excel 問答集批次評估
- 提供幻覺偵測、錯誤分析與修正歷程追蹤
- 使用繁體中文與台灣用語

## Project Objective

本專案對應「題目一：大語言模型運用」，目標是建立可驗證的富邦金控年報問答系統，並同時滿足：

- 可回答年報事實型問題（數字、策略、比較、複合查找）
- 以附件問答集進行批次評估並計算 Accuracy
- 可辨識證據不足並拒答，降低幻覺風險
- 產生可追蹤的錯誤分析與迭代紀錄，支援持續優化

## Pipeline Overview

系統採用 evidence-constrained RAG（先檢索、再作答，且回答受證據約束）：

1. PDF 前處理：逐頁抽字、清理噪訊、切 chunk（保留頁碼）
2. 向量化與索引：OpenAI Embeddings + FAISS 本地索引
3. 檢索：向量召回 + 詞面補強排序，回傳 top-k 證據
4. 回答：LLM 僅根據檢索內容輸出 JSON（含 pages / refused）
5. 評估：批次跑 Excel 問答集，產生 predictions 與 Accuracy
6. 錯誤分析：分類錯誤型態並輸出可簡報化報告

## Evaluation Overview

目前評估流程由 `src/evaluate.py` + `src/error_analysis.py` 組成：

- `evaluate.py`：逐題呼叫 `answer_question()`，輸出 `outputs/predictions.csv`
- 核心欄位：`is_correct`、`refused`、`hallucination`、`pages`、`note`
- `error_analysis.py`：從 `predictions.csv` 產生 `outputs/error_analysis.md`
- 錯誤分類：`retrieval_error`、`synthesis_error`、`numeric_error`、`multi_question_error`、`hallucination`、`formatting_difference`

## Hallucination Control Overview

本專案以「拒答優先 + 證據約束」控制幻覺：

- 檢索不足時直接拒答，不進入回答生成
- 問題主體不在證據中（或外部主體）時拒答
- 預測/推估型問題在無可驗證證據時拒答
- 回答需對齊引用頁碼與數值證據，避免憑空補數字
- 錯誤分析中將 `formatting_difference` 與 `hallucination` 分開，避免誤判

## 專案結構

```text
Fubon_codex/
├── .env.example
├── README.md
├── requirements.txt
├── scripts/
│   └── run_and_record.sh
├── src/
│   ├── ingest_pdf.py
│   ├── build_index.py
│   ├── retrieve.py
│   ├── prompts.py
│   ├── answer.py
│   ├── evaluate.py
│   ├── error_analysis.py
│   ├── progress_report.py
│   ├── config.py
│   └── utils.py
├── data/processed/
└── outputs/
```

## 流程說明

1. `ingest_pdf.py`
   讀取 PDF，逐頁抽字、清理、切 chunk，輸出 `chunks.jsonl`
2. `build_index.py`
   使用 OpenAI Embeddings + FAISS 建立本地向量索引
3. `retrieve.py`
   查詢本地索引，回傳 top-k chunks（含分數與頁碼）
4. `answer.py`
   先檢索再作答；證據不足直接拒答；回傳結構化欄位
5. `evaluate.py`
   讀取 Excel 問答集，逐題呼叫 `answer_question`，輸出 `predictions.csv`
6. `error_analysis.py`
   依規則分類錯誤，輸出 `error_analysis.md`
7. `progress_report.py`
   從 `run_records.md` 產生每輪修正成效歷程（答對題數、accuracy、錯誤率、hallucination 等）

## 安裝與設定

1. 建立環境並安裝套件

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. 建立環境變數檔

```bash
cp .env.example .env
```

請確認 `.env` 內至少有：

- `OPENAI_API_KEY`
- `PDF_PATH`
- `QA_EXCEL_PATH`
- `INDEX_DIR=outputs`
- `OUTPUT_DIR=outputs`

`.env` 放置位置：

- `Fubon_codex/.env`（專案根目錄）

## 穩定執行順序（請在專案根目錄執行）

```bash
python src/ingest_pdf.py --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl
python src/build_index.py --chunks-path data/processed/chunks.jsonl --output-dir outputs
python src/evaluate.py --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv
```

## 指令用法

### 1) PDF 前處理（切片）

```bash
python -m src.ingest_pdf \
  --pdf-path 113年報.pdf \
  --output-path data/processed/chunks.jsonl \
  --chunk-size 800 \
  --chunk-overlap 120
```

### 2) 建立向量索引

```bash
python src/build_index.py \
  --chunks-path data/processed/chunks.jsonl \
  --output-dir outputs \
  --batch-size 32 \
  --max-retries 3
```

### 3) 單題檢索測試

```bash
python -m src.retrieve --query "富邦金控113年度合併稅後淨利是多少？" --top-k 5
```

### 4) 單題問答測試

```bash
python -m src.answer --question "富邦金控113年度合併稅後淨利是多少？"
```

### 5) 批次評估

```bash
python src/evaluate.py \
  --qa-path 題目一_附件_問答集.xlsx \
  --output-path outputs/predictions.csv
```

### 6) 錯誤分析

```bash
python -m src.error_analysis \
  --predictions-path outputs/predictions.csv \
  --output-path outputs/error_analysis.md
```

### 7) 修正歷程彙總

```bash
python -m src.progress_report \
  --run-records-path outputs/run_records.md \
  --output-csv outputs/progress_history.csv \
  --output-md outputs/progress_history.md
```

### 8) 一鍵跑完整流程 + 全量記錄

```bash
./scripts/run_and_record.sh
```

## 主要輸出檔

- `outputs/faiss.index`
- `outputs/metadata.jsonl`
- `outputs/index_manifest.json`
- `outputs/predictions.csv`
- `outputs/error_analysis.md`
- `outputs/run_records.md`
- `outputs/progress_history.csv`
- `outputs/progress_history.md`
- `outputs/history/<timestamp>/`（每輪快照）

## 測試

```bash
pytest -q
```

## 方法補充文件

- `docs/methods_summary.md`：整理方法亮點、前處理 insight、錯誤反饋閉環與金融落地場景（適合簡報引用）
