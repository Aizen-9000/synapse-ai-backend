import asyncio
import json
from typing import Optional

import httpx

from .config import settings

# This file implements one adapter that prefers:
# 1) LOCAL ollama (if USE_OLLAMA=True)
# 2) GROQ API (if GROQ_API_KEY set)
# 3) OpenAI API (if OPENAI_API_KEY set)
#
# It exposes async generate() and translate_text().

class LLMAdapter:
    def __init__(self):
        self.use_ollama = settings.USE_OLLAMA
        self.ollama_url = settings.OLLAMA_URL.rstrip("/")
        self.groq_key = settings.GROQ_API_KEY
        self.groq_model = settings.GROQ_MODEL
        self.openai_key = settings.OPENAI_API_KEY
        self.openai_model = settings.OPENAI_MODEL

    async def generate(self, prompt: str, max_tokens: int = 512, temperature: float = 0.7) -> str:
        if self.use_ollama:
            return await self._generate_ollama(prompt, max_tokens, temperature)
        if self.groq_key:
            return await self._generate_groq(prompt, max_tokens, temperature)
        if self.openai_key:
            return await self._generate_openai(prompt, max_tokens, temperature)
        return "[LLM ERROR] No LLM provider configured (set GROQ_API_KEY, OPENAI_API_KEY or USE_OLLAMA=True)."

    async def _generate_ollama(self, prompt: str, max_tokens: int, temperature: float) -> str:
        url = f"{self.ollama_url}/api/generate"
        payload = {"model": self.groq_model if self.groq_model else "llama", "prompt": prompt, "max_tokens": max_tokens, "temperature": temperature}
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(url, json=payload)
            if r.status_code != 200:
                return f"[OLLAMA ERROR] {r.status_code} {r.text}"
            # Ollama JSON response shape may vary — try a few keys
            try:
                data = r.json()
                if isinstance(data, dict):
                    # common: data["response"] or data.get("choices")...
                    if "response" in data:
                        return data["response"]
                    if "choices" in data:
                        c = data["choices"][0]
                        return c.get("message", {}).get("content") or c.get("text", "") or str(c)
                return str(data)
            except Exception as e:
                return f"[OLLAMA ERROR] parse error: {e}"

    async def _generate_groq(self, prompt: str, max_tokens: int, temperature: float) -> str:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.groq_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.groq_model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": False,
        }
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(url, json=payload, headers=headers)
            if r.status_code != 200:
                return f"[GROQ ERROR] {r.status_code} {r.text}"
            data = r.json()
            try:
                return data["choices"][0]["message"]["content"]
            except Exception:
                return str(data)

    async def _generate_openai(self, prompt: str, max_tokens: int, temperature: float) -> str:
        # Use OpenAI HTTP via official endpoint (openai python lib could be used)
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.openai_model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(url, json=payload, headers=headers)
            if r.status_code != 200:
                return f"[OPENAI ERROR] {r.status_code} {r.text}"
            data = r.json()
            try:
                return data["choices"][0]["message"]["content"]
            except Exception:
                return str(data)

    async def translate_text(self, text: str, target_lang: str) -> str:
        prompt = f"Translate the following text to {target_lang}:\n\n{text}"
        return await self.generate(prompt, max_tokens=400)


llm = LLMAdapter()