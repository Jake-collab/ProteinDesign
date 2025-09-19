FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# system deps needed for psycopg2 and friends
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# app
WORKDIR /app/hub

# python deps (quote uvicorn extra so [] aren't shell-expanded)
RUN pip install --no-cache-dir fastapi "uvicorn[standard]" psycopg2-binary redis requests

# copy code last (better layer caching)
COPY hub/ /app/hub/

EXPOSE 8000

# start API
CMD ["uvicorn","hub.main:app","--host","0.0.0.0","--port","8000"]

