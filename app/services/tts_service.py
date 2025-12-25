from app.adapters.tts_adapter import TTSAdapter

class TTSService:
    def __init__(self):
        self.adapter = TTSAdapter()

    def synthesize_text(self, text: str, voice: str = "alloy", language: str = "en") -> bytes:
        """
        Wrapper for TTSAdapter to get audio bytes.
        """
        return self.adapter.synthesize(text, voice, language)