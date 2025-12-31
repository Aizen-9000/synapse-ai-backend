class PluginSandbox:
    def __init__(self, manifest):
        self.manifest = manifest

    def validate(self):
        if not self.manifest.entrypoint:
            raise ValueError("Plugin entrypoint missing")

    def execute(self, payload: dict):
        self.validate()

        # You can add restrictions here later
        # Example: block network / fs access

        return self.manifest.entrypoint(payload)