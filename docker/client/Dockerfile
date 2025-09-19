FROM --platform=linux/amd64 node:18-slim

WORKDIR /app

# Install http-server globally
RUN npm install -g --unsafe-perm http-server

# Copy client code into container
COPY . /app

EXPOSE 8081

# Default command: serve app on port 8081
CMD ["http-server", ".", "-p", "8081"]
