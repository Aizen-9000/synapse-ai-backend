class MultilingualStore:
    def __init__(self):
        self.store = {}

    def add_text(self, lang: str, key: str, text: str):
        self.store[(lang, key)] = text

    def get_text(self, lang: str, key: str):
        return self.store.get((lang, key))