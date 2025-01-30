from sqlalchemy.orm import Session
from src.models.mysql.profile import Profile

def create_profile(db: Session, profile_data: dict):
    profile = Profile(**profile_data)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def update_profile(db: Session, profile_id: int, profile_data: dict):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if profile:
        for key, value in profile_data.items():
            setattr(profile, key, value)
        db.commit()
        db.refresh(profile)
    return profile

def delete_profile(db: Session, profile_id: int):
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if profile:
        db.delete(profile)
        db.commit()
    return profile