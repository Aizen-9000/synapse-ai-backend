from app.adapters.web_search_adapter import WebSearchAdapter
from app.adapters.web_fetch_adapter import WebFetchAdapter


class WebService:
    def __init__(
        self,
        search_adapter: WebSearchAdapter,
        fetch_adapter: WebFetchAdapter,
    ):
        self.search_adapter = search_adapter
        self.fetch_adapter = fetch_adapter

    async def research(self, query: str, limit: int = 5) -> list[str]:
        results = await self.search_adapter.search(query, limit)
        pages = []

        for r in results:
            url = r.get("url")
            if not url:
                continue
            text = await self.fetch_adapter.fetch(url)
            pages.append(text)

        return pages