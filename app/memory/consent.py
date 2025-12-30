class ConsentManager:
    def __init__(self):
        self.flags = {}

    def grant(self, user_id: str):
        self.flags[user_id] = True

    def revoke(self, user_id: str):
        self.flags[user_id] = False

    def allowed(self, user_id: str) -> bool:
        return self.flags.get(user_id, False)