import pytest
from masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "************3456"),
        ("1234 5678 9012 3456", "************3456"),
        ("", None),
        ("123456", None),
    ]


def test_get_mask_card_number(card_numbers):
    for card, expected in card_numbers:
        assert get_mask_card_number(card) == expected


@pytest.fixture
def account_numbers():
    return [
        ("123456789012", "**********012"),
        ("1234", None),
        ("", None),
    ]


def test_get_mask_account(account_numbers):
    for account, expected in account_numbers:
        assert get_mask_account(account) == expected
