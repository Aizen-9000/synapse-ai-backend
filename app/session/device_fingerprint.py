import hashlib

def fingerprint(device_info: str) -> str:
    return hashlib.sha256(device_info.encode()).hexdigest()