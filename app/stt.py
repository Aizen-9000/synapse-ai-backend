import io
from typing import Optional

import httpx
from .config import settings

async def transcribe_bytes(file_bytes: bytes) -> str:
    """
    If OPENAI_API_KEY present, call OpenAI whisper endpoint.
    Otherwise returns an error telling to configure STT.
    (You can extend to call Groq/other models if you have provider.)
    """
    if not settings.OPENAI_API_KEY:
        return "[STT ERROR] No OPENAI_API_KEY configured for Whisper transcription."

    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}"}
    # httpx multipart
    files = {"file": ("audio.wav", file_bytes, "audio/wav")}
    data = {"model": "whisper-1"}
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(url, headers=headers, data=data, files=files)
        if r.status_code != 200:
            return f"[STT ERROR] {r.status_code} {r.text}"
        j = r.json()
        return j.get("text", "")