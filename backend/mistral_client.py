import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "codellama:7b-instruct")

def query_mistral(prompt, context=""):
    # Prompt otimizado para C#/.NET
    system_prompt = (
        "Você é um desenvolvedor especialista em C# .NET. "
        "Forneça exemplos de código e explicações concisas e práticas. "
        "Se a pergunta pedir explicação, seja detalhado e didático. "
        "Se for uma pergunta objetiva, responda apenas com o trecho relevante, sem repetir o contexto."
    )
    
    full_prompt = f"{system_prompt}\n\nContext: {context}\n\nQuestion: {prompt}\n\nAnswer:"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,        # Mais focado e determinístico
            "top_p": 0.9,              # Controle de diversidade
            "top_k": 40,               # Limita escolhas de tokens
            "repeat_penalty": 1.15,    # Evita repetição
            "num_predict": 1024,       # Aumentado para permitir respostas mais longas
            "num_ctx": 4096,           # Contexto menor
            "stop": ["\n\n###", "User:", "Human:", "Pergunta:"] # Para parar em perguntas
        }
    }
    
    try:
        res = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
        return res.json().get("response", "")
    except Exception as e:
        return f"Erro ao consultar modelo: {str(e)}"
