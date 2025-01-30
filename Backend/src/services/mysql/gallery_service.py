from sqlalchemy.orm import Session
from src.models.mysql.gallery import Gallery

def create_gallery(db: Session, gallery_data: dict):
    gallery = Gallery(**gallery_data)
    db.add(gallery)
    db.commit()
    db.refresh(gallery)
    return gallery

def get_gallery(db: Session, gallery_id: int):
    return db.query(Gallery).filter(Gallery.id == gallery_id).first()

def update_gallery(db: Session, gallery_id: int, gallery_data: dict):
    gallery = db.query(Gallery).filter(Gallery.id == gallery_id).first()
    if gallery:
        for key, value in gallery_data.items():
            setattr(gallery, key, value)
        db.commit()
        db.refresh(gallery)
    return gallery

def delete_gallery(db: Session, gallery_id: int):
    gallery = db.query(Gallery).filter(Gallery.id == gallery_id).first()
    if gallery:
        db.delete(gallery)
        db.commit()
    return gallery