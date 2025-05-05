def filter_by_currency(transactions, currency_code):
    """
    Функция принимает на вход список словарей, представляющих транзакции, и возвращает итератор.
    Итератор поочередно выдает транзакции, где валюта совпадает с заданной.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты, по которой нужно фильтровать транзакции.
    :yield: Транзакция, если валюта совпадает с заданной.
    """

    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Функция-генератор принимает список словарей.

    :param transactions: Список словарей с транзакциями.
    :yield: Описание транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int):
    """
    Генератор номеров карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.

    :param start: Начальное значение (включительно).
    :param stop: Конечное значение (включительно).
    :yield: Номера карт от start до stop.
    """

    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
