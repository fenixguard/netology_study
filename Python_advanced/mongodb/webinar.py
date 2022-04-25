import psycopg2 as pg
from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import create_all, Course, Student

engine = create_engine('postgresql://netology:netology@localhost/netology')

create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_course(name, start_at, tags=None):
    course = Course(name=name, start_at=start_at, tags=tags)

    print(course.id, course.name, course.start_at)
    session.add(course)
    session.commit()

    print(course.id, course.name, course.start_at)


def add_student(name: str, gpa: float = None):
    student = Student(name=name, gpa=gpa)
    print(student.id, student.name, student.gpa)

    session.add(student)
    session.commit()
    print(student.id, student.name, student.gpa)


# add_student('Vova', 4.5)
# add_student('Dima')


for s in session.query(Student).all():
    print(s)

for s in session.query(Student).filter(Student.name == 'Vova'):
    print(s)