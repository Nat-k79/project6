import functools


def log(filename):
    """
    Декоратор для логирования начала и конца выполнения функции, а также ее результатов или ошибок.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"Called {func.__name__} with args: {args}, kwargs: {kwargs}. Result: {result}"
                print(message)  # Выводим сообщение в консоль
                with open(filename, 'a') as f:
                    f.write(message + '\n')
                return result
            except Exception as e:
                error_message = f"Error in {func.__name__}: {str(e)}"
                print(error_message)  # Выводим сообщение об ошибке в консоль
                with open(filename, 'a') as f:
                    f.write(error_message + '\n')
                raise  # Пробрасываем исключение дальше
        return wrapper

    return decorator


@log(filename="../mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)  # Вызов функции


@log(filename="../mylog.txt")
def my_function_error(x, y):
    return x / y  # Это вызовет ZeroDivisionError


# Вызываем функцию с ошибкой
try:
    my_function_error(1, 0)
except ZeroDivisionError:
    pass  # Игнорируем ошибку для теста
