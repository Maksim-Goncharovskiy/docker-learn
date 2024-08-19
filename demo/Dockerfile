FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src src

CMD ["python", "src/app.py"]
