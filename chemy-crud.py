from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid


Base = declarative_base()
db = 'sqlite:///bestDB.db'
engine = create_engine(db)
engine.metadata(bind=engine)

class Student(Base):
    __tablename__='students'
    studentId = Column(Integer)
    studentName = Column(String)