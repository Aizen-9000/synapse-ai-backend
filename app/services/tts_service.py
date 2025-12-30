from app.adapters.tts_adapter import TTSAdapter

class TTSService:
    def __init__(self, adapter: TTSAdapter):
        self.adapter = adapter

    async def synthesize(self, text: str, language: str = "en") -> bytes:
        return await self.adapter.synthesize(text, language)