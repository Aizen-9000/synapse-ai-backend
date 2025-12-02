import httpx
from urllib.parse import quote_plus

async def duckduckgo_search(query: str, max_results: int = 5):
    # DuckDuckGo instant answer API
    q = quote_plus(query)
    url = f"https://api.duckduckgo.com/?q={q}&format=json&no_redirect=1&no_html=1"
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
        if r.status_code != 200:
            return []
        j = r.json()
        results = []
        # abstract and related topics fallback
        if j.get("AbstractText"):
            results.append({"title": j.get("Heading") or query, "snippet": j.get("AbstractText"), "url": j.get("AbstractURL")})
        # RelatedTopics may contain list of topics
        for t in j.get("RelatedTopics", [])[:max_results]:
            if "Text" in t and "FirstURL" in t:
                results.append({"title": t.get("Text"), "snippet": "", "url": t.get("FirstURL")})
        return results