from sqlalchemy.orm import declarative_base

Base = declarative_base()

# import models here so alembic can detect them
from app.models import user, profile, job, job_score