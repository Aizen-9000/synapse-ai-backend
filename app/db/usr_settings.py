from sqlalchemy import Column, String, JSON
from .base import Base

class UserSettings(Base):
    __tablename__ = "user_settings"

    user_id = Column(String, primary_key=True)
    settings = Column(JSON)