from sqlalchemy import Column, String, Boolean
from .base import Base

class FeatureFlags(Base):
    __tablename__ = "feature_flags"

    feature_name = Column(String, primary_key=True)
    enabled = Column(Boolean, default=True)