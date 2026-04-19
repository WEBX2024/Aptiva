from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.scoring_service import score_jobs

router = APIRouter(prefix="/score", tags=["scoring"])


@router.post("/jobs")
def score_jobs_api(user_id: int, db: Session = Depends(get_db)):
    return score_jobs(db, user_id)