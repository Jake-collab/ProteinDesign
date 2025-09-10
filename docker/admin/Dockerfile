FROM node:18
WORKDIR /app
RUN npm install -g http-server
COPY admin/ /app/admin/
EXPOSE 3000
CMD ["http-server", "admin", "-p", "3000", "-a", "0.0.0.0"]
