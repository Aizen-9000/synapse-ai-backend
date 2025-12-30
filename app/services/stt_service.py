from app.adapters.stt_adapter import STTAdapter

class STTService:
    def __init__(self, adapter: STTAdapter):
        self.adapter = adapter

    async def transcribe(self, audio_bytes: bytes, language: str | None = None) -> str:
        return await self.adapter.transcribe(audio_bytes, language)