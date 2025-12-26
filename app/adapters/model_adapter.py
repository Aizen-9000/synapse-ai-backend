# app/adapters/model_adapter.py

from app.config import settings
import requests
import openai

class ModelAdapter:
    def __init__(self):
        self.use_ollama = settings.USE_OLLAMA

        if settings.OPENAI_API_KEY:
            openai.api_key = settings.OPENAI_API_KEY

    def generate(self, prompt: str) -> str:
        if self.use_ollama:
            return self._ollama_generate(prompt)

        if settings.OPENAI_API_KEY:
            return self._openai_generate(prompt)

        if settings.GROQ_API_KEY:
            return self._grok_generate(prompt)

        raise RuntimeError("No AI provider configured")

    def _openai_generate(self, prompt: str) -> str:
        response = openai.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS_PER_REQUEST,
        )
        message = response.choices[0].message
        content = message.content
        if content is None:
            raise RuntimeError("OpenAI returned empty response content")
        return content
    def _ollama_generate(self, prompt: str) -> str:
        r = requests.post(
            f"{settings.OLLAMA_URL}/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        return r.json()["response"]

    def _grok_generate(self, prompt: str) -> str:
        # placeholder until Grok SDK stabilizes
        raise NotImplementedError("Grok integration pending")