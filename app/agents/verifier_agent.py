from app.agents.base_agent import BaseAgent
from app.intelligence.fact_checker import FactChecker


class VerifierAgent(BaseAgent):
    name = "verifier"

    def __init__(self, checker: FactChecker):
        self.checker = checker

    async def execute(self, payload: dict) -> dict:
        verified = self.checker.verify(payload["responses"])
        return {"verified": verified}