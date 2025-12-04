import httpx
from .config import settings

async def synthesize_elevenlabs(text: str, voice: str = "alloy") -> bytes:
    if not settings.ELEVENLABS_API_KEY:
        return b""
    
    # ElevenLabs voice mapping: can pass language codes
    voice_map = {
        "en": "alloy",
        "hi": "hindi",
        "es": "spanish",
        "fr": "french",
        "bn": "bengali"
    }
    voice_id = voice_map.get(voice[:2].lower(), "alloy")
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": settings.ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    payload = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}

    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(url, json=payload, headers=headers)
        if r.status_code == 200:
            return r.content
    return b""