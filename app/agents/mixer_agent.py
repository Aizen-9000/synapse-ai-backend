from app.agents.base_agent import BaseAgent
from app.intelligence.answer_mixer import AnswerMixer


class MixerAgent(BaseAgent):
    name = "mixer"

    def __init__(self, mixer: AnswerMixer):
        self.mixer = mixer

    async def execute(self, payload: dict) -> dict:
        mixed = self.mixer.mix(payload["verified"])
        return {"mixed": mixed}