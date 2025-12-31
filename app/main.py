from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.plugins import PluginLoader
plugin_loader =PluginLoader()
from app.config import get_settings
from app.routers import (
    auth,
    users,
    admin,
    chat,
    files,
    tools,
    toolkit,
    local_ai,
    multilingual,
    stt,
    tts,
    system_agents,
    sync_engine,
    plugins,
)

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
)

# CORS (desktop + web safe)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # desktop apps + web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(tools.router, prefix="/tools", tags=["Tools"])
app.include_router(toolkit.router, prefix="/toolkit", tags=["Toolkit"])
app.include_router(local_ai.router, prefix="/local-ai", tags=["Offline"])
app.include_router(multilingual.router, prefix="/lang", tags=["Multilingual"])
app.include_router(stt.router, prefix="/stt", tags=["STT"])
app.include_router(tts.router, prefix="/tts", tags=["TTS"])
app.include_router(system_agents.router, prefix="/agents", tags=["Agents"])
app.include_router(sync_engine.router, prefix="/sync", tags=["Sync"])
app.include_router(plugins.router, prefix="/{plugin_name}/execute", tags=["Plugins"])

@app.get("/health")
def health():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "env": settings.ENV,
    }