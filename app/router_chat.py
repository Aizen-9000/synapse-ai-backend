from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langdetect import detect, DetectorFactory

from .llm import llm
from .stt import transcribe_bytes
from .tts import synthesize_elevenlabs
from .websearch import duckduckgo_search
from .translate import translate

DetectorFactory.seed = 0  # consistent language detection

router = APIRouter(prefix="/chat")


# -------------------------------
# Utility: Force proper script for Indian languages
# -------------------------------
async def fix_indian_script(text: str, lang: str) -> str:
    indian_scripts = {
        "bn": ("\u0980", "\u09FF"),
        "hi": ("\u0900", "\u097F"),
        "ta": ("\u0B80", "\u0BFF"),
        "te": ("\u0C00", "\u0C7F"),
        "ml": ("\u0D00", "\u0D7F"),
        "kn": ("\u0C80", "\u0CFF"),
        "gu": ("\u0A80", "\u0AFF"),
        "mr": ("\u0900", "\u097F"),
        "or": ("\u0B00", "\u0B7F"),
        "as": ("\u0980", "\u09FF"),
        "pa": ("\u0A00", "\u0A7F"),
    }

    if lang in indian_scripts:
        start, end = indian_scripts[lang]
        if not any(start <= c <= end for c in text):
            text = await translate(text, lang)

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
PROMPT_HINT = """You are a multilingual assistant.
Always respond in the same language as the user input.
If the language is low-resource or rare, do your best to respond in that language.
You can use proper script for Indian languages even if input is transliterated."""

@router.post("/generate")
async def generate_chat(req: ChatRequest):
    # detect language
    try:
        user_lang = detect(req.message)
    except:
        user_lang = "en"

    # fix Indian script if needed
    msg = await fix_indian_script(req.message, user_lang)

    # create prompt for LLM with hint
    if user_lang != "en":
        english_prompt = await translate(msg, "en")
    else:
        english_prompt = msg

    llm_prompt = f"{PROMPT_HINT}\nUser: {msg}\nAI:"

    # Generate response
    resp_en = await llm.generate(
        llm_prompt, max_tokens=req.max_tokens or 512, temperature=req.temperature or 0.7
    )

    # translate back to user language if needed
    if user_lang != "en":
        final_resp = await translate(resp_en, user_lang)
        final_resp = await fix_indian_script(final_resp, user_lang)
    else:
        final_resp = resp_en

    return {"response": final_resp, "language": user_lang}


# -------------------------------
# SPEECH-TO-TEXT
# -------------------------------
@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...), target_lang: str | None = None):
    data = await file.read()
    text = await transcribe_bytes(data)

    try:
        detected_lang = detect(text)
    except:
        detected_lang = "en"

    text = await fix_indian_script(text, detected_lang)

    if target_lang and target_lang != detected_lang:
        text = await translate(text, target_lang)

    return {"text": text, "language": detected_lang}


# -------------------------------
# TEXT-TO-SPEECH
# -------------------------------
@router.post("/tts")
async def tts(req: dict):
    text = req.get("text", "")
    lang = req.get("language", "en")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    text = await fix_indian_script(text, lang)
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

    try:
        detected_lang = detect(text)
    except:
        detected_lang = "en"

    text = await fix_indian_script(text, detected_lang)
    out = await translate(text, target)
    return {"translation": out}