from adapters.sync_adapter import SyncAdapter

class SyncEngineService:
    def __init__(self):
        self.adapter = SyncAdapter()

    def sync_data(self, user_id: str):
        return self.adapter.sync(user_id)

    def get_sync_status(self, user_id: str):
        return self.adapter.status(user_id)