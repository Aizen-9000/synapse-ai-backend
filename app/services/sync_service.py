from app.adapters.sync_adapter import SyncAdapter


class SyncService:
    def __init__(self, adapter: SyncAdapter):
        self.adapter = adapter

    def sync(self, payload: dict) -> dict:
        if self.adapter.should_sync():
            return self.adapter.sync_payload(payload)
        return payload