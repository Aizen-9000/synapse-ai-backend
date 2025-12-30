import requests

class WebFetchAdapter:
    async def fetch(self, url: str) -> str:
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            return f"Failed to fetch {url}: {e}"