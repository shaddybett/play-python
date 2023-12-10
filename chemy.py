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


class likes(Base):
    __tablename__ = 'likes'
    userId = Column('userId',String,ForeignKey('users.userID'),default=generate_uuid)
    likedId = Column('likedId',String,primary_key=True,default=generate_uuid)
    postId = Column('postId',String,ForeignKey('posts.postId'),default=generate_uuid)

    def __init__(self,userId,postId):
        self.userId = userId
        self.postId = postId


def addUser(firstName,lastName,profileName,email,session):
    exist = session.query(users).filter(users.email==email).all()
    if len(exist)>0:
        print('Email already exists!')
    else:
        user = users(firstName,lastName,profileName,email)
        session.add(user)
        session.commit()
        print('user added to database')
            # add post
def addpost(userId,postContent,session):
    newPost = posts(userId,postContent)
    session.add(newPost)
    session.commit()
    print('all good')

def addLike(userId,postId):
    like = likes(userId,postId)
    session.add(like)
    session.commit()
    print('wow liked!')


db = 'sqlite:///socialDB.db'
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

firstName = 'Mich'
lastName = 'tai'
profileName = 'mTai'
email = 'mTai@gmail.com'
# addUser(firstName,lastName,profileName,email,session)

userId = "586fc4c9-6633-4fcb-aee0-76bd231f94b1"
postId = '3f0f7a8c-dab3-4c02-a60f-b85dfc0eba46'
postContent = 'meet at the usual restaurnt later'
# addpost(userId,postContent,session)

# allPosts = session.query(posts).filter(posts.userId == userId).all()
# postList = []
# for p in allPosts:
#     postList.append(p.postContent)
# print(postList)    
# addLike(postId,userId)

postLikes = session.query(likes).filter(likes.postId==postId).all()
print(len(postLikes))

