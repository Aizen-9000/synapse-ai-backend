class ToolkitService:
    def decide_tools(self, user_input: str) -> dict:
        # Example logic: return recommended tools based on input keywords
        tools = []
        if "image" in user_input.lower():
            tools.append("ImageGenerator")
        if "search" in user_input.lower():
            tools.append("WebSearch")
        return {"recommended_tools": tools}