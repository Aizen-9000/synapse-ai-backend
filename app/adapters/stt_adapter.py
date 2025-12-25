import requests
from app.config import settings

class STTAdapter:
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.endpoint = "https://api.elevenlabs.io/v1/speech-to-text"

    def transcribe(self, audio_file_path: str, language: str = "en"):
        """
        Sends audio to 11Labs STT API and returns transcribed text.
        Supports multilingual transcription based on `language`.
        """
        headers = {"xi-api-key": self.api_key}
        files = {"file": open(audio_file_path, "rb")}

        # Optional: set language in params if API supports it
        data = {"language": language}

        response = requests.post(self.endpoint, headers=headers, files=files, data=data)
        response.raise_for_status()  # Raises exception if API fails

        result = response.json()
        # Assuming API returns {"text": "transcribed text"}
        return result.get("text", "")