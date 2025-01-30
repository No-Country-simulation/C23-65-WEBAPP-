from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.genre_service import create_genre, get_genre, update_genre, delete_genre
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class GenreCreate(BaseModel):
    name: str

class GenreUpdate(BaseModel):
    name: str

@router.post("/genres/")
def create_genre_route(genre_data: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, genre_data.dict())

@router.get("/genres/{genre_id}")
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = get_genre(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.put("/genres/{genre_id}")
def update_genre_route(genre_id: int, genre_data: GenreUpdate, db: Session = Depends(get_db)):
    genre = update_genre(db, genre_id, genre_data.dict())
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.delete("/genres/{genre_id}")
def delete_genre_route(genre_id: int, db: Session = Depends(get_db)):
    genre = delete_genre(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {"message": "Genre deleted"}