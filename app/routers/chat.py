from fastapi import APIRouter, UploadFile, File
from app.services.chat_service import ChatService
from app.services.stt_service import STTService
from app.services.tts_service import TTSService

router = APIRouter()
chat_service = ChatService()
stt_service = STTService()
tts_service = TTSService()

@router.post("/text")
async def chat_text(prompt: str):
    return {"response": chat_service.generate_reply(prompt)}

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