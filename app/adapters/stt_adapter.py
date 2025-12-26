from typing import BinaryIO
import requests
from app.config import settings

class STTAdapter:
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.endpoint = "https://api.elevenlabs.io/v1/speech-to-text"

    def transcribe(self, audio: BinaryIO, language: str = "en") -> str:
        headers = {"xi-api-key": self.api_key}

        files = {
            "file": audio
        }

        data = {"language": language}

        response = requests.post(
            self.endpoint,
            headers=headers,
            files=files,
            data=data
        )
        response.raise_for_status()

        result = response.json()
        return result.get("text", "")