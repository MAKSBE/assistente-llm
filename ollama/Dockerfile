FROM ollama/ollama

# Instala o curl
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copia o entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

