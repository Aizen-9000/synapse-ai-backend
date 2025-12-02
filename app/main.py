from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .router_chat import router as chat_router
from .router_utils import router as utils_router

app = FastAPI(title="Mobile Backend for Synapse AI")

origins = ["*"]  # tighten this before production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(chat_router)
app.include_router(utils_router)

@app.get("/")
async def root():
    return {"app": "mobile-backend", "mode": settings.MODE}