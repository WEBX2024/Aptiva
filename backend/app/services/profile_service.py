from sqlalchemy.orm import Session
from app.models.profile import Profile

def create_profile(db: Session, user_id: int, resume_text: str):
    profile = Profile(user_id=user_id, resume_text=resume_text)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile