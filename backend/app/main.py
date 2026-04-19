import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from app.api import health, profile,ai

app = FastAPI(title="AI Job Agent")


# Routers
app.include_router(health.router)
app.include_router(profile.router)
app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "AI Job Agent Running"}