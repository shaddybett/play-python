from sqlalchemy import create_engine,ForeignKey,INTEGER,Column,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base
def generate_uuid():
    return str(uuid.uuid4())

class users:
    __tablename__= 'users'
    userID = Column('userID',String,primary_key=True,default=generate_uuid)
    firstName = Column('firstName',String)
    lastName = Column('lastName',String)
    email = Column('email',String)
    profileName = Column('profileName',String)

    def __init__(self,firstName,lastName,email,profileName):
        
        