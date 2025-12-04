from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langdetect import detect, DetectorFactory

from .llm import llm
from .stt import transcribe_bytes
from .tts import synthesize_elevenlabs
from .websearch import duckduckgo_search
from .translate import translate

DetectorFactory.seed = 0  # for consistent language detection

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str
    max_tokens: int | None = 512
    temperature: float | None = 0.7

@router.post("/generate")
async def generate_chat(req: ChatRequest):
    # detect input language
    try:
        detected_lang = detect(req.message)
    except:
        detected_lang = "en"

    # translate to English (LLM language) if needed
    if detected_lang != "en":
        prompt = await translate(req.message, "en")
    else:
        prompt = req.message

    resp_en = await llm.generate(prompt, max_tokens=req.max_tokens or 512, temperature=req.temperature or 0.7)

    # translate back to user language
    if detected_lang != "en":
        resp = await translate(resp_en, detected_lang)
    else:
        resp = resp_en

    return {"response": resp, "language": detected_lang}

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...), target_lang: str | None = None):
    data = await file.read()
    text = await transcribe_bytes(data)
    detected_lang = "en"
    try:
        detected_lang = detect(text)
    except:
        pass

    if target_lang and target_lang != detected_lang:
        text = await translate(text, target_lang)

    return {"text": text, "language": detected_lang}

@router.post("/tts")
async def tts(req: dict):
    text = req.get("text", "")
    lang = req.get("language", "en")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    audio = await synthesize_elevenlabs(text, voice=lang)
    if not audio:
        raise HTTPException(status_code=500, detail="TTS not available")
    return StreamingResponse(iter([audio]), media_type="audio/mpeg")

@router.get("/search")
async def search(q: str):
    results = await duckduckgo_search(q)
    return {"results": results}

@router.post("/translate")
async def translate_endpoint(req: dict):
    text = req.get("text")
    target = req.get("target_lang", "en")
    if not text:
        raise HTTPException(status_code=400, detail="No text")
    out = await translate(text, target)
    return {"translation": out}