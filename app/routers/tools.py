from fastapi import APIRouter
from app.media.image_generation import ImageGenerator

router = APIRouter()
image_service = ImageGenerator()

@router.post("/image")
def generate_image(payload: dict):
    return image_service.generate(payload["prompt"])

@router.get("/status")
def tools_status():
    return {
        "web_search": True,
        "file_analysis": True,
        "image_generation": True
    }