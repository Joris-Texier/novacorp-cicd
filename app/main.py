from fastapi import FastAPI
import os
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": "NovaCorp API",
        "version": "1.2.0",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/config")
def config():
    return {
        "environment": os.getenv("APP_ENV", "development"),
        "database_host": os.getenv("DB_HOST", "not-configured")
    }
