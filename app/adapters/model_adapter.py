from app.config import get_settings

settings = get_settings()


class BaseModel:
    def generate(
        self,
        prompt: str,
        *,
        context: list | None = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        language: str = "en",
    ) -> str:
        raise NotImplementedError


class OllamaModel(BaseModel):
    def generate(
        self,
        prompt: str,
        *,
        context: list | None = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        language: str = "en",
    ) -> str:
        # Offline-safe default
        return f"[Ollama:{settings.OLLAMA_DEFAULT_MODEL}] {prompt}"


class ModelAdapter:
    def __init__(self):
        self.models: list[BaseModel] = []
        self._load_models()

    def _load_models(self):
        # Always have at least one offline-safe model
        self.models.append(OllamaModel())

        # Cloud models plug in here later
        # if settings.OPENAI_API_KEY:
        #     self.models.append(OpenAIModel())

    def generate(
        self,
        prompt: str,
        *,
        context: list | None = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        language: str = "en",
    ) -> str:
        if not self.models:
            return "No models available"

        return self.models[0].generate(
            prompt,
            context=context,
            temperature=temperature,
            max_tokens=max_tokens,
            language=language,
        )