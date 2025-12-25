from fastapi import APIRouter
from app.deps import crud

router = APIRouter()

@router.get("/{user_id}")
def get_user(user_id: str):
    user = crud.get_user(user_id)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "username": user.username, "settings": user.settings}