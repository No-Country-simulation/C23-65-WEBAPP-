from sqlalchemy.orm import Session
from src.models.mysql.artpiece import Artpiece

def create_artpiece(db: Session, artpiece_data: dict):
    artpiece = Artpiece(**artpiece_data)
    db.add(artpiece)
    db.commit()
    db.refresh(artpiece)
    return artpiece

def get_artpiece(db: Session, artpiece_id: int):
    return db.query(Artpiece).filter(Artpiece.id == artpiece_id).first()

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def get_all_artpiece(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Artpiece)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener artpieces: {e}")
        return []

def update_artpiece(db: Session, artpiece_id: int, artpiece_data: dict):
    artpiece = db.query(Artpiece).filter(Artpiece.id == artpiece_id).first()
    if artpiece:
        for key, value in artpiece_data.items():
            setattr(artpiece, key, value)
        db.commit()
        db.refresh(artpiece)
    return artpiece

def delete_artpiece(db: Session, artpiece_id: int):
    artpiece = db.query(Artpiece).filter(Artpiece.id == artpiece_id).first()
    if artpiece:
        db.delete(artpiece)
        db.commit()
    return artpiece