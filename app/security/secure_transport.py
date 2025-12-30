from app.security.crypto_manager import CryptoManager


class SecureTransport:
    def __init__(self):
        self.crypto = CryptoManager()

    def inbound(self, user_id: str, encrypted_payload: dict) -> str:
        return self.crypto.decrypt_for_user(user_id, encrypted_payload)

    def outbound(self, user_id: str, plaintext: str) -> dict:
        return self.crypto.encrypt_for_user(user_id, plaintext)