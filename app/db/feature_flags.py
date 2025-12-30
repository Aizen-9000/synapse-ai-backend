DEFAULT_FLAGS = {
    "web_search": True,
    "multi_agent": True,
    "image_generation": False,
    "premium_models": False,
    "offline_mode": True,
    "stt": True,
    "tts": True
}

class FeatureFlags:
    def __init__(self, flags: dict):
        self.flags = flags or DEFAULT_FLAGS

    def enabled(self, feature: str) -> bool:
        return self.flags.get(feature, False)