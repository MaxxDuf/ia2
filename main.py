from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from freeflow_llm import FreeFlowClient

app = FastAPI()

# Pour permettre à ton HTML (GitHub Pages ou local) de communiquer avec Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou mets ton URL front-end si tu veux plus de sécurité
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat")
def chat(message: str):
    with FreeFlowClient() as client:
        response = client.chat(messages=[{"role": "user", "content": message}])
    return {"response": response.content}
