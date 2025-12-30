from fastapi import APIRouter
from app.services.toolkit_service import ToolkitService

router = APIRouter()
service = ToolkitService()

@router.post("/decide-tools")
def decide_tools(payload: dict):
    return service.decide_tools(payload["input"])