from app.db.crud import CRUD
from app.adapters.model_adapter import ModelAdapter
from app.vectorstore.faiss_store import FaissStore
from app.config import settings

crud = CRUD(settings.DATABASE_URL)
vector_store = FaissStore(settings.VECTOR_STORE_PATH)
model_adapter = ModelAdapter()