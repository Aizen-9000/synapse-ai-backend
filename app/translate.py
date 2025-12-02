from .llm import llm

async def translate(text: str, target_lang: str) -> str:
    # Try using LLM translate_text wrapper (uses configured provider)
    return await llm.translate_text(text, target_lang)