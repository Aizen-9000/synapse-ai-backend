import httpx
from typing import List, Dict

class WebSearchAdapter:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    async def search(self, query: str, num_results: int = 5) -> List[Dict]:
        """
        Returns:
        [
          {
            "title": "...",
            "url": "...",
            "snippet": "..."
          }
        ]
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "query": query,
            "limit": num_results
        }

        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.post(
                self.base_url,
                json=payload,
                headers=headers
            )
            response.raise_for_status()

        return response.json().get("results", [])