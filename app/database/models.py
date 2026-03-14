# Importing necessary libraries
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base


# Model for User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # Relationship with other tables
    posts = relationship('Post', back_populates='author')

# Model for Post
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='posts')


Base = declarative_base()

class Boundary(Base):
    __tablename__ = "boundaries"

    id = Column(String, primary_key=True)
    name = Column(String)
    level = Column(String)
    code = Column(String)
    geom = Column(Geometry("MULTIPOLYGON"))

class Road(Base):
    __tablename__ = "roads"

    id = Column(String, primary_key=True)
    name = Column(String)
    type = Column(String)
    geom = Column(Geometry("LINESTRING"))


class Building(Base):
    __tablename__ = "buildings"

    id = Column(String, primary_key=True)
    type = Column(String)
    geom = Column(Geometry("POLYGON"))
