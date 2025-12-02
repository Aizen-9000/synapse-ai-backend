from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel

from .llm import llm
from .stt import transcribe_bytes
from .tts import synthesize_elevenlabs
from .websearch import duckduckgo_search
from .translate import translate

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str
    max_tokens: int | None = 512
    temperature: float | None = 0.7

@router.post("/generate")
async def generate_chat(req: ChatRequest):
    resp = await llm.generate(req.message, max_tokens=req.max_tokens or 512, temperature=req.temperature or 0.7)
    return {"response": resp}

@router.post("/stream")
async def stream_chat(req: ChatRequest):
    """
    Very simple streaming endpoint (non-llm streaming).
    For providers that support SSE/stream, you'd need to implement streaming per-provider.
    Here we do a simple generator that yields the output in one chunk.
    """
    async def generator():
        text = await llm.generate(req.message, max_tokens=req.max_tokens or 512, temperature=req.temperature or 0.7)
        yield text
    return StreamingResponse(generator(), media_type="text/plain")

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    data = await file.read()
    text = await transcribe_bytes(data)
    return {"text": text}

@router.post("/tts")
async def tts(req: dict):
    text = req.get("text", "")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    audio = await synthesize_elevenlabs(text)
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