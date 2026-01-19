from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Structure de la requête JSON
class Prompt(BaseModel):
    prompt: str

FREEFLOW_API_KEY = os.getenv("FREEFLOW_API_KEY")  # Ta clé API FreeFlow

@app.post("/chat")
def chat(prompt: Prompt):
    try:
        response = requests.post(
            "https://freeflow-llm.joshsparks.dev/api",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {FREEFLOW_API_KEY}"
            },
            json={"prompt": prompt.prompt}
        )
        data = response.json()
        return {"text": data.get("text", "Erreur")}
    except Exception as e:
        return {"error": str(e)}
