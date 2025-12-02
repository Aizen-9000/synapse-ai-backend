

Synapse Mobile – Backend (Python / FastAPI)

This is the backend service for Synapse Mobile, a multilingual AI chatbot application that supports:

🧠 LLM responses using Grok / Llama / custom models

🎤 Speech-to-Text (STT) with Google / Vosk / OpenAI Whisper (configurable)

🔊 Text-to-Speech (TTS) with 11Labs / Edge / OpenAI (configurable)

🌍 Multilingual support

🌐 Web search + returns visited URLs

🔌 REST API endpoints for the Flutter mobile app


The backend is built with FastAPI, fully stateless, and deployable on Render, Railway, Vercel, or any Linux server.


---

🔧 Project Structure

mobile-backend/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── deps.py
│   ├── models.py
│   ├── llm.py
│   ├── translate.py
│   ├── websearch.py
│   ├── stt.py
│   ├── tts.py
│   ├── router_chat.py
│   └── router_utils.py
│
├── requirements.txt
├── .env
└── README.md


---

🚀 Running Locally

1. Install dependencies

pip install -r requirements.txt

2. Copy .env.example to .env and add your keys

GROK_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here

3. Start server

uvicorn app.main:app --reload

Backend runs at:

http://localhost:8000


---

🌐 Deployment

This backend is optimized for:

Render (recommended)

Railway

Fly.io

Any VM / Docker server


Just connect your GitHub repository and deploy.


---

📡 Endpoints (Summary)

Method	URL	Description

POST	/chat/	LLM chatbot response
POST	/stt/	Speech to Text
POST	/tts/	Text to Speech
GET	/search?q=	Web search
GET	/health	Status check



---

📦 Tech Stack

FastAPI – Backend framework

Grok / Llama API – LLM

11Labs / Edge / Whisper – TTS / STT

DuckDuckGo / SerpAPI – Web search

Python 3.11+



---

📝 License

This project currently uses no license (private).