class MultilingualAdapter:
    def normalize(self, text: str, source_lang: str, target_lang: str) -> str:
        if source_lang == target_lang:
            return text
        # Placeholder normalization logic
        return f"[{target_lang}] {text}"

    def detect_language(self, text: str) -> str:
        # Very basic heuristic
        if any(ord(c) > 127 for c in text):
            return "non-en"
        return "en"