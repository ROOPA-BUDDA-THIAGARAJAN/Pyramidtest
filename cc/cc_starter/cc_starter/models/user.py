from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
    __tablename__ = 'user'
    email = Column(Text, primary_key=True)
    password = Column(Text)
   
