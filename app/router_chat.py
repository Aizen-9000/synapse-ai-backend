from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langdetect import detect, DetectorFactory

from .llm import llm
from .stt import transcribe_bytes
from .tts import synthesize_elevenlabs
from .websearch import duckduckgo_search
from .translate import translate

DetectorFactory.seed = 0  # consistent detection

router = APIRouter(prefix="/chat")


# ----------------------------------------------------
# Utility: Normalize Bengali transliteration → Bengali
# ----------------------------------------------------
async def force_bengali_script(text: str) -> str:
    """
    Whisper frequently outputs Bengali as English letters.
    This forces proper Bengali Unicode using translation model.
    """
    # If text already contains Bengali characters, skip
    if any("\u0980" <= c <= "\u09FF" for c in text):
        return text

    # If it's English-like but detected as bn, translate
    try:
        lang = detect(text)
    except:
        lang = "en"

    if lang == "bn":
        return await translate(text, "bn")

    return text


# -------------------------------
# Chat request model
# -------------------------------
class ChatRequest(BaseModel):
    message: str
    max_tokens: int | None = 512
    temperature: float | None = 0.7


# -------------------------------
# CHAT COMPLETION
# -------------------------------
@router.post("/generate")
async def generate_chat(req: ChatRequest):
    msg = await force_bengali_script(req.message)

    # detect language reliably
    try:
        detected = detect(msg)
    except:
        detected = "en"

    user_lang = detected

    # ALWAYS translate to English for the LLM
    if user_lang != "en":
        english_prompt = await translate(msg, "en")
    else:
        english_prompt = msg

    # Generate response in English
    resp_en = await llm.generate(
        english_prompt,
        max_tokens=req.max_tokens or 512,
        temperature=req.temperature or 0.7,
    )

    # Convert back to user language
    if user_lang != "en":
        final_resp = await translate(resp_en, user_lang)
    else:
        final_resp = resp_en

    return {"response": final_resp, "language": user_lang}


# -------------------------------
# SPEECH-TO-TEXT (Whisper)
# -------------------------------
@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...), target_lang: str | None = None):
    data = await file.read()
    text = await transcribe_bytes(data)

    # Clean Whisper transliteration
    text = await force_bengali_script(text)

    try:
        detected = detect(text)
    except:
        detected = "en"

    # Translate only if user requested specific output
    if target_lang and target_lang != detected:
        text = await translate(text, target_lang)

    return {"text": text, "language": detected}


# -------------------------------
# TEXT-TO-SPEECH
# -------------------------------
@router.post("/tts")
async def tts(req: dict):
    text = req.get("text", "")
    lang = req.get("language", "en")

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    text = await force_bengali_script(text)

    audio = await synthesize_elevenlabs(text, voice=lang)
    if not audio:
        raise HTTPException(status_code=500, detail="TTS not available")

    return StreamingResponse(iter([audio]), media_type="audio/mpeg")


# -------------------------------
# SEARCH
# -------------------------------
@router.get("/search")
async def search(q: str):
    results = await duckduckgo_search(q)
    return {"results": results}


# -------------------------------
# TRANSLATE ENDPOINT
# -------------------------------
@router.post("/translate")
async def translate_endpoint(req: dict):
    text = req.get("text")
    target = req.get("target_lang", "en")

    if not text:
        raise HTTPException(status_code=400, detail="No text")

    text = await force_bengali_script(text)
    out = await translate(text, target)

    return {"translation": out}