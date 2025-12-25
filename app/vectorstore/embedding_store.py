class EmbeddingStore:
    def __init__(self):
        self.store = {}

    def add_embedding(self, key, embedding):
        self.store[key] = embedding

    def get_embedding(self, key):
        return self.store.get(key)