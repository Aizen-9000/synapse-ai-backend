from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # App Core
    # =========================
    APP_NAME: str = "Synapse AI"
    DEBUG: bool = False
    MODE: str = "production"

    # =========================
    # Database (REQUIRED)
    # =========================
    DATABASE_URL: str

    # =========================
    # Vector Store
    # =========================
    VECTOR_STORE_PATH: str = "./vector_store"
    VECTOR_DIM: int = 1536

    # =========================
    # Limits
    # =========================
    MAX_FREE_TOKENS: int = 1000
    MAX_HISTORY: int = 20
    MAX_TOKENS_PER_REQUEST: int = 2000
    SYSTEM_MEMORY_LIMIT: int = 2048

    UPLOAD_DIRS: str = "./uploads"

    # =========================
    # Server
    # =========================
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # =========================
    # Auth / Security
    # =========================
    SECRET_KEY: str = "supersecretkey"
    JWT_ALGORITHM: str = "HS256"

    # =========================
    # Model Providers
    # =========================
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4"

    ANTHROPIC_API_KEY: str | None = None

    GROK_API_KEY: str | None = None
    GROK_MODEL: str = "grok-1"

    HF_API_KEY: str | None = None

    # =========================
    # Ollama (Local)
    # =========================
    USE_OLLAMA: bool = True
    OLLAMA_URL: str = "http://localhost:11434"

    # =========================
    # Speech
    # =========================
    STT_API_KEY: str | None = None
    TTS_API_KEY: str | None = None
    ELEVENLABS_API_KEY: str | None = None

    VOSK_MODEL_PATH: str = "./models/vosk-model-small"

    # =========================
    # Feature Flags
    # =========================
    ENABLE_RAG: bool = True
    ENABLE_TOOLS: bool = True
    ALLOW_UNLIMITED_TOKENS: bool = False

    # =========================
    # Pydantic config
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()