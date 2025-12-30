from .action_registry import ACTION_REGISTRY
from .action_executer import ActionExecutor
from .instruction_builder import build_instructions
from .action_models import ActionResponse
from .action_types import ActionScope, SystemAction


class ActionRouter:
    def __init__(self):
        self.executor = ActionExecutor()

    def route(self, action: SystemAction, platform: str) -> ActionResponse:
        if action not in ACTION_REGISTRY:
            return ActionResponse(
                executed=False,
                scope=ActionScope.USER_ASSISTED,
                message=f"Unsupported system action: {action}",
                instructions=["This action is not supported by the system."]
            )

        scope: ActionScope = ACTION_REGISTRY[action]

        if scope == ActionScope.APP_ONLY:
            success = self.executor.execute(action)
            return ActionResponse(
                executed=success,
                scope=scope,
                message="Action executed successfully."
            )

        instructions = build_instructions(action, platform)

        return ActionResponse(
            executed=False,
            scope=scope,
            message="Action requires user assistance.",
            instructions=instructions
        )