class ModeManager:
    def __init__(self):
        self.offline = False

    def enable_offline(self):
        self.offline = True

    def disable_offline(self):
        self.offline = False

    def is_offline(self) -> bool:
        return self.offline