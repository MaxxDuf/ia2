from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from freeflow_llm import FreeFlowClient
import os

app = FastAPI()

# Page HTML simple intégrée
HTML_PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Chat IA</title>
</head>
<body>
    <h1>Chat avec l'IA</h1>
    <input id="msg" type="text" placeholder="Écris ton message">
    <button onclick="send()">Envoyer</button>
    <pre id="out"></pre>

    <script>
        async function send() {
            const msg = document.getElementById("msg").value;
            const res = await fetch(`/chat?message=${encodeURIComponent(msg)}`);
            const data = await res.json();
            document.getElementById("out").textContent = data.response || data.error;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.get("/chat")
def chat(message: str = Query(...)):
    try:
        with FreeFlowClient() as client:
            response = client.chat(
                messages=[{"role": "user", "content": message}]
            )
        return {"response": response.content}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
