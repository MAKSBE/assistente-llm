import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "codellama:7b-code")

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
            "top_p": 0.8,              # Controle de diversidade
            "top_k": 20,               # Limita escolhas de tokens
            "repeat_penalty": 1.1,     # Evita repetição
            "num_predict": 512,        # Aumentado para permitir respostas mais longas
            "num_ctx": 2048,           # Contexto menor
            "stop": ["\n\nQuestion:", "\n\nPergunta:", "Human:", "User:"]  # Para parar em perguntas
        }
    }
    
    try:
        res = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
        return res.json().get("response", "")
    except Exception as e:
        return f"Erro ao consultar modelo: {str(e)}"
