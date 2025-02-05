from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.gallery import Gallery

def create_gallery(db: Session, gallery_data: dict):
    gallery = Gallery(**gallery_data)
    db.add(gallery)
    db.commit()
    db.refresh(gallery)
    return gallery

def get_gallery(db: Session, gallery_id: int):
    return db.query(Gallery).filter(Gallery.id == gallery_id).first()

def get_all_galleries(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Gallery)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener galerías: {e}")
        return []

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