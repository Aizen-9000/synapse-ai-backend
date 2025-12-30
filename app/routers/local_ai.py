from fastapi import APIRouter
from app.services.local_ai import LocalAIService
from app.runtime.ollama_controller import OllamaController

router = APIRouter()
ollama = OllamaController()
service = LocalAIService(ollama)

@router.post("/offline-message")
def offline_message(payload: dict):
    text = payload["message"]
    offline = payload.get("offline", True)
    return {"response": service.generate(text, offline)}