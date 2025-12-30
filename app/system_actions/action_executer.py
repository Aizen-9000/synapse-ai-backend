from .action_types import ActionScope

class ActionExecutor:
    def execute(self, action: str) -> bool:
        # App-level actions only
        if action == "clear_cache":
            return True
        if action == "reset_app":
            return True
        if action == "export_data":
            return True

        return False