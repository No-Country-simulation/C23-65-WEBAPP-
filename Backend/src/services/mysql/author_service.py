from sqlalchemy.orm import Session
from src.models.mysql.author import Author

def create_author(db: Session, author_data: dict):
    author = Author(**author_data)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def update_author(db: Session, author_id: int, author_data: dict):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        for key, value in author_data.items():
            setattr(author, key, value)
        db.commit()
        db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
    return author