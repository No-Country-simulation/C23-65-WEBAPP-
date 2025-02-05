from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.author_service import create_author, get_author, update_author, delete_author, get_all_author
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

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

# Ruta para obtener todos los comentarios
@router.get("/authors/")
def read_all_authors(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_author(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

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