from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)