from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.services.profile_service import create_profile
from app.schemas.profile import ProfileResponse

router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("/upload", response_model=ProfileResponse)
async def upload_profile(
    user_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files supported")

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file encoding")

    profile = create_profile(db, user_id=user_id, resume_text=text)

    return profile