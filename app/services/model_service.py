from app.adapters.model_adapter import ModelAdapter


class ModelService:
    def __init__(self, adapter: ModelAdapter):
        self.adapter = adapter

    def generate_response(
        self,
        prompt: str,
        *,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        language: str = "en",
        context: list | None = None,
    ) -> str:
        return self.adapter.generate(
            prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            language=language,
            context=context or []
        )