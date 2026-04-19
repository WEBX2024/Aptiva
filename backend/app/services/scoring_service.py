from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.models.job import Job
from app.models.job_score import JobScore


def calculate_score(resume_text: str, job_description: str) -> float:
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    overlap = resume_words.intersection(job_words)

    if not job_words:
        return 0.0

    match_ratio = len(overlap) / len(job_words)

    experience_score = match_ratio
    skills_score = match_ratio

    score = (experience_score * 0.6) + (skills_score * 0.4)

    return round(score, 3)


def score_jobs(db: Session, user_id: int):
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        return {"error": "Profile not found"}

    jobs = db.query(Job).all()

    results = []

    for job in jobs:
        score_value = calculate_score(profile.resume_text, job.description)

        job_score = JobScore(
            job_id=job.id,
            user_id=user_id,
            score=score_value
        )

        db.add(job_score)

        results.append({
            "job_id": job.id,
            "title": job.title,
            "score": score_value
        })

    db.commit()

    results.sort(key=lambda x: x["score"], reverse=True)

    return results