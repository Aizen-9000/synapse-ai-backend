class ToolkitService:
    def perform_action(self, action_name: str, params: dict):
        # Add more tools as needed
        if action_name == "calculate":
            return eval(params.get("expression", "0"))
        elif action_name == "format_text":
            return str(params.get("text", "")).upper()
        return None