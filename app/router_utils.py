from fastapi import APIRouter

router = APIRouter(prefix="/utils")

@router.get("/health")
async def health():
    return {"status": "ok"}