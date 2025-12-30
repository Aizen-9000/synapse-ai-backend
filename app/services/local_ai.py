class LocalAIService:
    def __init__(self, ollama_controller):
        self.ollama = ollama_controller

    def generate(self, prompt: str, offline: bool = True) -> str:
        if offline:
            return self.ollama.run(prompt)
        return "Offline AI not enabled"