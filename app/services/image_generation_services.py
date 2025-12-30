from app.media.image_generation import ImageGenerator

class ImageGenerationService:
    def __init__(self):
        self.generator = ImageGenerator()

    def generate(self, prompt: str) -> dict:
        return self.generator.generate(prompt)