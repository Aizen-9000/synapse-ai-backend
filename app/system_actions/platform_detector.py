def detect_platform(user_agent: str | None = None) -> str:
    if not user_agent:
        return "unknown"

    ua = user_agent.lower()

    if "android" in ua:
        return "android"
    if "iphone" in ua or "ios" in ua:
        return "ios"
    if "windows" in ua:
        return "windows"
    if "mac" in ua:
        return "macos"
    if "linux" in ua:
        return "linux"

    return "unknown"