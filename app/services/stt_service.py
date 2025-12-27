from typing import BinaryIO
from app.adapters.stt_adapter import STTAdapter
from app.services.multilingual_service import MultilingualService

class STTService:
    def __init__(self):
        self.adapter = STTAdapter()
        self.lang_service = MultilingualService()

    def transcribe_audio(
        self,
        audio: BinaryIO,
        language: str | None = None
    ) -> dict:
        """
        Returns structured transcription result:
        {
          "text": "...",
          "language": "hi",
          "confidence": optional
        }
        """

        # 1. Determine language code to send to adapter
        lang_code = language if language else "auto"

        # 2. Transcribe using adapter
        text = self.adapter.transcribe(audio, lang_code)

        # 3. Detect actual language from text
        detected_lang = self.lang_service.detect_language(text)

        return {
            "text": text,
            "language": detected_lang
        }