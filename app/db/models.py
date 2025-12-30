from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class ChatMemory(Base):
    __tablename__ = "chat_memory"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    encrypted_content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class FileRecord(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    filename = Column(String)
    mime_type = Column(String)
    encrypted_blob = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)