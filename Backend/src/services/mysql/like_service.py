from sqlalchemy.orm import Session
from src.models.mysql.like import Like

def create_like(db: Session, like_data: dict):
    like = Like(**like_data)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def get_like(db: Session, like_id: int):
    return db.query(Like).filter(Like.id == like_id).first()

def update_like(db: Session, like_id: int, like_data: dict):
    like = db.query(Like).filter(Like.id == like_id).first()
    if like:
        for key, value in like_data.items():
            setattr(like, key, value)
        db.commit()
        db.refresh(like)
    return like

def delete_like(db: Session, like_id: int):
    like = db.query(Like).filter(Like.id == like_id).first()
    if like:
        db.delete(like)
        db.commit()
    return like