FROM python:3.11-slim
WORKDIR /app
COPY client/ /app/client/
RUN pip install --no-cache-dir requests
CMD ["python", "client/main.py"]
