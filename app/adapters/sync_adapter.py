class SyncAdapter:
    def sync(self, user_id: str):
        return f"Data synced for {user_id}"

    def status(self, user_id: str):
        return "Completed"