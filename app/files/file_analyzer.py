class FileAnalyzer:
    def analyze(self, data) -> str:
        if isinstance(data, list):
            return f"CSV with {len(data)} rows"
        return "Unstructured file"