# app/session/session_manager.py

from app.session.device_fingerprint import fingerprint
from app.session.token_store import TokenStore


class SessionManager:
    def __init__(self, db):
        self.db = db
        self.store = TokenStore()

    def create_session(
        self,
        user_id: str,
        device_info: str,
        refresh_token: str
    ):
        device_id = fingerprint(device_info)

        # ✅ FIX: pass user_id explicitly
        encrypted = self.store.encrypt(user_id, refresh_token)

        self.db.execute(
            """
            INSERT INTO sessions (device_id, user_id, refresh_token)
            VALUES (:d, :u, :t)
            """,
            {
                "d": device_id,
                "u": user_id,
                "t": encrypted
            }
        )

    def restore_session(self, device_info: str):
        device_id = fingerprint(device_info)
        return self.db.fetch_one(
            "SELECT * FROM sessions WHERE device_id = :d",
            {"d": device_id}
        )