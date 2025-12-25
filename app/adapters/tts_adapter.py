import requests
from app.config import settings

class TTSAdapter:
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.endpoint = "https://api.elevenlabs.io/v1/text-to-speech"

    def synthesize(self, text: str, voice: str = "alloy", language: str = "en") -> bytes:
        """
        Converts text to speech using 11Labs TTS API.
        Returns raw audio bytes.
        """
        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice": voice,
            "language": language,
            "format": "mp3"
        }

        response = requests.post(self.endpoint, headers=headers, json=payload)
        response.raise_for_status()

        return response.content