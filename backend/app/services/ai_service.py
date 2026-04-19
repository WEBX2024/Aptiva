from sqlalchemy.orm import Session
from app.models.profile import Profile
from ai.chains.role_chain import recommend_roles

def get_role_recommendations(db: Session, user_id: int):
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        return {"error": "Profile not found"}

    result = recommend_roles(profile.resume_text)

    return {
        "recommendations": result
    }