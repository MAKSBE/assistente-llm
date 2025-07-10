# Documentação do Projeto LLM

## Visão Geral

Este projeto é uma solução baseada em LLM (Large Language Model) que utiliza containers Docker para orquestrar diferentes componentes, incluindo backend, frontend, ingestão de dados e integração com modelos de linguagem (ex: Ollama/Mistral). O objetivo é fornecer uma interface para consulta e manipulação de dados utilizando modelos de linguagem natural.

## Estrutura do Projeto

```
llm/
  backend/         # API backend em Python
  frontend/        # Interface web (HTML)
  ingest/          # Scripts para ingestão e embedding de documentos
  ollama/          # Configuração do container do Ollama
  docker-compose.yml
  docs/            # Documentação e boas práticas
```

### Principais Componentes

- **backend/**: API em Python responsável por receber requisições, consultar o modelo de linguagem e retornar respostas.
- **frontend/**: Interface web simples para interação com o backend.
- **ingest/**: Scripts para processar e embutir documentos no sistema.
- **ollama/**: Configuração para rodar o modelo de linguagem (ex: Mistral, CodeLlama) via Ollama.
- **docker-compose.yml**: Orquestra todos os serviços necessários usando Docker.

## Funcionalidades

- Consulta a modelos de linguagem (ex: Mistral, CodeLlama) via API REST.
- Ingestão e embedding de documentos para enriquecer o contexto das respostas.
- Interface web para facilitar a interação com o sistema.
- Arquitetura modular e baseada em containers, facilitando a escalabilidade e manutenção.

## Como Rodar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados
- (Opcional) Python 3.8+ para rodar scripts manualmente

### Passos

1. **Clone o repositório:**
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd llm
   ```

2. **Configure variáveis de ambiente (opcional):**
   - Você pode definir `OLLAMA_BASE_URL` e `MODEL_NAME` conforme necessário, ou usar os padrões do sistema.

3. **Suba os containers:**
   ```sh
   docker-compose up --build
   ```
   Isso irá iniciar todos os serviços: backend, ingest, ollama e frontend.

4. **Acesse a interface:**
   - Abra o navegador e acesse `http://localhost:8080` (ou a porta configurada no frontend).

5. **Utilize a API:**
   - O backend expõe endpoints para consulta ao modelo e ingestão de documentos.
   - Exemplo de uso do endpoint de consulta (via `curl`):
     ```sh
     curl -X POST http://localhost:8000/api/query -H "Content-Type: application/json" -d '{"prompt": "Explique o que é LLM."}'
     ```

## Estrutura dos Principais Arquivos

- `backend/main.py`: Inicializa a API e define os endpoints.
- `backend/mistral_client.py`: Cliente para consulta ao modelo de linguagem via Ollama.
- `ingest/embed_docs.py`: Script para processar e embutir documentos.
- `docker-compose.yml`: Orquestra todos os serviços necessários.

## Dicas e Boas Práticas

- Consulte a pasta `docs/` para padrões de código, práticas recomendadas e exemplos de uso.
- Para adicionar novos modelos ou alterar configurações, edite as variáveis de ambiente e os arquivos de configuração dos containers. 