from app.adapters.stt_adapter import STTAdapter

class STTService:
    def __init__(self):
        self.adapter = STTAdapter()

    def transcribe_audio(self, audio_file_path: str, language: str = "en") -> str:
        """
        Wrapper for STTAdapter to get transcription.
        """
        return self.adapter.transcribe(audio_file_path, language)