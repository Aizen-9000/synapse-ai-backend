import openai
from app.config import settings

class ModelAdapter:
    def __init__(self):
        openai.api_key = settings.GPT_API_KEY

    def generate_text(self, prompt: str, max_tokens: int = 512):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()