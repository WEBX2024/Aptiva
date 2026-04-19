from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.job_service import create_mock_jobs

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("/discover")
def discover_jobs(query: str, db: Session = Depends(get_db)):
    jobs = create_mock_jobs(db, query)

    return {
        "jobs": [
            {
                "id": job.id,
                "title": job.title,
                "description": job.description
            }
            for job in jobs
        ]
    }