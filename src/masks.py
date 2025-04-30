def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты по правилу XXXX XX** **** XXXX.


    :param card_number: Номер карты в виде числа.
    :return: Маскированный номер карты.
    """
    card_str = str(card_number)
    card_str = card_str.replace(" ", "")

    masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked_card


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску счета по правилу **ХХХХ
    :param account_number: Номер счета в виде числа.
    :return: Маскированный номер счета.
    """
    # Преобразуем номер счета в строку
    account_str = str(account_number)

    # Формируем маску
    masked_account = f"**{account_str[-4:]}"
    return masked_account


# Примеры использования
print(get_mask_card_number(1234567812345678))  # XXXX XX78 **** 5678
print(get_mask_account(123456789012))  # **9012
