from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker
session = Session()
class student(Base):
    __tablename__ = 'students'
    studentId = Column(Integer,primary_key=True),
    studentName = Column(String),
    studentAge = Column(Integer)
    def __init__(self,studentName,studentAge):
        self.studentId = None,
        self.studentName = studentName,
        self.studentAge = studentAge
def addStudent(studentAge,studentName):
    exist = session.querry(student).filter(studentName == studentName)
old = session.query(student).filter(student.studentAge < 10).all()
print(old)
