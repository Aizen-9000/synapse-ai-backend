from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import STTService

router = APIRouter()
service = STTService()

@router.post("/stt")
async def transcribe(file: UploadFile = File(...), language: str = "en"):
    result = service.transcribe_audio(file.file, language)
    return {"text": result}