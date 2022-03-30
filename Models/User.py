from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

# an example mapping using the base
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    date = Column(String)