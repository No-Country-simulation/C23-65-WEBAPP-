from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.author_service import create_author, get_author, update_author, delete_author
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class AuthorCreate(BaseModel):
    name: str
    birth_date: str
    death_date: str
    nationality: str

class AuthorUpdate(BaseModel):
    name: str
    birth_date: str
    death_date: str
    nationality: str

@router.post("/authors/")
def create_author_route(author_data: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author_data.dict())

@router.get("/authors/{author_id}")
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/authors/{author_id}")
def update_author_route(author_id: int, author_data: AuthorUpdate, db: Session = Depends(get_db)):
    author = update_author(db, author_id, author_data.dict())
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.delete("/authors/{author_id}")
def delete_author_route(author_id: int, db: Session = Depends(get_db)):
    author = delete_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted"}