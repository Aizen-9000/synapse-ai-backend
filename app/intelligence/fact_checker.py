class FactChecker:
    def verify(self, responses: dict[str, str]) -> dict[str, str]:
        verified = {}
        for model, text in responses.items():
            if len(text.strip()) > 0:
                verified[model] = text
        return verified