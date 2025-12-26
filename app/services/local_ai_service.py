from typing import Optional
from app.adapters.local_ai_adapter import LocalAIAdapter

class LocalAIService:
    def __init__(self):
        self.adapter = LocalAIAdapter()

    def generate_response(self, prompt: str, context: Optional[dict] = None):
        if context is None:
            context = {}
        return self.adapter.generate(prompt, context)