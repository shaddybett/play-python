from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

generate_id = uuid()
Base = declarative_base()
db = 'sqlite:///bestDB.db'
engine = create_engine(db)
engine.metadata.create_all(bind=engine)

Session = sessionmaker()
session = Session()

class Student(Base):
    __tablename__='students'
    studentId = Column(Integer,primary_key=True,default=generate_id)
    studentName = Column(String)
    studentEmail = Column(String)
    studentAge = Column(Integer)

    def __init__(self,studentAge,studentEmail,studentName):
        self.studentId = None
        self.studentAge = studentAge
        self.studentEmail = studentEmail
        self.studentName = studentName

        exists = session.query(Student).filter(Student.studentEmail == studentEmail).all()
        if len(exists) > 0:
            print('Student already exists')
        else:
            studentList = Student(studentAge,studentEmail,studentName)
            session.add(studentList)
            Session.commit
