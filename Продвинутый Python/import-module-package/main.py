from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def now_time():
    print(datetime.utcnow())


if __name__ == '__main__':
    now_time()
    calculate_salary()
    now_time()
    get_employees()
