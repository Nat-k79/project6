import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data"
API_KEY = os.getenv("API_KEY")


def convert_currency(transaction):
    """Конвертирует сумму транзакции в рубли."""
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency not in ['USD', 'EUR']:
        return float(amount)

    headers = {
        "apikey": API_KEY
    }
    response = requests.get(f"{API_URL}/convert?to=RUB&from={currency}&amount={amount}", headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result.get('result', 0.0)

    return float(amount)  # Возвращаем исходную сумму, если произошла ошибка
