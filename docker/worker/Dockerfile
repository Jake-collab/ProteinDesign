FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app/worker

# worker deps
RUN pip install --no-cache-dir psycopg2-binary redis requests

COPY worker/ /app/worker/

CMD ["python","-m","worker.main"]

