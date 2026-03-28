from src.evaluate import judge_correctness


def test_judge_correctness_equivalent_numeric_sentence() -> None:
    reference = "1,508.2 億元"
    predicted = "富邦金控113年度合併稅後淨利為1,508.2億元。"
    assert judge_correctness(reference, predicted) is True


def test_judge_correctness_percent_decimal_equivalent() -> None:
    reference = "0.0012"
    predicted = "0.12%"
    assert judge_correctness(reference, predicted) is True


def test_judge_correctness_chinese_amount_equivalent() -> None:
    reference = "超過 1 億元 (106,749,000 元)"
    predicted = "1億674萬9,000元"
    assert judge_correctness(reference, predicted) is True


def test_judge_correctness_should_fail_when_missing_key_number() -> None:
    reference = "人壽：1026.6億 銀行：313億元 證券：100.2億元"
    predicted = "人壽：1026.6億元；銀行：未揭露；證券：100.2億元"
    assert judge_correctness(reference, predicted) is False
