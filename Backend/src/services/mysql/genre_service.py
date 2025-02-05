from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.genre import Genre

def create_genre(db: Session, genre_data: dict):
    genre = Genre(**genre_data)
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre

def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()

def get_all_genres(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Genre)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener géneros: {e}")
        return []

def update_genre(db: Session, genre_id: int, genre_data: dict):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        for key, value in genre_data.items():
            setattr(genre, key, value)
        db.commit()
        db.refresh(genre)
    return genre

def delete_genre(db: Session, genre_id: int):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre:
        db.delete(genre)
        db.commit()
    return genre