Mobile-backend for Synapse AI
----------------------------

Run locally (development):

1. Create .env from .env.example and set keys.
2. Create a virtualenv and install requirements:
   python -m venv .venv
   .venv/bin/activate   (or Windows: .venv\Scripts\activate)
   pip install -r requirements.txt

3. Start server:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

APIs:
- POST /chat/generate   -> { message, max_tokens?, temperature? }
- POST /chat/stream     -> streaming
- POST /chat/transcribe -> upload audio file
- POST /chat/tts        -> { text }
- GET  /chat/search?q=  -> search
- POST /chat/translate  -> { text, target_lang }

Notes:
- By default LLMAdapter uses (in priority): OLLAMA local -> GROQ -> OPENAI
- Set USE_OLLAMA=true if you run `ollama` on local machine.
- For free/unlimited local Llama models you can run ollama, or host llama in local infra.