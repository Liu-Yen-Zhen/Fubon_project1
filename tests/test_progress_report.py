from pathlib import Path

from src.progress_report import parse_run_records


def test_parse_run_records_extracts_metrics(tmp_path: Path) -> None:
    run_records = tmp_path / "run_records.md"
    run_records.write_text(
        "\n".join(
            [
                "## Run Record - 2026-03-27 10:00:00",
                "",
                "### Batch Evaluate",
                "",
                "```text",
                "題數: 30",
                "correct 數: 18",
                "accuracy: 0.6000",
                "refused 數: 3",
                "hallucination 數: 2",
                "```",
                "",
                "### Error Analysis",
                "",
                "```text",
                "retrieval_error: 0",
                "synthesis_error: 4",
                "numeric_error: 3",
                "multi_question_error: 1",
                "hallucination: 2",
                "refusal_needed_but_not_triggered: 0",
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )

    rows = parse_run_records(run_records)
    assert len(rows) == 1
    row = rows[0]
    assert row.total == 30
    assert row.correct == 18
    assert row.accuracy == 0.6
    assert row.error_rate == 0.4
    assert row.refused == 3
    assert row.hallucination == 2
    assert row.synthesis_error == 4
