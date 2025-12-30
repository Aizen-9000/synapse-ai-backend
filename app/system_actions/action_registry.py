from .action_types import ActionScope, SystemAction

ACTION_REGISTRY = {
    SystemAction.CLEAR_CACHE: ActionScope.APP_ONLY,
    SystemAction.RESET_APP: ActionScope.APP_ONLY,
    SystemAction.EXPORT_DATA: ActionScope.APP_ONLY,
    SystemAction.OPTIMIZE_STORAGE: ActionScope.USER_ASSISTED,
    SystemAction.TROUBLESHOOT: ActionScope.USER_ASSISTED,
}