import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: Путь к Excel-файлу
    :return: Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


csv_transactions = read_transactions_from_csv('transactions.csv')
print(csv_transactions)

excel_transactions = read_transactions_from_excel('transactions_excel.xlsx')
print(excel_transactions)
