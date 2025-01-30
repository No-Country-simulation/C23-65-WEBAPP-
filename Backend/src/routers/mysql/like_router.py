from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.like_service import create_like, get_like, update_like, delete_like
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class LikeCreate(BaseModel):
    created_at: datetime
    user_id: int
    gallery_id: int

class LikeUpdate(BaseModel):
    created_at: datetime

@router.post("/likes/")
def create_like_route(like: LikeCreate, db: Session = Depends(get_db)):
    return create_like(db, like.dict())

@router.get("/likes/{like_id}")
def read_like(like_id: int, db: Session = Depends(get_db)):
    db_like = get_like(db, like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

@router.put("/likes/{like_id}")
def update_like_route(like_id: int, like: LikeUpdate, db: Session = Depends(get_db)):
    db_like = update_like(db, like_id, like.dict())
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

@router.delete("/likes/{like_id}")
def delete_like_route(like_id: int, db: Session = Depends(get_db)):
    db_like = delete_like(db, like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"message": "Like deleted"}