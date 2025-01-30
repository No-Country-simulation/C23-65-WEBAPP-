from sqlalchemy.orm import Session
from src.models.mysql.favorite import Favorite

def create_favorite(db: Session, favorite_data: dict):
    favorite = Favorite(**favorite_data)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

def get_favorite(db: Session, favorite_id: int):
    return db.query(Favorite).filter(Favorite.id == favorite_id).first()

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