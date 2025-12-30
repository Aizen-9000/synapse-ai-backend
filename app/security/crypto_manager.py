from app.security.encryption import encrypt, decrypt
from app.security.key_manager import KeyManager


class CryptoManager:
    def __init__(self):
        self.keys = KeyManager()

    def encrypt_for_user(self, user_id: str, text: str) -> dict:
        key = self.keys.get_user_key(user_id)
        return encrypt(text.encode(), key)

    def decrypt_for_user(self, user_id: str, payload: dict) -> str:
        key = self.keys.get_user_key(user_id)
        return decrypt(
            payload["ciphertext"],
            payload["nonce"],
            key
        ).decode()