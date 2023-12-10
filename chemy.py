from sqlalchemy import create_engine,ForeignKey,String,integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()
def generate_uuid():
    return str(uuid.uuid4())

class users(Base):
    __tablename__= 'users'
    userID = Column('userID',String,primary_key=True,default=generate_uuid)
    firstName = Column('firstName', String)
    lastName = Column('lastName',String)
    profileName = Column('profileName',String)
    email = Column('email',String)