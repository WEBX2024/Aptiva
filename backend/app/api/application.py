from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.application_service import get_application_answer

router = APIRouter(prefix="/application", tags=["application"])


@router.post("/answer")
def answer_question(
    user_id: int,
    question: str,
    db: Session = Depends(get_db)
):
    return get_application_answer(db, user_id, question)