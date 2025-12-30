from app.agents.base_agent import BaseAgent


class AgentManager:
    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent):
        self._agents[agent.name] = agent

    async def run(self, agent_name: str, payload: dict) -> dict:
        if agent_name not in self._agents:
            raise ValueError(f"Agent '{agent_name}' not registered")
        return await self._agents[agent_name].execute(payload)

    def list_agents(self) -> list[str]:
        return list(self._agents.keys())