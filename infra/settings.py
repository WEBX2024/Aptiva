import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "AI Job Agent"
    ENV = os.getenv("ENV", "development")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()