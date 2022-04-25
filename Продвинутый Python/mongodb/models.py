from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def create_all(engine):
    Base.metadata.create_all(engine)


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    start_at = Column(Date, nullable=False)
    tags = Column(JSONB, default=list, nullable=True)

    def __str__(self):
        return f'<{self.id} | {self.name} | {self.start_at}>'


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gpa = Column(Numeric(precision=4, scale=2), nullable=True)

    def __str__(self):
        return f'[{self.id} | {self.name}, {self.gpa}]'

    def __repr__(self):
        return f'<{self.id} | {self.name}, {self.gpa}>'
