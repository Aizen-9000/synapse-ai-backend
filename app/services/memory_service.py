import time


class MemoryService:
    def __init__(self):
        self._memory: list[dict] = []

    def store(
        self,
        content: str,
        *,
        user_id: str | None = None,
        ttl: int | None = None,
        metadata: dict | None = None,
    ):
        entry = {
            "content": content,
            "user_id": user_id,
            "created_at": time.time(),
            "ttl": ttl,
            "metadata": metadata or {},
        }
        self._memory.append(entry)

    def retrieve(self, user_id: str | None = None) -> list[str]:
        now = time.time()
        results = []

        for m in self._memory:
            if m["ttl"] and now - m["created_at"] > m["ttl"]:
                continue
            if user_id and m["user_id"] != user_id:
                continue
            results.append(m["content"])

        return results

    def purge(self):
        self._memory.clear()