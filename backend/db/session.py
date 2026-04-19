import os
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get project root (ai-job-agent/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_config_path = os.path.join(BASE_DIR, "infra", "database.yaml")

with open(db_config_path, "r") as f:
    config = yaml.safe_load(f)

DATABASE_URL = config["database"]["url"]

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)