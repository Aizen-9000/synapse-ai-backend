from typing import List, Dict
from app.adapters.web_search_adapter import WebSearchAdapter
from app.adapters.web_fetch_adapter import WebFetchAdapter

class WebRAGService:
    def __init__(
        self,
        search_adapter: WebSearchAdapter,
        fetch_adapter: WebFetchAdapter,
        embedder
    ):
        self.search_adapter = search_adapter
        self.fetch_adapter = fetch_adapter
        self.embedder = embedder

    async def run(self, query: str) -> Dict:
        search_results = await self.search_adapter.search(query)

        documents = []
        citations = []

        for idx, result in enumerate(search_results):
            content = await self.fetch_adapter.fetch(result["url"])

            documents.append({
                "content": content,
                "source": result["url"]
            })

            citations.append({
                "id": idx + 1,
                "title": result.get("title"),
                "url": result["url"]
            })

        embeddings = self.embedder.embed_documents(
            [doc["content"] for doc in documents]
        )

        return {
            "query": query,
            "documents": documents,
            "embeddings": embeddings,
            "citations": citations
        }