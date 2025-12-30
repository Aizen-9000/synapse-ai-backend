class ModuleRegistry:
    def __init__(self, modules: dict):
        self.modules = modules

    def is_enabled(self, module_name: str) -> bool:
        return self.modules.get(module_name, False)