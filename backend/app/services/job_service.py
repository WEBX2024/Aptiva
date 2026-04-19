from sqlalchemy.orm import Session
from app.models.job import Job

def create_mock_jobs(db: Session, query: str):
    jobs = []

    # Simple mock generation
    for i in range(3):
        job = Job(
            title=f"{query} Role {i+1}",
            description=f"Job description for {query} role {i+1}"
        )
        db.add(job)
        jobs.append(job)

    db.commit()

    for job in jobs:
        db.refresh(job)

    return jobs