# app/db/crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.db import models
from app.security.encryption import verify_password, get_password_hash


# -----------------------------
# CHAT MEMORY
# -----------------------------
def save_chat_memory(db: Session, user_id: int, encrypted_content: str):
    memory = models.ChatMemory(
        user_id=user_id,
        encrypted_content=encrypted_content
    )
    db.add(memory)
    db.commit()
    db.refresh(memory)
    return memory


# -----------------------------
# ADMIN OPERATIONS
# -----------------------------
def list_all_users(db: Session):
    """Return all users in the system."""
    return db.query(models.User).all()


def delete_user(db: Session, user_id: int):
    """Delete a user by their ID."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return True


# -----------------------------
# AUTHENTICATION OPERATIONS
# -----------------------------
def create_user(db: Session, username: str, password: str, email: str | None = None):
    """Create a new user and store a hashed password."""
    hashed_password = get_password_hash(password)
    user = models.User(username=username, hashed_password=hashed_password, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str):
    """Authenticate a user by verifying their password."""
    try:
        user = db.query(models.User).filter(models.User.username == username).one()
    except NoResultFound:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
# -----------------------------
# USER OPERATIONS
# -----------------------------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user_settings(db: Session, user_id: int, settings: dict):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None

    # assuming User has a JSON or dict-like `settings` column
    user.settings = settings
    db.commit()
    db.refresh(user)
    return user