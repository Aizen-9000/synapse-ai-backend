from app.security.crypto_manager import CryptoManager

class TokenStore:
    def __init__(self):
        self.crypto = CryptoManager()

    def encrypt(self, user_id: str, token: str) -> dict:
        return self.crypto.encrypt_for_user(user_id, token)

    def decrypt(self, user_id: str, payload: dict) -> str:
        return self.crypto.decrypt_for_user(user_id, payload)