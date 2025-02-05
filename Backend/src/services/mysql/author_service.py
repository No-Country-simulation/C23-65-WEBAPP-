from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.author import Author

def create_author(db: Session, author_data: dict):
    author = Author(**author_data)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_all_author(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Author)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener autores: {e}")
        return []

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