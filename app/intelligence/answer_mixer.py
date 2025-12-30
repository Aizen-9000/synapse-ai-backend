class AnswerMixer:
    def mix(self, verified: dict[str, str]) -> str:
        seen = set()
        mixed = []

        for text in verified.values():
            for sentence in text.split("."):
                s = sentence.strip()
                if s and s not in seen:
                    seen.add(s)
                    mixed.append(s)

        return ". ".join(mixed) + "."