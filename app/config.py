import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Core settings
    APP_NAME: str = "Synapse AI"
    DEBUG: bool = True
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./synapse.db")
    VECTOR_STORE_PATH: str = os.getenv("VECTOR_STORE_PATH", "./vector_store/faiss.index")
    MAX_FREE_TOKENS: int = int(os.getenv("MAX_FREE_TOKENS", 1000))
    MAX_HISTORY: int = int(os.getenv("MAX_HISTORY", 20))
    MAX_TOKENS_PER_REQUEST: int = int(os.getenv("MAX_TOKENS_PER_REQUEST", 2000))
    SYSTEM_MEMORY_LIMIT: int = int(os.getenv("SYSTEM_MEMORY_LIMIT", 2048))
    UPLOAD_DIRS: str = os.getenv("UPLOAD_DIRS", "./uploads")
    VECTOR_DIM: int = int(os.getenv("VECTOR_DIM", 1536))

    # Server / Auth
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    MODE: str = os.getenv("MODE", "production")

    # AI / Model Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    GROK_API_KEY: str = os.getenv("GROK_API_KEY", "")
    GROK_MODEL: str = os.getenv("GROK_MODEL", "grok-1")
    HF_API_KEY: str = os.getenv("HF_API_KEY", "")
    USE_OLLAMA: bool = os.getenv("USE_OLLAMA", "True") == "True"
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")

    # TTS / STT
    STT_API_KEY: str = os.getenv("STT_API_KEY", "")
    TTS_API_KEY: str = os.getenv("TTS_API_KEY", "")
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
    VOSK_MODEL_PATH: str = os.getenv("VOSK_MODEL_PATH", "./models/vosk-model-small")

    # Feature flags
    ENABLE_RAG: bool = os.getenv("ENABLE_RAG", "True") == "True"
    ENABLE_TOOLS: bool = os.getenv("ENABLE_TOOLS", "True") == "True"
    ALLOW_UNLIMITED_TOKENS: bool = os.getenv("ALLOW_UNLIMITED_TOKENS", "False") == "True"

settings = Settings()