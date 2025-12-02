from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    system: str | None = None
    language: str | None = None

class ChatResponse(BaseModel):
    reply: str

class STTResponse(BaseModel):
    text: str

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class TranslateResponse(BaseModel):
    translated: str