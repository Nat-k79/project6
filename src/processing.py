from typing import List, Dict, Optional


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Функция сортирует список словарей по дате.

    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)