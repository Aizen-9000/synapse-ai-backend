from app.security.privacy_guard import PrivacyGuard

class MemoryManager:
    def __init__(self, store):
        self.store = store

    def store_message(self, user_id, workspace_id, message):
        PrivacyGuard.ensure_user_access(user_id, workspace_id)

        self.store.save(
            user_id=user_id,
            workspace_id=workspace_id,
            content=message
        )

    def retrieve_context(self, user_id, workspace_id):
        PrivacyGuard.ensure_user_access(user_id, workspace_id)

        return self.store.fetch_recent(
            user_id=user_id,
            workspace_id=workspace_id
        )