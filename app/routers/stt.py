# app/routers/stt.py

from fastapi import APIRouter, UploadFile, File

from app.services.stt_service import STTService
from app.adapters.stt_adapter import WhisperSTTAdapter

router = APIRouter()

adapter = WhisperSTTAdapter()
service = STTService(adapter)


@router.post("/stt")
async def speech_to_text(
    file: UploadFile = File(...),
    language: str | None = None
):
    audio_bytes = await file.read()
    text = await service.transcribe(audio_bytes, language)
    return {"text": text}