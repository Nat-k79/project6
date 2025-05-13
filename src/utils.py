import json
import os


def read_json_file(file_path):
    """Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            if not data:  # Проверяет, что данные не пустые
                return []  # Возвращает пустой список, если файл пустой.
            elif not isinstance(data, list):
                return []  # Возвращает пустой список, если данные не являются списком.
        except json.JSONDecodeError:
            return []  # Возвращает пустой список при ошибке чтения JSON

    return data
