import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_string, expected", [
       ("1234567812345678", "1234 56** **** 5678"),
       ("123456789012", "Счет **9012"),
       ("invalid_input", "Некорректный формат ввода"),
])
def test_mask_account_card(input_string: str, expected: str) -> None:
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-01-01", "2023-01-01"),
    ("01/01/2023", "2023-01-01"),
    ("invalid_date", "Некорректный формат даты"),
])
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
