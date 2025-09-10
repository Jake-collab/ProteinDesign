FROM python:3.11-slim
WORKDIR /app
COPY worker/ /app/worker/
RUN pip install --no-cache-dir requests
CMD ["python", "worker/main.py"]
