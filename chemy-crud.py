from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
     return str(uuid.uuid4())


Base = declarative_base()
db = 'sqlite:///bestDB.db'
engine = create_engine(db)
engine.metadata.create_all(bind=engine)

Session = sessionmaker()
session = Session()

class Student(Base):
    __tablename__='students'
    studentId = Column('studentId',String,primary_key=True,default=generate_uuid)
    studentName = Column('studentName',String)
    studentEmail = Column('studentEmail',String)
    studentAge = Column('studentAge',Integer)

    def __init__(self,studentAge,studentEmail,studentName):
        self.studentId = None
        self.studentAge = studentAge
        self.studentEmail = studentEmail
        self.studentName = studentName

def add_Student(studentAge,studentEmail,studentName):
        exists = session.query(Student).filter(Student.studentEmail == studentEmail).all()
        if len(exists) > 0:
            print('Email already exists')
        else:
            new_Sudent = Student(studentAge,studentEmail,studentName)
            session.add(new_Sudent)
            session.commit()
            print('Added new student')
add_Student(20,'mark@gmail.com','Marcos')            
