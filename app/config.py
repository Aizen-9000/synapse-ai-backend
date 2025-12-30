from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App
    APP_NAME: str = "OmniAI"
    ENV: str = "production"
    DEBUG: bool = False

    # Security
    MASTER_ENCRYPTION_KEY: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    # Databases
    DATABASE_URL: str
    MONGODB_URL: str

    # Cloud LLMs
    OPENAI_API_KEY: str | None = None
    ANTHROPIC_API_KEY: str | None = None
    GROK_API_KEY: str | None = None

    # Audio
    ELEVENLABS_API_KEY: str | None = None

    # Web Search
    WEB_SEARCH_API_KEY: str | None = None
    WEB_SEARCH_BASE_URL: str | None = None

    # Offline / Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_DEFAULT_MODEL: str = "llama3"

    # Feature Flags
    ENABLE_IMAGE_GEN: bool = True
    ENABLE_FILE_ANALYSIS: bool = True
    ENABLE_MULTI_AGENT: bool = True
    ENABLE_WEB_SEARCH: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()