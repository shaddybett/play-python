from sqlalchemy import create_engine, Integer, String, Column
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

# Base = declarative_base()  
Base = declarative_base()

db = 'sqlite:///wedDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):  # Inherit from Base
    __tablename__='books'
    bookId = Column('bookId', String, primary_key=True, default=generate_uuid)
    bookName = Column('bookName', String)
    bookPages = Column('bookPages', Integer)
    bookAuthor = Column('bookAuthor', String)

    @classmethod    
    def add_books(cls, bookName, bookPages, bookAuthor):
        exists = session.query(cls).filter(cls.bookName == bookName).all()
        if len(exists) > 0:
            print('Book already exists')
        else:
            new_book = cls(bookAuthor=bookAuthor, bookName=bookName, bookPages=bookPages)
            session.add(new_book)
            session.commit()
            print('New book added')          

# Example usage:
# Book.add_books('The Great Gatsby', 1200, 'F. Scott Haddersfield')


