from app.adapters.system_agents_adapter import SystemAgentsAdapter


class AgentService:
    def __init__(self, adapter: SystemAgentsAdapter):
        self.adapter = adapter

    async def run_agent(self, agent_name: str, payload: dict) -> dict:
        return await self.adapter.run(agent_name, payload)