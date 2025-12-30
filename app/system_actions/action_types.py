from enum import Enum

class ActionScope(str, Enum):
    APP_ONLY = "app_only"
    USER_ASSISTED = "user_assisted"
    PRIVILEGED = "privileged"


class SystemAction(str, Enum):
    CLEAR_CACHE = "clear_cache"
    RESET_APP = "reset_app"
    EXPORT_DATA = "export_data"
    OPTIMIZE_STORAGE = "optimize_storage"
    TROUBLESHOOT = "troubleshoot"