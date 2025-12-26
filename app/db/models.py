from sqlalchemy import Column, Integer, String, Identity
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        Identity(always=True),
        primary_key=True,
        index=True
    )

    username = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)