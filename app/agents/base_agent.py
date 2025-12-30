from abc import ABC, abstractmethod


class BaseAgent(ABC):
    name: str

    @abstractmethod
    async def execute(self, payload: dict) -> dict:
        pass