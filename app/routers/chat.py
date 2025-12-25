from fastapi import APIRouter, UploadFile, File
from services.chat_service import ChatService
from services.stt_service import STTService
from services.tts_service import TTSService

router = APIRouter()
chat_service = ChatService()
stt_service = STTService()
tts_service = TTSService()

@router.post("/chat/text")
async def chat_text(prompt: str):
    return {"reply": chat_service.generate_reply(prompt)}

@router.post("/chat/audio")
async def chat_audio(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    text = stt_service.transcribe_audio(temp_path)
    reply = chat_service.generate_reply(text)
    audio_file = tts_service.synthesize_text(reply)
    return {"text": reply, "audio_file": audio_file}