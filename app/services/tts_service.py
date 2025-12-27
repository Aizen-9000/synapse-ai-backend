from app.adapters.tts_adapter import TTSAdapter

# Mapping: language code → recommended ElevenLabs voice
VOICE_MAP = {
    "en": "alloy",
    "hi": "hindi_male",
    "bn": "bengali_female",
    "es": "spanish_female",
    "fr": "french_male",
    # add more supported languages here
}

class TTSService:
    def __init__(self):
        self.adapter = TTSAdapter()

    def synthesize_text(
        self, 
        text: str, 
        voice: str | None = None, 
        language: str | None = "en"
    ) -> bytes:
        """
        Synthesize text into audio bytes using language-appropriate voice.
        """

        # Ensure language is a string and fallback to 'en'
        language_str: str = language if language else "en"

        # Determine correct voice, fallback to 'alloy'
        voice_str: str = voice if voice else VOICE_MAP.get(language_str, "alloy")

        # Call adapter safely
        return self.adapter.synthesize(text, voice_str, language_str)