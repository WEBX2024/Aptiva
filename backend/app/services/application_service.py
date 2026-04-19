from sqlalchemy.orm import Session
from app.models.profile import Profile
from ai.chains.application_chain import generate_answer


def get_application_answer(db: Session, user_id: int, question: str):
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        return {"error": "Profile not found"}

    answer = generate_answer(profile.resume_text, question)

    return {
        "answer": answer
    }