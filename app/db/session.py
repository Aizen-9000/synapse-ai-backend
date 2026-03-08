# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

settings = get_settings()
engine = create_engine(settings.DATABASE_URL, future=True,   pool_pre_ping=True,  # << automatically checks if connection is alive
    pool_size=10,        # adjust based on your needs
    max_overflow=5,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()