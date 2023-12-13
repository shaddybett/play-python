from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()  # Corrected this line
db = 'sqlite:///wedDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Book:
    __tablename__='books'
    bookId = Column('bookId',String,primary_key=True,default=generate_uuid)
    bookName = Column('bookName',String)
    bookPages = Column('bookPages',Integer)
    bookAuthor = Column('bookAuthor',String)
    