from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "Synapse AI Backend Running"}