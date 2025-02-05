from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.favorite import Favorite

def create_favorite(db: Session, favorite_data: dict):
    favorite = Favorite(**favorite_data)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

def get_favorite(db: Session, favorite_id: int):
    return db.query(Favorite).filter(Favorite.id == favorite_id).first()

def get_all_favorites(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Favorite)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener favoritos: {e}")
        return []

def update_favorite(db: Session, favorite_id: int, favorite_data: dict):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if favorite:
        for key, value in favorite_data.items():
            setattr(favorite, key, value)
        db.commit()
        db.refresh(favorite)
    return favorite

def delete_favorite(db: Session, favorite_id: int):
    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()
    if favorite:
        db.delete(favorite)
        db.commit()
    return favorite