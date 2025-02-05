from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.medium import Medium

def create_medium(db: Session, medium_data: dict):
    medium = Medium(**medium_data)
    db.add(medium)
    db.commit()
    db.refresh(medium)
    return medium

def get_medium(db: Session, medium_id: int):
    return db.query(Medium).filter(Medium.id == medium_id).first()

def get_all_medium(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Medium)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener medios: {e}")
        return []

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