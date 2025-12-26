# app/adapters/model_adapter.py

from app.config import settings
import requests
import openai

class ModelAdapter:
    def __init__(self):
        self.use_ollama = settings.USE_OLLAMA

        if settings.OPENAI_API_KEY:
            openai.api_key = settings.OPENAI_API_KEY

    # ✅ SINGLE public entry point
    def generate_text(self, prompt: str) -> str:
        if self.use_ollama:
            return self._ollama_generate(prompt)

        if settings.OPENAI_API_KEY:
            return self._openai_generate(prompt)

        if settings.GROK_API_KEY:
            return self._grok_generate(prompt)

        raise RuntimeError("No AI provider configured")

    # -------- Providers --------

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
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        r.raise_for_status()

        result = r.json().get("response")
        if not result:
            raise RuntimeError("Ollama returned empty response")

        return result

    def _grok_generate(self, prompt: str) -> str:
        raise NotImplementedError("Grok integration pending")