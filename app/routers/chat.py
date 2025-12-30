from fastapi import APIRouter
from app.services.chat_service import ChatService
from app.adapters.model_adapter import ModelAdapter
from app.memory.memory_manager import MemoryManager

router = APIRouter()

adapter = ModelAdapter()  # Permanent multi-model adapter
memory = MemoryManager(None)  # Persistent memory store
service = ChatService(adapter, memory)

@router.post("/message")
def chat_message(payload: dict):
    user_id = payload["user_id"]
    workspace_id = payload.get("workspace_id", "default")
    message = payload["message"]
    response = service.generate_reply(user_id, workspace_id, message)
    return {"response": response}