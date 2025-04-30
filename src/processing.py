from typing import Dict, List


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


if __name__ == "__main__":
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    executed_transactions = filter_by_state(transactions)
    print("Executed Transactions:", executed_transactions)

    canceled_transactions = filter_by_state(transactions, state='CANCELED')
    print("Canceled Transactions:", canceled_transactions)

    sorted_transactions = sort_by_date(transactions)
    print("Sorted Transactions (Descending):", sorted_transactions)

    sorted_transactions_asc = sort_by_date(transactions, descending=False)
    print("Sorted Transactions (Ascending):", sorted_transactions_asc)
