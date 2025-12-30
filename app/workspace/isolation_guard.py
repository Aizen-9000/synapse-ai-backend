class IsolationGuard:
    @staticmethod
    def enforce(user_id: str, workspace_user_id: str):
        if user_id != workspace_user_id:
            raise PermissionError("Workspace isolation violation")