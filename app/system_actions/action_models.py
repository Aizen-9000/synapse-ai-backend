from pydantic import BaseModel
from typing import Optional, List
from .action_types import ActionScope, SystemAction

class ActionRequest(BaseModel):
    user_id: str
    action: SystemAction
    platform: Optional[str] = None


class ActionResponse(BaseModel):
    executed: bool
    scope: ActionScope
    message: str
    instructions: Optional[List[str]] = None