# 🕒 SimpleTimeService

A minimal microservice built with Flask that returns the current UTC timestamp and the IP address of the client in JSON format.

---

## 📦 Features

- Returns the current UTC time in ISO 8601 format
- Returns the IP address of the requester
- Built with Python + Flask
- Dockerized and runs as a non-root user for better security

---

## 🧪 JSON Response Format

When you send a GET request to `/`, the service responds with:

```json
{
  "timestamp": "2025-04-15T11:00:00.000Z",
  "ip": "192.168.1.101"
}

```
# Create a folder and pull the repo for development purpose:

mkdir app
cd app
git init
git pull https://github.com/sumitronaldo/SimpleTimeService.git


# Execute below commands with docker engine installed to pull and test the app:

docker pull sumitronaldo111/simple-time-service:latest

docker run -p 5000:5000 sumitronaldo111/simple-time-service
