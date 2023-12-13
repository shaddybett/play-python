# from sqlalchemy import create_engine, Integer, String, Column
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import uuid

# def generate_uuid():
#     return str(uuid.uuid4())

# Base = declarative_base()  # Corrected this line
# db = 'sqlite:///wedDB.db'
# engine = create_engine(db)
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()


from sqlalchemy import create_engine,String,Column,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str (uuid.uuid4())

Base = declarative_base()

db = 'sqlite:///wedDB.db'