from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from freeflow_llm import FreeFlowClient

app = FastAPI()

# Autoriser ton front-end GitHub Pages
origins = [
    "https://maxxduf.github.io",  # ton front-end
    "http://localhost",           # pour tests locaux
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat")
def chat(message: str):
    with FreeFlowClient() as client:
        response = client.chat(messages=[{"role": "user", "content": message}])
    return {"response": response.content}
