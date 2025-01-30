from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.favorite_service import create_favorite, get_favorite, update_favorite, delete_favorite
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class FavoriteCreate(BaseModel):
    created_at: datetime
    archeopiece_id: int
    artpiece_id: int
    gallery_id: int
    user_id: int

class FavoriteUpdate(BaseModel):
    created_at: datetime

@router.post("/favorites/")
def create_favorite_route(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return create_favorite(db, favorite.dict())

@router.get("/favorites/{favorite_id}")
def read_favorite(favorite_id: int, db: Session = Depends(get_db)):
    db_favorite = get_favorite(db, favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return db_favorite

@router.put("/favorites/{favorite_id}")
def update_favorite_route(favorite_id: int, favorite: FavoriteUpdate, db: Session = Depends(get_db)):
    db_favorite = update_favorite(db, favorite_id, favorite.dict())
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return db_favorite

@router.delete("/favorites/{favorite_id}")
def delete_favorite_route(favorite_id: int, db: Session = Depends(get_db)):
    db_favorite = delete_favorite(db, favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"message": "Favorite deleted"}