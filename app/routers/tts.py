from fastapi import APIRouter
from services.tts_service import TTSService

router = APIRouter()
service = TTSService()

@router.post("/tts")
async def synthesize(text: str, language: str = "en", voice: str = "default"):
    result = service.synthesize_speech(text, language, voice)
    return {"audio": result}