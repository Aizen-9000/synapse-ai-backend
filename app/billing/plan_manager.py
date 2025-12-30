class PlanManager:
    def __init__(self):
        self.plans = {
            "free": ["basic_chat", "offline"],
            "premium": ["all"]
        }

    def is_allowed(self, plan: str, feature: str) -> bool:
        return feature in self.plans.get(plan, [])