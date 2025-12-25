from fastapi import APIRouter, UploadFile
from app.deps import crud
from app.utils import generate_id

router = APIRouter()

@router.post("/upload")
async def upload_file(user_id: str, file: UploadFile):
    file_data = {
        "id": generate_id(),
        "user_id": user_id,
        "filename": file.filename,
        "metadata": {"content_type": file.content_type}
    }
    saved_file = crud.save_file(file_data)
    return {"file_id": saved_file.id, "filename": saved_file.filename}