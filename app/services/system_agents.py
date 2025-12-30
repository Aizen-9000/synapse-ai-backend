# app/services/system_agents.py

from app.agents.agent_manager import AgentManager


class SystemAgentsService:
    def __init__(self, manager: AgentManager | None = None):
        self.manager = manager or AgentManager()

    async def act(self, agent_name: str, message: str) -> dict:
        """
        Executes a registered agent with a standard payload.
        """
        payload = {
            "message": message
        }
        return await self.manager.run(agent_name, payload)

    def list_agents(self) -> list[str]:
        return self.manager.list_agents()