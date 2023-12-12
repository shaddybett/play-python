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
session.commit(student)
session.close()
old = session.query(student).filter(student.studentAge < 10).all()
print()