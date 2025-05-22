import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/masks.log')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты по правилу XXXX XX** **** XXXX.


    :param card_number: Номер карты в виде числа.
    :return: Маскированный номер карты.
    """
    try:
        card_str = str(card_number)
        card_str = card_str.replace(" ", "")

        if len(card_str) != 16 or not card_str.isdigit():
            raise ValueError("Номер карты должен содержать 16 цифр.")

        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"

        logger.info(f"Успешно замаскирован номер карты: {masked_card}")
        return masked_card
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску счета по правилу **ХХХХ
    :param account_number: Номер счета в виде числа.
    :return: Маскированный номер счета.
    """
    try:
        account_str = str(account_number)

        if len(account_str) < 4 or not account_str.isdigit():
            raise ValueError("Номер счета должен содержать как минимум 4 цифры.")

        masked_account = f"{'**'}{account_str[-4:]}"

        logger.info(f"Успешно замаскирован номер счета: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счета: {e}")
        raise


# Примеры использования
if __name__ == "__main__":
    print(get_mask_card_number(1234567812345678))  # XXXX XX78 **** 5678
    print(get_mask_account(123456789012))  # **9012
