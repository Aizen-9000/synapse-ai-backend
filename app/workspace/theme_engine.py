class ThemeEngine:
    def __init__(self, theme_config: dict):
        self.theme = theme_config

    def serialize(self):
        return self.theme