import json
import logging
import os

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/utils.log')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def read_json_file(file_path):
    """Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента."""
    if not os.path.exists(file_path):
        logger.error(f'Файл не найден: {file_path}')
        return []

    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            if not data:  # Проверяет, что данные не пустые
                logger.warning(f'Файл пустой: {file_path}')
                return []  # Возвращает пустой список, если файл пустой.
            elif not isinstance(data, list):
                logger.warning(f'Данные не являются списком в файле: {file_path}')
                return []  # Возвращает пустой список, если данные не являются списком.
        except json.JSONDecodeError:
            logger.error(f'Ошибка чтения JSON из файла: {file_path}')
            return []  # Возвращает пустой список при ошибке чтения JSON

    logger.info(f'Успешно прочитан файл: {file_path}')
    return data
