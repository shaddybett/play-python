from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()

db = 'sqlite:///best.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
    studentId = Column('studentId', String, primary_key=True, default=generate_uuid)
    studentName = Column('studentName', String)
    studentEmail = Column('studentEmail', String)
    studentAge = Column('studentAge', Integer)

    def __init__(self, studentAge, studentEmail, studentName):
        self.studentId = None
        self.studentAge = studentAge
        self.studentEmail = studentEmail
        self.studentName = studentName

def add_student(studentAge, studentEmail, studentName):
    exists = session.query(Student).filter(Student.studentEmail == studentEmail).all()
    if len(exists) > 0:
        print('Email already exists')
    else:
        new_student = Student(studentAge=studentAge, studentEmail=studentEmail, studentName=studentName)
        session.add(new_student)
        print('New student added')

# Example usage to add a new student to the database
add_student(studentAge=20, studentEmail='Gofa@gmail.com', studentName='Gofa')

# Commit the changes to the database
session.commit()
