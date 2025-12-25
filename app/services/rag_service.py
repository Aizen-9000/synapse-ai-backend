from app.vectorstore.faiss_store import FaissStore
from app.adapters.model_adapter import ModelAdapter

class RAGService:
    def __init__(self, vector_store: FaissStore, model_adapter: ModelAdapter):
        self.vector_store = vector_store
        self.model_adapter = model_adapter

    def query(self, user_id: str, query: str):
        query_vector = self.model_adapter.text_to_vector(query)
        indices, distances = self.vector_store.search(query_vector)
        context = self.model_adapter.retrieve_context(indices)
        answer_vector = self.model_adapter.generate_response(context)
        return self.model_adapter.vector_to_text(answer_vector)