from fastapi import APIRouter, Depends
from app.services.web_rag_service import WebRAGService

router = APIRouter(prefix="/tools", tags=["tools"])

@router.post("/web-search")
async def web_search_tool(
    query: str,
    web_rag_service: WebRAGService = Depends()
):
    return await web_rag_service.run(query)