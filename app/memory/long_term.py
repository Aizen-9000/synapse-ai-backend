from app.security.crypto_manager import CryptoManager


class LongTermMemory:
    def __init__(self):
        self.crypto = CryptoManager()
        self.store = {}

    def save(self, user_id: str, text: str):
        self.store[user_id] = self.crypto.encrypt_for_user(user_id, text)

    def load(self, user_id: str) -> str | None:
        if user_id not in self.store:
            return None
        return self.crypto.decrypt_for_user(user_id, self.store[user_id])