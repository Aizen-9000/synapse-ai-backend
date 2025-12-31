from typing import Dict
from .plugin_manifest import PluginManifest
from .sandbox import PluginSandbox


class PluginLoader:
    def __init__(self):
        self._plugins: Dict[str, PluginManifest] = {}

    def register(self, manifest: PluginManifest):
        if manifest.name in self._plugins:
            raise ValueError(f"Plugin '{manifest.name}' already registered")

        self._plugins[manifest.name] = manifest

    def unregister(self, name: str):
        self._plugins.pop(name, None)

    def list_plugins(self):
        return list(self._plugins.keys())

    def execute(self, name: str, payload: dict):
        plugin = self._plugins.get(name)

        if not plugin:
            raise ValueError(f"Plugin '{name}' not found")

        sandbox = PluginSandbox(plugin)
        return sandbox.execute(payload)