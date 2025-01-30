from sqlalchemy.orm import Session
from src.models.mysql.medium import Medium

def create_medium(db: Session, medium_data: dict):
    medium = Medium(**medium_data)
    db.add(medium)
    db.commit()
    db.refresh(medium)
    return medium

def get_medium(db: Session, medium_id: int):
    return db.query(Medium).filter(Medium.id == medium_id).first()

def update_medium(db: Session, medium_id: int, medium_data: dict):
    medium = db.query(Medium).filter(Medium.id == medium_id).first()
    if medium:
        for key, value in medium_data.items():
            setattr(medium, key, value)
        db.commit()
        db.refresh(medium)
    return medium

def delete_medium(db: Session, medium_id: int):
    medium = db.query(Medium).filter(Medium.id == medium_id).first()
    if medium:
        db.delete(medium)
        db.commit()
    return medium