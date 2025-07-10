from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from vector_store import get_relevant_docs
from mistral_client import query_mistral

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    question = body.get("question")

    if not question:
        return JSONResponse(status_code=400, content={"error": "Missing question"})

    docs = get_relevant_docs(question)
    print(f"[DEBUG] Documentos retornados pelo RAG: {docs}")
    context = "\n".join(docs)
    response = query_mistral(question, context)
    # Pós-processamento para limpar a resposta
    response_linhas = [linha for linha in response.split('\n') if linha.strip() and not linha.strip().lower().startswith('context:')]
    resposta_final = "\n".join(response_linhas) if response_linhas else response
    return {"response": resposta_final}

