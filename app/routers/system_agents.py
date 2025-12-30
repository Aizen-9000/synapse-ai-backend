from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AgentRequest(BaseModel):
    role: str
    input_text: str


@router.post("/run")
def run_agent(payload: AgentRequest):
    """
    HTTP entry point for system agents.
    """
    agent = SystemAgent(payload.role)
    return {
        "result": agent.act(payload.input_text)
    }


class SystemAgent:
    """
    Lightweight HTTP-exposed wrapper.
    Core logic can later move to app/agents/.
    """
    def __init__(self, role: str):
        self.role = role

    def act(self, input_text: str):
        return f"[{self.role}] processed: {input_text}"