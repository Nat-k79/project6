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
        assert "my_function ok" in content

    # Проверяем вывод в консоль
        captured = capsys.readouterr()
        assert "my_function ok" in captured.out


def test_my_function(log_file, capsys):
    @log(filename=log_file)
    def my_function(x, y):
        return x / y  # Это вызовет ZeroDivisionError

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    # Проверяем содержимое лог-файла
    with open(log_file) as f:
        content = f.read()
        assert "my_function error: ZeroDivisionError" in content

    # Проверяем вывод в консоль
        captured = capsys.readouterr()
        assert "my_function error: ZeroDivisionError" in captured.out


def test_log_file_creation(log_file):
    @log(filename=log_file)
    def my_function(x):
        return x

    my_function(10)

    # Проверяем, что файл был создан
    assert os.path.exists(log_file)
