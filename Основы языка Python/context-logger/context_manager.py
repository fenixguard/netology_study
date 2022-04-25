from contextlib import contextmanager
from random import randint
from datetime import datetime


@contextmanager
def time_logger():
    date_start = datetime.now()
    print(f"Время начала работы: {date_start}")
    yield  # тут будет подставлен блок из конструции with
    date_end = datetime.now()
    print(f"Время окончания работы: {date_end}")
    print(f"Время работы: {date_end - date_start}")
    print(f"Уникальные значения: {unical_id_list}")


if __name__ == '__main__':
    with time_logger():
        ids = {'user1': [randint(1, 100) for i in range(10_000_000)],
               'user2': [randint(1, 100) for i in range(10_000_000)],
               'user3': [randint(1, 100) for i in range(10_000_000)]}

        unical_id_list = list(set(sum(ids.values(), [])))
