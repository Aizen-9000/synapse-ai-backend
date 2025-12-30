from fastapi import APIRouter
from app.services.tts_service import TTSService
from app.adapters.tts_adapter import TTSAdapter, LocalTTSAdapter

router = APIRouter()

# Instantiate a real adapter (offline-safe default)
adapter: TTSAdapter = LocalTTSAdapter()
service = TTSService(adapter)


@router.post("/tts")
async def text_to_speech(payload: dict):
    audio_bytes = await service.synthesize(
        payload["text"],
        payload.get("language", "en")
    )
    return {"audio": audio_bytes}