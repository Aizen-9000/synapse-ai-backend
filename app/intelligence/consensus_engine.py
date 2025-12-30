class ConsensusEngine:
    def select_best(self, verified: dict[str, str]) -> str:
        return max(
            verified.values(),
            key=lambda x: len(x),
            default=""
        )