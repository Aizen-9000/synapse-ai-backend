def build_instructions(action: str, platform: str) -> list[str]:
    if action == "clear_cache":
        if platform == "android":
            return [
                "Open Settings",
                "Go to Apps",
                "Select this app",
                "Tap Storage",
                "Tap Clear Cache"
            ]
        if platform == "windows":
            return [
                "Open Settings",
                "Go to Apps",
                "Select the application",
                "Open Advanced Options",
                "Click Reset or Clear Cache"
            ]

    return ["No instructions available for this platform."]