class WebSearchAdapter:
    async def search(self, query: str, num_results: int = 5) -> list:
        # Placeholder: return simulated search results
        return [{"title": f"Result {i+1}", "url": f"https://example.com/{i+1}"} for i in range(num_results)]