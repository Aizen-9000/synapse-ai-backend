from app.agents.base_agent import BaseAgent
from app.services.model_service import ModelService


class GenerationAgent(BaseAgent):
    name = "generation"

    def __init__(self, model_service: ModelService):
        self.model_service = model_service

    async def execute(self, payload: dict) -> dict:
        text = self.model_service.generate_response(
            payload["prompt"],
            temperature=payload.get("temperature", 0.7),
            max_tokens=payload.get("max_tokens", 2048),
            language=payload.get("language", "en"),
            context=payload.get("context"),
        )
        return {"output": text}