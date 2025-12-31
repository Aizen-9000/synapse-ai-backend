from app.plugins import PluginLoader


class PluginService:
    def __init__(self, loader: PluginLoader):
        self.loader = loader

    def execute(self, name: str, payload: dict):
        return self.loader.execute(name, payload)