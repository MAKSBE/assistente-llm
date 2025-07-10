#!/bin/bash

# Inicia o servidor Ollama em background
ollama serve &

# Aguarda o Ollama subir
echo "Aguardando Ollama iniciar..."
until curl --silent --fail http://localhost:11434/api/tags; do
  sleep 1
done

echo "Servidor Ollama ativo. Verificando modelo..."

# Baixa o modelo se ainda não estiver disponível
if ! curl --silent http://localhost:11434/api/tags | grep -q "codellama:7b-code"; then
  echo "Modelo 'codellama:7b-code' não encontrado. Fazendo o download..."
  ollama pull codellama:7b-code
else
  echo "Modelo 'codellama:7b-code' já está disponível."
fi

echo "Tudo pronto com Ollama!"

# Mantém o container vivo
tail -f /dev/null

