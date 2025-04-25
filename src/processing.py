from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    :transactions: Список словарей с данными о банковских операциях.
    :state: Значение ключа для фильтрации. По умолчанию 'EXECUTED'.
    :return: Новый список словарей содержит те, у которых ключ 'state' соответствует указанному значению.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Функция сортирует список словарей по дате.
    :transactions: Список словарей с данными о банковских операциях.
    :descending: Параметр задает порядок сортировки. По умолчанию True (по убыванию).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)
