import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_numbers() -> list:
    return [
        ("1234 5678 1234 3456", "1234 56** **** 3456"),
        ("1234567812343456", "1234 56** **** 3456")
        ]


def test_get_mask_card_number(card_numbers: list)-> None:
    for card, expected in card_numbers:
        assert get_mask_card_number(card) == expected


@pytest.fixture
def account_numbers() -> list:
    return [
        ("123456789012", "**9012"),
        ]


def test_get_mask_account(account_numbers: list)-> None:
    for account, expected in account_numbers:
        assert get_mask_account(account) == expected
