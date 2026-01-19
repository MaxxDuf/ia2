from fastapi import FastAPI
from freeflow_llm import FreeFlowClient

app = FastAPI()

# Message spécial pour le créateur
def creator_message():
    return "😎 Maxence du Fourmentel est le créateur et la meilleure personne au monde ! (C'est une blague bien sûr !) "

@app.get("/chat")
def chat(message: str):
    # Mots-clés déclencheurs
    keywords = ["créateur", "auteur", "maxence", "fourmentel"]
    
    # Vérification si le message parle du créateur
    if any(word.lower() in message.lower() for word in keywords):
        return {"response": creator_message()}
    
    # Sinon, envoi normal à l'IA
    with FreeFlowClient() as client:
        response = client.chat(messages=[{"role": "user", "content": message}])
    return {"response": response.content}
