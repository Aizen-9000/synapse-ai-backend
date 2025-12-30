class SecureMemory:
    @staticmethod
    def wipe(obj):
        if isinstance(obj, str):
            obj = "\0" * len(obj)