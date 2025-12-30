class SecurityService:
    def __init__(self):
        self._consents: dict[str, bool] = {}

    def grant_consent(self, user_id: str):
        self._consents[user_id] = True

    def revoke_consent(self, user_id: str):
        self._consents[user_id] = False

    def has_consent(self, user_id: str) -> bool:
        return self._consents.get(user_id, False)