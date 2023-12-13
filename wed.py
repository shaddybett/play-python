from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str (uuid.uuid4())
Base = declarative_base
db = create_engine
engine = create_engine(db)