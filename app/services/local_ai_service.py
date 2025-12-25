from adapters.local_ai_adapter import LocalAIAdapter

class LocalAIService:
    def __init__(self):
        self.adapter = LocalAIAdapter()

    def generate_response(self, prompt: str, context: dict = None):
        return self.adapter.generate(prompt, context)