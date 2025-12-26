from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.chat_service import ChatService
from app.services.stt_service import STTService
from app.services.tts_service import TTSService

router = APIRouter()
chat_service = ChatService()
stt_service = STTService()
tts_service = TTSService()

# -----------------------------
# Request body model for text chat
# -----------------------------
class ChatRequest(BaseModel):
    message: str

@router.post("/text")
async def chat_text(request: ChatRequest):
    """
    Expects JSON body like: { "message": "Hello" }
    """
    reply = chat_service.generate_reply(request.message)
    return {"response": reply}

@router.post("/audio")
async def chat_audio(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"

    with open(temp_path, "wb") as f:
        f.write(await file.read())

    with open(temp_path, "rb") as audio_file:
        text = stt_service.transcribe_audio(audio_file)

    reply = chat_service.generate_reply(text)
    audio_file_path = tts_service.synthesize_text(reply)

    return {
        "text": reply,
        "audio_file": audio_file_path
    }