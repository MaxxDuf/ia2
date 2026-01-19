from fastapi import FastAPI
from freeflow_llm import FreeFlowClient

app = FastAPI()

@app.get("/chat")
def chat(message: str):
    with FreeFlowClient() as client:
        response = client.chat(messages=[{"role": "user", "content": message}])
    return {"response": response.content}
