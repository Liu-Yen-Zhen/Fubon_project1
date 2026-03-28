#!/usr/bin/env bash

set +e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_FILE="${ROOT_DIR}/outputs/run_records.md"

mkdir -p "${ROOT_DIR}/outputs"

timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
stamp="$(date '+%Y%m%d_%H%M%S')"
{
  echo "## Run Record - ${timestamp}"
  echo ""
  echo "- workspace: ${ROOT_DIR}"
  echo ""
} >> "${LOG_FILE}"

run_step() {
  local name="$1"
  local cmd="$2"
  local tmp
  tmp="$(mktemp)"
  echo "[RUN] ${name}"

  eval "${cmd}" >"${tmp}" 2>&1
  local code=$?

  {
    echo "### ${name}"
    echo ""
    echo "- command: \`${cmd}\`"
    echo "- exit_code: ${code}"
    echo ""
    echo "\`\`\`text"
    sed -n '1,200p' "${tmp}"
    echo "\`\`\`"
    echo ""
  } >> "${LOG_FILE}"

  rm -f "${tmp}"
}

run_step "Ingest PDF" \
  "cd ${ROOT_DIR} && python -m src.ingest_pdf --pdf-path 113年報.pdf --output-path data/processed/chunks.jsonl --chunk-size 800 --chunk-overlap 120 --log-level INFO"

run_step "Build Index" \
  "cd ${ROOT_DIR} && python -m src.build_index --chunks-path data/processed/chunks.jsonl --output-dir outputs --batch-size 32 --max-retries 1 --log-level INFO"

run_step "Retrieve Smoke Test" \
  "cd ${ROOT_DIR} && python -m src.retrieve --query 富邦金控113年度合併稅後淨利是多少 --top-k 5 --log-level INFO"

run_step "Batch Evaluate" \
  "cd ${ROOT_DIR} && python -m src.evaluate --qa-path 題目一_附件_問答集.xlsx --output-path outputs/predictions.csv --log-level INFO"

run_step "Error Analysis" \
  "cd ${ROOT_DIR} && python -m src.error_analysis --predictions-path outputs/predictions.csv --output-path outputs/error_analysis.md"

run_step "Progress Report" \
  "cd ${ROOT_DIR} && python -m src.progress_report --run-records-path outputs/run_records.md --output-csv outputs/progress_history.csv --output-md outputs/progress_history.md"

run_history_dir="${ROOT_DIR}/outputs/history/${stamp}"
mkdir -p "${run_history_dir}"
cp -f "${ROOT_DIR}/outputs/predictions.csv" "${run_history_dir}/predictions.csv" 2>/dev/null
cp -f "${ROOT_DIR}/outputs/error_analysis.md" "${run_history_dir}/error_analysis.md" 2>/dev/null
cp -f "${ROOT_DIR}/outputs/progress_history.md" "${run_history_dir}/progress_history.md" 2>/dev/null

echo "record_file=${LOG_FILE}"
echo "run_snapshot_dir=${run_history_dir}"
