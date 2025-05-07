import os

import pytest

from src.decorators import log


@pytest.fixture(scope="function", autouse=True)
def cleanup_log_file():
    """Фикстура для очистки лог-файла перед каждым тестом."""
    log_file = "mylog.txt"
    if os.path.exists(log_file):
        os.remove(log_file)


@pytest.fixture
def log_file():
    """Возвращает имя лог-файла для тестов."""
    return "mylog.txt"


def test_my_function_success(log_file, capsys):
    @log(filename=log_file)
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    # Проверяем, что результат правильный
    assert result == 3

    # Проверяем содержимое лог-файла
    with open(log_file) as f:
        content = f.read()
        assert "Called my_function with args: (1, 2), kwargs: {}. Result: 3" in content

    # Проверяем вывод в консоль
        captured = capsys.readouterr()
        assert "Called my_function with args: (1, 2), kwargs: {}. Result: 3" in captured.out


def test_my_function_error(log_file, capsys):
    @log(filename=log_file)
    def my_function_error(x, y):
        return x / y  # Это вызовет ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        my_function_error(1, 0)

    # Проверяем содержимое лог-файла
    with open(log_file) as f:
        content = f.read()
        assert "Error in my_function_error: division by zero" in content

    # Проверяем вывод в консоль
        captured = capsys.readouterr()
        assert "Error in my_function_error: division by zero" in captured.out


def test_multiple_calls(log_file, capsys):
    @log(filename=log_file)
    def my_function(x, y):
        return x * y

    my_function(2, 3)
    my_function(4, 5)

    # Проверяем содержимое лог-файла
    with open(log_file) as f:
        content = f.read()
        assert "Called my_function with args: (2, 3), kwargs: {}. Result: 6" in content
        assert "Called my_function with args: (4, 5), kwargs: {}. Result: 20" in content

    # Проверяем вывод в консоль
        captured = capsys.readouterr()
        assert "Called my_function with args: (2, 3), kwargs: {}. Result: 6" in captured.out
        assert "Called my_function with args: (4, 5), kwargs: {}. Result: 20" in captured.out


def test_log_file_creation(log_file):
    @log(filename=log_file)
    def my_function(x):
        return x

    my_function(10)

    # Проверяем, что файл был создан
    assert os.path.exists(log_file)
