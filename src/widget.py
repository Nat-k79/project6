from datetime import datetime


def mask_account_card(account_info: str) -> str:
    """Функция маскирует номер карты или счета"""
    if "Счет" in account_info:
        # Маскировка для счета
        return account_info.replace(account_info.split()[1], '**' + account_info.split()[1][-4:])
    else:
        # Маскировка для карт
        parts = account_info.split()
        card_number = parts[-1]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return f"{' '.join(parts[:-1])} {masked_number}"


print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305


def get_date(date_str: str) -> str:
    """Функция преобразует строку даты"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
