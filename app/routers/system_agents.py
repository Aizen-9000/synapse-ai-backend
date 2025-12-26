from fastapi import APIRouter
from app.services.system_agents_service import SystemAgentsService

router = APIRouter()
service = SystemAgentsService()

@router.post("/execute_task")
async def execute_task(agent_id: str, task_data: dict):
    return {"result": service.execute_task(agent_id, task_data)}