from fastapi import APIRouter
from app.services.multilingual_service import MultilingualService
from app.adapters.multilingual_adapter import MultilingualAdapter

router = APIRouter()

adapter = MultilingualAdapter()  # Permanent concrete multilingual adapter
service = MultilingualService(adapter=adapter)

@router.post("/detect")
async def detect_language(text: str):
    return {"language": service.detect_language(text)}

@router.post("/translate")
async def translate(text: str, target_lang: str):
    source_lang = service.detect_language(text)
    translated = service.normalize(text, source_lang, target_lang)
    return {"translated": translated}