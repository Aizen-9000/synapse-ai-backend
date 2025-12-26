from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.services.chat_service import ChatService
from app.services.stt_service import STTService
from app.services.tts_service import TTSService
import os
import tempfile

router = APIRouter()
chat_service = ChatService()
stt_service = STTService()
tts_service = TTSService()

# -----------------------------
# Pydantic model for /text
# -----------------------------
class ChatRequest(BaseModel):
    message: str

# -----------------------------
# /text endpoint
# -----------------------------
@router.post("/text")
async def chat_text(request: ChatRequest):
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        reply = chat_service.generate_reply(request.message)
        return {"response": reply}

    except Exception as e:
        # Log the error in backend logs
        print(f"[ERROR] /text endpoint failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# /audio endpoint
# -----------------------------
@router.post("/audio")
async def chat_audio(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        # Use a temporary file safely
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
            temp_path = tmp.name
            tmp.write(await file.read())

        # Transcribe
        with open(temp_path, "rb") as audio_file:
            text = stt_service.transcribe_audio(audio_file)

        # Generate AI reply
        reply = chat_service.generate_reply(text)

        # Generate audio response
        audio_file_path = tts_service.synthesize_text(reply)

        # Clean up temp file
        os.remove(temp_path)

        return {
            "text": reply,
            "audio_file": audio_file_path
        }

    except Exception as e:
        print(f"[ERROR] /audio endpoint failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))