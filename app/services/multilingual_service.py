from app.adapters.multilingual_adapter import MultilingualAdapter

class MultilingualService:
    def __init__(self):
        self.adapter = MultilingualAdapter()

    def translate_text(self, text: str, target_lang: str):
        return self.adapter.translate(text, target_lang)

    def detect_language(self, text: str):
        return self.adapter.detect(text)