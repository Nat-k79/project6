from datetime import datetime


def mask_account_card(input_string: str) -> str:
    # Проверка на 16-значный номер карты
    if len(input_string) == 16 and input_string.isdigit():
        return f"{input_string[:4]} {input_string[4:6]}** **** {input_string[12:]}"
    # Проверка на 12-значный номер счета
    elif len(input_string) == 12 and input_string.isdigit():
        return f"Счет **{input_string[-4:]}"
    # Если входные данные не соответствуют ожидаемым форматам
    else:
        return "Некорректный формат ввода"


# Примеры использования
print(mask_account_card("Visa Platinum 7000792289606361"))  # Вывод: Visa Platinum 7000 79 **** 6361
print(mask_account_card("Maestro 7000792289606361"))       # Вывод: Maestro 7000 79 **** 6361
print(mask_account_card("Счет 123456789012"))      # Вывод: Счет **4301


def get_date(date_str: str) -> str:
    """Функция преобразует строку даты"""
    try:
        # Сравниваем дату в формате YYYY-MM-DD
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d")  # Возвращаем дату в нужном формате
    except ValueError:
        try:
            # Если не удалось, сравниваем в формате DD/MM/YYYY
            dt = datetime.strptime(date_str, "%d/%m/%Y")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            # Обработка случая, когда формат даты некорректен
            return "Некорректный формат даты"


print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
