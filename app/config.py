from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # LLM providers
    GROQ_API_KEY: str | None = None
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"  # fallback if you have OpenAI

    # Ollama/local Llama (if you run ollama locally)
    USE_OLLAMA: bool = False
    OLLAMA_URL: str = "http://127.0.0.1:11434"  # local ollama

    # TTS / STT
    ELEVENLABS_API_KEY: str | None = None

    # Web search
    DUCKDUCKGO: bool = True

    # App / runtime
    MODE: str = "prod"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()