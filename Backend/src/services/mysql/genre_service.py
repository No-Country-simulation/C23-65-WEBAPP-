from sqlalchemy.orm import Session
from src.models.mysql.genre import Genre

def create_genre(db: Session, genre_data: dict):
    genre = Genre(**genre_data)
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre

def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()

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