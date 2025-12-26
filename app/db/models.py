from sqlalchemy import Column, Integer, String, Identity
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Identity(), primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)