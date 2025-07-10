FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libmagic1 file

RUN pip install \
    langchain \
    langchain-community \
    chromadb \
    "unstructured[md]" \
    sentence-transformers

CMD ["python", "embed_docs.py"]

