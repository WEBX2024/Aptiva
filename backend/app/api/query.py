from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.query_service import get_search_queries

router = APIRouter(prefix="/query", tags=["query"])


@router.get("/generate")
def generate_query_api(user_id: int, db: Session = Depends(get_db)):
    return get_search_queries(db, user_id)