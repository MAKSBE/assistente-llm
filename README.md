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
   git clone git clone https://github.com/MAKSBE/assistente-llm.git
   cd llm
   ```

2. **Configure variáveis de ambiente (opcional):**
   - Você pode definir `OLLAMA_BASE_URL` e `MODEL_NAME` conforme necessário, ou usar os padrões do sistema.
   - O container já irá subir com as variáveis configuradas. 

3. **Suba os containers:**
   ```sh
   docker-compose up --build
   ```
   Isso irá iniciar todos os serviços: backend, ingest, ollama e frontend.
   Ao iniciar os containers serão baixadas e instaladas todas as dependências.

5. **Acesse a interface:**
   - Abra o navegador e acesse `http://localhost:8000/frontend/index.html` (ou a porta configurada no frontend).

6. **Utilize a API:**
   - O backend expõe endpoints para consulta ao modelo e ingestão de documentos.
   - Endereço Swagger - `http://localhost:8000/docs`
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

- Consulte a pasta `docs/` para inserir padrões de código, práticas recomendadas e exemplos de uso.

## Melhorias

## 1. Otimização de Recursos
- Ajustar a configuração dos containers para consumir menos memória e CPU, garantindo que o LLM rode bem em máquinas pessoais ou servidores locais.
- Permitir fácil troca de modelos (ex: CodeLlama, Mistral) via variáveis de ambiente ou interface.
- Buscar modelo de linguagem mais eficiênte para desenvolvedores.
- 
## 2. Interface de Administração Local
- Criar uma interface web simples para monitorar o status dos serviços, logs e uso de recursos.
- Adicionar opções para reiniciar serviços ou atualizar modelos sem precisar acessar o terminal.

## 3. Facilidade de Instalação
- Fornecer scripts que automatize a instalação do Docker e a configuração inicial.
- Documentar requisitos mínimos de hardware para rodar o projeto localmente.

## 4. Backup e Restauração
- Implementar mecanismos para backup e restauração dos dados e embeddings locais.
- Permitir exportar/importar configurações e documentos.

## 5. Segurança Local
- Mesmo em ambiente local, proteger a interface e a API com autenticação simples (ex: senha única).
- Implementar logs de acesso para auditoria.

## 6. Atualização Simples
- Fornecer um comando ou script para atualizar facilmente o projeto e os modelos, sem perder dados locais.

## 7. Customização
- Permitir ao usuário customizar prompts, contexto e parâmetros do modelo via interface ou arquivo de configuração.

## 8. Desempenho
- Implementar cache local para respostas frequentes.
- Permitir configurar o tamanho do contexto e batch de embeddings para otimizar o desempenho. 
