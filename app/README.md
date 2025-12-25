Synapse AI - backend skeleton
=============================

Quick start
-----------
1. Copy .env.example -> .env and fill keys.
2. Create venv:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
3. Run:
   uvicorn app.main:app --reload --port 8000
4. Endpoints:
   - GET /health
   - POST /auth/login  { "username": "bob" }
   - POST /users/create { "username": "bob", "display_name": "Bob" }
   - POST /chat/send { "user_id": 1, "message": "hi" }
   - POST /files/upload (multipart form: user_id + file)

Notes
-----
- This is a skeleton. Key extension points:
  - adapters/model_adapter.py -> change provider or add streaming
  - services/rag_service.py -> add chunking + embedding calls
  - vectorstore/faiss_store.py -> replace with faiss-gpu for production
- GPU: none required for this skeleton. If you host a local LLM, you will need appropriate GPU + drivers.