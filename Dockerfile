FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY blog_summarizer.py .
COPY app.py .
COPY styles.css .
COPY tasks.py .
COPY podcast_tramsitions.py .
COPY agents.py .


EXPOSE 7777

CMD ["python", "app.py"]
