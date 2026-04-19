from fastapi import FastAPI
from app.api import health, profile

app = FastAPI(title="AI Job Agent")

app.include_router(health.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {"message": "AI Job Agent Running"}