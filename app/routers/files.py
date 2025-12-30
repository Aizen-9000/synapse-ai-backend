from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    return {
        "filename": file.filename,
        "size": len(content),
        "status": "received",
        "content_type": file.content_type
    }