from sqlalchemy.orm import Session
from src.models.mysql.comment import Comment

def create_comment(db: Session, comment_data: dict):
    comment = Comment(**comment_data)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

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