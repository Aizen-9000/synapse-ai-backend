# app/routers/admin.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.crud import list_all_users, delete_user
from app.db.session import get_db

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = list_all_users(db)
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        for user in users
    ]


@router.delete("/user/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    result = delete_user(db, user_id)

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    return {"deleted": True, "user_id": user_id}