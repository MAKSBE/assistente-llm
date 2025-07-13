# 🧠 Projeto: Assistente de IA Local com LLM + Docker + Python

## 📌 Visão Geral

Este projeto implementa um assistente de IA baseado em **Large Language Models (LLM)**, rodando 100% localmente, com orquestração via **Docker**.

Ele inclui:

- Backend em Python (FastAPI)
- Frontend web simples
- Ingestão e embedding de documentos
- Integração com modelos como **Mistral** e **CodeLlama** via **Ollama**

O objetivo é fornecer uma solução privada e customizável para consultas e manipulação de dados com IA generativa.

---

## 🗂️ Estrutura do Projeto

```
llm/
  backend/         # API backend em Python (FastAPI)
  frontend/        # Interface web HTML/JS
  ingest/          # Scripts de ingestão e embedding de documentos
  ollama/          # Configuração do container com LLM
  docker-compose.yml
  docs/            # Documentação e boas práticas
```

---

## ⚙️ Principais Componentes

### 🔹 `backend/`
API FastAPI que expõe endpoints para consultas ao LLM e serve o frontend.

### 🔹 `frontend/`
Interface web simples e responsiva (tema escuro), construída em HTML e JS puro.

### 🔹 `ingest/`
Scripts em Python usando LangChain e ChromaDB para gerar embeddings a partir de documentos da pasta `docs/`.

### 🔹 `ollama/`
Configuração Docker para execução local de modelos via Ollama, como **Mistral** e **CodeLlama**.

### 🔹 `docker-compose.yml`
Orquestra todos os serviços automaticamente com um único comando.

---

## 🚀 Funcionalidades

- Consulta a LLMs locais via API REST
- Enriquecimento do contexto com RAG (Retrieval-Augmented Generation)
- Interface web para interação
- Execução local e offline com Docker

---

## 🧪 Como Rodar o Projeto

### ✅ Pré-requisitos

- Docker e Docker Compose instalados  
- (Opcional) Python 3.8+ para rodar scripts manualmente

### 📦 Passos para execução

```bash
# Clone o repositório
git clone https://github.com/MAKSBE/assistente-llm.git
cd assistente-llm

# (Opcional) Configure variáveis de ambiente
export OLLAMA_BASE_URL=http://localhost:11434
export MODEL_NAME=mistral

# Suba os containers
docker-compose up --build
```

### 🌐 Acesse:

- Interface Web: [http://localhost:8000/frontend/index.html](http://localhost:8000/frontend/index.html)  
- Swagger da API: [http://localhost:8000/docs](http://localhost:8000/docs)

### 💬 Exemplo de uso via `curl`

```bash
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explique o que é LLM."}'
```

---

## 🧾 Estrutura de Arquivos Relevantes

- `backend/main.py`: Inicialização da API e rotas
- `backend/mistral_client.py`: Cliente para comunicação com Ollama
- `ingest/embed_docs.py`: Geração de embeddings com LangChain + ChromaDB
- `docker-compose.yml`: Orquestração dos serviços

---

## 🛠️ Boas Práticas

- Separação clara de responsabilidades (camadas Domain, Application, Infra, API)
- Uso de DTOs (nunca exponha entidades diretamente)
- Injeção de dependência e testes facilitados
- Validações centralizadas
- Prompts otimizados e configuráveis
- Documentação na pasta `docs/`

---

## 📈 Melhorias Planejadas

### 🔧 Otimização de Recursos
- Ajustar containers para rodar em máquinas pessoais
- Permitir troca rápida de modelos via `.env`

### 📊 Interface de Administração
- Painel web para status, logs, memória, CPU e restart de serviços

### ⚡ Instalação Facilitada
- Script para instalar Docker e configurar ambiente automaticamente
- Requisitos mínimos de hardware documentados

### 💾 Backup e Restauração
- Exportação/importação de embeddings e documentos
- Salvamento das configurações locais

### 🔐 Segurança
- Autenticação com senha única
- Logs de acesso para auditoria

### 🔁 Atualização Simplificada
- Script para atualizar código e modelos sem perda de dados

### 🎛️ Customização
- Permitir ajuste de prompts, contexto e temperatura do modelo via interface

### 🚀 Performance
- Cache local para perguntas frequentes
- Controle do tamanho de chunk/contexto

---
