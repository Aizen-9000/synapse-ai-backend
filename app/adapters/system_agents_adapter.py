class SystemAgentsAdapter:
    def run(self, agent_id: str, task_data: dict):
        return f"Agent {agent_id} executed task with data {task_data}"