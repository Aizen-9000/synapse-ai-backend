from app.system_actions.action_router import ActionRouter

class SystemActionService:
    def __init__(self):
        self.router = ActionRouter()

    def handle(self, action, platform):
        return self.router.route(action, platform)