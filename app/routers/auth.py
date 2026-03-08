from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from datetime import datetime, timedelta
from jose import jwt

from app.db.crud import create_user, authenticate_user
from app.db.session import get_db

router = APIRouter()

# JWT CONFIG
SECRET_KEY = "CHANGE_THIS_TO_A_LONG_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    """
    Create a JWT token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return encoded_jwt


@router.post("/register")
def register_user(payload: dict, db: Session = Depends(get_db)):
    username = payload.get("username")
    password = payload.get("password")
    email = payload.get("email")

    if not username or not password:
        raise HTTPException(
            status_code=400,
            detail="Username and password required"
        )

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
        raise HTTPException(
            status_code=400,
            detail="Username and password required"
        )

    user = authenticate_user(
        db=db,
        username=username,
        password=password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # Create JWT token
    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }