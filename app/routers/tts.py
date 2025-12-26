from fastapi import APIRouter
from app.services.tts_service import TTSService

router = APIRouter()
service = TTSService()

@router.post("/tts")
async def synthesize(text: str, language: str = "en", voice: str = "default"):
    result = service.synthesize_text(text, language, voice)
    return {"audio": result}