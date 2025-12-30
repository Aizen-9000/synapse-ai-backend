class ShortTermMemory:
    def __init__(self):
        self.sessions = {}

    def add(self, session_id: str, message: str):
        self.sessions.setdefault(session_id, []).append(message)

    def get(self, session_id: str):
        return self.sessions.get(session_id, [])