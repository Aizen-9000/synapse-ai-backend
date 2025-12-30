class MultilingualStore:
    def normalize(self, text: str, lang: str) -> str:
        return f"[{lang}] {text}"