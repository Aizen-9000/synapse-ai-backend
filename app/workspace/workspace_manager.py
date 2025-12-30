import uuid
from app.workspace.defaults import DEFAULT_THEME, DEFAULT_LAYOUT, DEFAULT_MODULES
from app.workspace.isolation_guard import IsolationGuard

class WorkspaceManager:
    def __init__(self, db):
        self.db = db

    def create_workspace(self, user_id: str):
        workspace_id = str(uuid.uuid4())

        self.db.execute(
            "INSERT INTO workspaces (id, user_id) VALUES (:id, :user_id)",
            {"id": workspace_id, "user_id": user_id}
        )

        self.db.execute(
            """
            INSERT INTO ui_configs (workspace_id, layout, theme, modules)
            VALUES (:wid, :layout, :theme, :modules)
            """,
            {
                "wid": workspace_id,
                "layout": DEFAULT_LAYOUT,
                "theme": DEFAULT_THEME,
                "modules": DEFAULT_MODULES
            }
        )

        return workspace_id

    def load_workspace(self, user_id: str, workspace_id: str):
        ws = self.db.fetch_one(
            "SELECT * FROM workspaces WHERE id=:id",
            {"id": workspace_id}
        )

        IsolationGuard.enforce(user_id, ws["user_id"])
        return ws