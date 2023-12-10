from sqlalchemy import create_engine,ForeignKey,String,Integer,Column
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
    
    def __init__(self,firstName,lastName,profileName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email
class posts(Base):
    __tablename__='posts'
    userId = Column('userId',String,ForeignKey('users.userID'),default=generate_uuid)
    postId = Column('postId',String,primary_key=True,default=generate_uuid)
    postContent = Column('postContent',String)

    def __init__(self,userId,postContent):
        self.userId = userId
        self.postContent = postContent

def addUser(firstName,lastName,profileName,email,session):
    user = users(firstName,lastName,profileName,email)
    session.add(user)
    session.commit()
    print('user added to database')
            
            # add post
def add_posts(session,userId,postContent):
    newPost = posts(userId,postContent)
    session.add(newPost)
    session.commit()
    print('all good')

db = 'sqlite:///socialDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

firstName = 'clark'
lastName = 'lone'
profileName = 'Clone'
email = 'Clone@gmail.com'
addUser(firstName,lastName,profileName,email,session)


