from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.crud import get_user, update_user_settings
from app.db.session import get_db

router = APIRouter()

@router.get("/{user_id}")
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.post("/{user_id}/settings")
def update_settings(
    user_id: int,
    settings: dict,
    db: Session = Depends(get_db)
):
    return update_user_settings(db, user_id, settings)