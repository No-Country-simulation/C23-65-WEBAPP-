from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.mysql.comment import Comment

def create_comment(db: Session, comment_data: dict):
    comment = Comment(**comment_data)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_all_comments(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filter_by: dict = None,
    order_by: str = None
):
    try:
        query = db.query(Comment)

        if filter_by:
            query = query.filter_by(**filter_by)

        if order_by:
            query = query.order_by(order_by)

        return query.offset(skip).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"Error al obtener comentarios: {e}")
        return []

def update_comment(db: Session, comment_id: int, comment_data: dict):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        for key, value in comment_data.items():
            setattr(comment, key, value)
        db.commit()
        db.refresh(comment)
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
    return comment