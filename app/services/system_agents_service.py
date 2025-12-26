from app.adapters.system_agents_adapter import SystemAgentsAdapter

class SystemAgentsService:
    def __init__(self):
        self.adapter = SystemAgentsAdapter()

    def execute_task(self, agent_id: str, task_data: dict):
        return self.adapter.run(agent_id, task_data)