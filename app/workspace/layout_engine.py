class LayoutEngine:
    def __init__(self, layout_config: dict):
        self.layout = layout_config

    def serialize(self):
        return self.layout