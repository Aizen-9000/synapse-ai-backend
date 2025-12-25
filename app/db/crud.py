# app/db/crud.py

from sqlalchemy import create_engine, text

class CRUD:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url, future=True)

    def create_document(self, content: str) -> int:
        query = text("""
            INSERT INTO documents (content)
            VALUES (:content)
            RETURNING id
        """)
        with self.engine.begin() as conn:
            result = conn.execute(query, {"content": content})
            return result.scalar_one()

    def get_document_by_id(self, doc_id: int) -> str | None:
        query = text("""
            SELECT content
            FROM documents
            WHERE id = :doc_id
        """)
        with self.engine.connect() as conn:
            result = conn.execute(query, {"doc_id": doc_id}).fetchone()
            return result[0] if result else None

    def list_documents(self, limit: int = 10):
        query = text("""
            SELECT id, content
            FROM documents
            LIMIT :limit
        """)
        with self.engine.connect() as conn:
            return conn.execute(query, {"limit": limit}).fetchall()