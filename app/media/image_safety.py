class ImageSafety:
    def check(self, prompt: str) -> bool:
        banned = ["illegal", "abuse"]
        return not any(word in prompt.lower() for word in banned)