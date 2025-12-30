from fastapi import APIRouter
from app.services.sync_service import SyncService
from app.adapters.sync_adapter import SyncAdapter

router = APIRouter()

sync_adapter = SyncAdapter()  # Permanent
service = SyncService(adapter=sync_adapter)

@router.post("/sync")
def sync_data(payload: dict):
    return service.sync(payload)