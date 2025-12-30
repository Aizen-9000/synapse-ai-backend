from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import get_settings

settings = get_settings()

# PostgreSQL
engine = create_engine(settings.DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# MongoDB
mongo_client = AsyncIOMotorClient(settings.MONGODB_URL)
mongo_db = mongo_client.get_default_database()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()