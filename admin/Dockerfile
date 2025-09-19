# Force amd64 architecture for Node
FROM --platform=linux/amd64 node:18-slim

WORKDIR /app

# Show Node + npm version to confirm install works
RUN node -v && npm -v

# Install http-server safely
RUN npm install -g --unsafe-perm http-server

# Copy admin files into container
COPY . /app

EXPOSE 3000

# Default command: run http-server on port 3000
CMD ["http-server", ".", "-p", "3000"]
