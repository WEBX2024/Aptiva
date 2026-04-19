from sqlalchemy import Column, Integer, Float, ForeignKey
from db.base import Base

class JobScore(Base):
    __tablename__ = "job_scores"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Float)