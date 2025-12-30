class PrivacyGuard:
    @staticmethod
    def ensure_user_access(user_id: str, workspace_user_id: str):
        if user_id != workspace_user_id:
            raise PermissionError("Unauthorized data access")

    @staticmethod
    def enforce_memory_scope(user_id, workspace_id, memory_owner):
        if user_id != memory_owner:
            raise PermissionError("Memory isolation violation")