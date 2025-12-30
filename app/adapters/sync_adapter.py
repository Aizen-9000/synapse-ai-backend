class SyncAdapter:
    def should_sync(self) -> bool:
        return True

    def sync_payload(self, payload: dict) -> dict:
        return payload