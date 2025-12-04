from .llm import llm

async def translate(text: str, target_lang: str) -> str:
    """
    Translate text to target language using LLM
    """
    return await llm.translate_text(text, target_lang)