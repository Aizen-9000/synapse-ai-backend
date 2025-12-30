from app.agents.base_agent import BaseAgent
from app.agents.agent_manager import AgentManager


class OrchestratorAgent(BaseAgent):
    name = "orchestrator"

    def __init__(self, manager: AgentManager):
        self.manager = manager

    async def execute(self, payload: dict) -> dict:
        responses = await self.manager.run("comparison", payload)
        verified = await self.manager.run("verifier", responses)
        best = await self.manager.run("consensus", verified)
        mixed = await self.manager.run("mixer", verified)

        return {
            "best": best["best"],
            "mixed": mixed["mixed"],
            "all": responses["responses"],
        }