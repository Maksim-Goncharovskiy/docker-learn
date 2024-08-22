FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src src
COPY data data

CMD ["python", "/app/src/main.py"]