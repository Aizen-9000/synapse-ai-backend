from adapters.model_adapter import ModelAdapter

class ChatService:
    def __init__(self):
        self.adapter = ModelAdapter()

    def generate_reply(self, prompt: str):
        return self.adapter.generate_text(prompt)