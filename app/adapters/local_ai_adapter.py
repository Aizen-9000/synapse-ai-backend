class LocalAIAdapter:
    def __init__(self, ollama_controller):
        self.ollama = ollama_controller

    def generate(self, prompt: str) -> str:
        return self.ollama.run(prompt)