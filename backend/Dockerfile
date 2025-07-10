FROM python:3.10-slim

WORKDIR /app

COPY ./backend /app
COPY ./docs /app/docs
COPY ./frontend /app/frontend

RUN pip install fastapi uvicorn requests chromadb

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
