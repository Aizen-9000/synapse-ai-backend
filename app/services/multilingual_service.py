from app.adapters.multilingual_adapter import MultilingualAdapter

class MultilingualService:
    def __init__(self, adapter: MultilingualAdapter):
        self.adapter = adapter

    def detect_language(self, text: str) -> str:
        return self.adapter.detect_language(text)

    def normalize(self, text: str, source_lang: str, target_lang: str) -> str:
        if source_lang == target_lang:
            return text
        return self.adapter.normalize(text, source_lang, target_lang)