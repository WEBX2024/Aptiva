from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.ai_service import get_role_recommendations

router = APIRouter(prefix="/ai", tags=["ai"])


@router.get("/recommend-roles")
def recommend_roles_api(user_id: int, db: Session = Depends(get_db)):
    return get_role_recommendations(db, user_id)