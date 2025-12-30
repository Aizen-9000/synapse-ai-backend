class SessionGuard:
    @staticmethod
    def verify(active: bool):
        if not active:
            raise PermissionError("Session expired")