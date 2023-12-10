from sqlalchemy import create_engine,ForeignKey,INTEGER,Column,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base
def generate_uuid():
    return str(uuid.uuid4())

