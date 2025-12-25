from sqlalchemy import Column, String, JSON, DateTime
from .base import Base
from datetime import datetime

class Logs(Base):
    __tablename__ = "logs"

    id = Column(String, primary_key=True)
    user_id = Column(String)
    action = Column(String)
    details = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)