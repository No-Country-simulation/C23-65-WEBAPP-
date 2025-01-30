from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.comment_service import create_comment, get_comment, update_comment, delete_comment
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class CommentCreate(BaseModel):
    content: str
    created_at: datetime
    user_id: int
    gallery_id: int

class CommentUpdate(BaseModel):
    content: str

@router.post("/comments/")
def create_comment_route(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db, comment.dict())

@router.get("/comments/{comment_id}")
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.put("/comments/{comment_id}")
def update_comment_route(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)):
    db_comment = update_comment(db, comment_id, comment.dict())
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.delete("/comments/{comment_id}")
def delete_comment_route(comment_id: int, db: Session = Depends(get_db)):
    db_comment = delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"}