from fastapi import APIRouter
from services.sync_engine_service import SyncEngineService

router = APIRouter()
service = SyncEngineService()

@router.get("/sync/{user_id}")
async def sync(user_id: str):
    return {"status": service.sync_data(user_id)}

@router.get("/sync_status/{user_id}")
async def sync_status(user_id: str):
    return {"status": service.get_sync_status(user_id)}