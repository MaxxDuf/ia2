from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from freeflow_llm import FreeFlowClient

app = FastAPI()

# Autoriser l'accès depuis ton site GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/chat")
def chat(message: str):
    with FreeFlowClient() as client:
        response = client.chat(
            messages=[{"role": "user", "content": message}]
        )
    return {"response": response.content}
