from typing import BinaryIO
from app.adapters.stt_adapter import STTAdapter

class STTService:
    def __init__(self):
        self.adapter = STTAdapter()

    def transcribe_audio(self, audio: BinaryIO, language: str = "en") -> str:
        return self.adapter.transcribe(audio, language)