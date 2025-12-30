import os
from app.security.encryption import generate_key


class KeyManager:
    def __init__(self):
        self.master_key = os.getenv("MASTER_ENCRYPTION_KEY", None)

    def get_user_key(self, user_id: str) -> bytes:
        if not self.master_key:
            return generate_key()
        return (self.master_key + user_id).encode()[:32]