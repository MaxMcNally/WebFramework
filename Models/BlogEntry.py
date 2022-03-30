from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

# an example mapping using the base
class BlogEntry(Base):
    __tablename__ = 'blog_entries'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    date = Column(String)