from fastapi import APIRouter, HTTPException
from app.deps import crud
from app.utils import generate_id

router = APIRouter()

@router.post("/signup")
def signup(username: str, email: str):
    user = crud.create_user({"id": generate_id(), "username": username, "email": email})
    return {"user_id": user.id, "username": user.username}

@router.post("/login")
def login(username: str):
    # Simulated login
    user = crud.get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Welcome {username}"}