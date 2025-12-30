class SystemAgentsAdapter:
    def __init__(self, agent_manager):
        self.manager = agent_manager

    async def run(self, agent_name: str, payload: dict) -> dict:
        return await self.manager.run(agent_name, payload)