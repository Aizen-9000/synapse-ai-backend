from app.agents.base_agent import BaseAgent
from app.intelligence.consensus_engine import ConsensusEngine


class ConsensusAgent(BaseAgent):
    name = "consensus"

    def __init__(self, engine: ConsensusEngine):
        self.engine = engine

    async def execute(self, payload: dict) -> dict:
        best = self.engine.select_best(payload["verified"])
        return {"best": best}