from datetime import datetime
from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)

        with open("log.txt", mode="a", encoding="utf8") as ff:
            current_time = datetime.now()
            function_name = function.__name__
            function_doc = function.__doc__
            ff.write(f"Время запуска функции:\t {current_time}\n"
                     f"Название функции:\t {function_name}\n"
                     f"Документация функции:\t {function_doc}\n"
                     f"Аргументы:\n"
                     f"\targs: \t\t{args}\n"
                     f"\tkwargs: \t{kwargs}\n"
                     f"Результат работы функции:\n"
                     f"{result}\n"
                     f"---------------------------------------------------\n")

        return result

    return wrapper


def params_logger(path):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)

            with open(path, mode="a", encoding="utf8") as ff:
                current_time = datetime.now()
                function_name = function.__name__
                function_doc = function.__doc__
                ff.write(f"Время запуска функции:\t {current_time}\n"
                         f"Название функции:\t {function_name}\n"
                         f"Документация функции:\t {function_doc}\n"
                         f"Аргументы:\n"
                         f"\targs: \t\t{args}\n"
                         f"\tkwargs: \t{kwargs}\n"
                         f"Результат работы функции:\n"
                         f"{result}\n"
                         f"---------------------------------------------------\n")

            return result

        return wrapper

    return decorator
