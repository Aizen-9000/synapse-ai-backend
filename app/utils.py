import uuid
import time
import hashlib


def generate_id() -> str:
    return str(uuid.uuid4())


def now_ts() -> int:
    return int(time.time())


def sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()