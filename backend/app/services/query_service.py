from sqlalchemy.orm import Session
from app.models.profile import Profile
from ai.chains.query_chain import generate_queries

def get_search_queries(db: Session, user_id: int):
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        return {"error": "Profile not found"}

    result = generate_queries(profile.resume_text)

    return {
        "queries": result
    }