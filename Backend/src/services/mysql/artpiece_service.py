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