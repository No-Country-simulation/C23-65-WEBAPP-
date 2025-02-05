from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.profile import Profile

def create_profile(db: Session, profile_data: dict):
    profile = Profile(**profile_data)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def get_all_profile(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Profile)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener perfiles: {e}")
        return []

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