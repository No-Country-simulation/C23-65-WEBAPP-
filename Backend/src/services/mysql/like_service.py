from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.like import Like

def create_like(db: Session, like_data: dict):
    like = Like(**like_data)
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

def get_like(db: Session, like_id: int):
    return db.query(Like).filter(Like.id == like_id).first()

def get_all_likes(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Like)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener likes: {e}")
        return []

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