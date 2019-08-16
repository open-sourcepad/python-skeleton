from sqlalchemy import Column, String, Integer, DATETIME
from .base import BaseModel, BaseDeclaration

class User(BaseModel, BaseDeclaration):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    createdAt = Column(DATETIME)
