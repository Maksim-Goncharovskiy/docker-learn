FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY config.py config.py
COPY main.py main.py

EXPOSE 8000

ENV DB_NAME=my_db
ENV DB_PORT=5432
ENV DB_USER=maksim

CMD ["python", "main.py"]