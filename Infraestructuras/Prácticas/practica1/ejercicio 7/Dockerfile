FROM python:3.9-slim

WORKDIR /app

RUN mkdir data
COPY config.json data/config.json

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el código
COPY app.py .

CMD ["python", "app.py"]