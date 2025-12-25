import faiss
import numpy as np
import os
from app.config import settings

class FAISSStore:
    def __init__(self):
        self.index_path = settings.VECTOR_STORE_PATH
        self.dim = 768  # typical embedding dimension, adjust as needed
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            self.index = faiss.IndexFlatL2(self.dim)

    def add_vector(self, vector: np.ndarray, metadata=None):
        self.index.add(np.array([vector], dtype='float32'))
        self.save_index()

    def query(self, vector: np.ndarray, top_k=5):
        D, I = self.index.search(np.array([vector], dtype='float32'), top_k)
        return I[0], D[0]

    def save_index(self):
        faiss.write_index(self.index, self.index_path)