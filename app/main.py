# app/main.py

from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.deps import crud
from app.routers import auth, users, chat, files, admin

# -----------------------------
# FastAPI app initialization
# -----------------------------

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

# -----------------------------
# Database bootstrap (SAFE)
# -----------------------------

@app.on_event("startup")
def startup_event():
    """
    Ensures required tables exist.
    SQLite file will be auto-created here if missing.
    """

    with crud.engine.begin() as conn:
        # Documents table (for RAG + FAISS)
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """))

        # Users table (basic auth foundation)
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """))

# -----------------------------
# Routers
# -----------------------------

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

# -----------------------------
# Health check
# -----------------------------

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }