from abc import ABC, abstractmethod

class STTAdapter(ABC):
    @abstractmethod
    async def transcribe(self, audio_bytes: bytes, language: str | None) -> str:
        pass
# app/adapters/whisper_stt_adapter.py

from app.adapters.stt_adapter import STTAdapter

class WhisperSTTAdapter(STTAdapter):
    async def transcribe(
        self,
        audio_bytes: bytes,
        language: str | None
    ) -> str:
        # Placeholder for Whisper / WhisperFlow / API
        return "Transcription not implemented yet"