from fastapi import APIRouter, Request
from app.services.system_action_service import SystemActionService
from app.system_actions.platform_detector import detect_platform

router = APIRouter(prefix="/system")

service = SystemActionService()

@router.post("/action")
async def system_action(request: Request, action: str):
    platform = detect_platform(request.headers.get("user-agent"))
    return service.handle(action, platform)