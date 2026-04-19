from pydantic import BaseModel

class ProfileResponse(BaseModel):
    id: int
    user_id: int
    resume_text: str

    class Config:
        from_attributes = True