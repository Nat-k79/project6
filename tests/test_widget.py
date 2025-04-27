import pytest
from widget import mask_account_card


@pytest.mark.parametrize("input_data, expected", [
    ("1234567890123456", "************3456"),
    ("123456789012", "**********012"),
    ("invalid_input", None),
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2023-01-01", "2023-01-01"),
    ("01/01/2023", "2023-01-01"),
    ("invalid_date", None),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
