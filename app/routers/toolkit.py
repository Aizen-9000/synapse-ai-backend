from fastapi import APIRouter
from app.services.toolkit_service import ToolkitService

router = APIRouter()
service = ToolkitService()

@router.post("/toolkit_action")
async def toolkit_action(action_name: str, params: dict):
    return {"result": service.perform_action(action_name, params)}