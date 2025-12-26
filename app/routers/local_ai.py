from fastapi import APIRouter
from app.services.local_ai_service import LocalAIService

router = APIRouter()
service = LocalAIService()

@router.post("/generate")
async def generate_response(prompt: str):
    return {"response": service.generate_response(prompt)}