from abc import ABC, abstractmethod


class TTSAdapter(ABC):
    @abstractmethod
    async def synthesize(self, text: str, language: str ='en') -> bytes:
        pass
class CloudTTSAdapter(TTSAdapter):
    async def synthesize(self, text: str, language: str = 'en') -> bytes:
        # Example placeholder (11Labs / OpenAI / etc.)
        return b"CLOUD_TTS_AUDIO_BYTES"
class LocalTTSAdapter(TTSAdapter):
    async def synthesize(self, text: str, language: str ='en') -> bytes:
        # Example placeholder (Ollama / WhisperFlow / local engine)
        return b"LOCAL_TTS_AUDIO_BYTES"