# app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.crud import create_user, authenticate_user
from app.db.session import get_db

router = APIRouter()


@router.post("/register")
def register_user(payload: dict, db: Session = Depends(get_db)):
    username = payload.get("username")
    password = payload.get("password")
    email = payload.get("email")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password required")

    user = create_user(
        db=db,
        username=username,
        password=password,
        email=email,
    )

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }


@router.post("/login")
def login_user(payload: dict, db: Session = Depends(get_db)):
    username = payload.get("username")
    password = payload.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password required")

    user = authenticate_user(
        db=db,
        username=username,
        password=password,
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "authenticated": True,
        "user_id": user.id,
        "username": user.username,
    }