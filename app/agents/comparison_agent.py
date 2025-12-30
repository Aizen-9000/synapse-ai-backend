from app.agents.base_agent import BaseAgent
from app.services.model_service import ModelService


class ComparisonAgent(BaseAgent):
    name = "comparison"

    def __init__(self, services: dict[str, ModelService]):
        self.services = services

    async def execute(self, payload: dict) -> dict:
        prompt = payload["prompt"]
        results = {}

        for model_name, service in self.services.items():
            results[model_name] = service.generate_response(prompt)

        return {"responses": results}