FROM python:3.11-slim
WORKDIR /app
# copy only the hub service code
COPY hub/ /app/hub/
RUN pip install --no-cache-dir fastapi uvicorn[standard]
EXPOSE 8000
CMD ["uvicorn", "hub.main:app", "--host", "0.0.0.0", "--port", "8000"]
