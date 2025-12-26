from fastapi import APIRouter
from app.services.multilingual_service import MultilingualService

router = APIRouter()
service = MultilingualService()

@router.post("/translate")
async def translate(text: str, target_lang: str):
    return {"translated": service.translate_text(text, target_lang)}

@router.post("/detect")
async def detect_language(text: str):
    return {"language": service.detect_language(text)}