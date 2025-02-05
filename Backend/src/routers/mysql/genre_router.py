from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.genre_service import (
    create_genre,
    get_genre,
    update_genre,
    delete_genre,
    get_all_genres  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class GenreCreate(BaseModel):
    name: str

class GenreUpdate(BaseModel):
    name: str

# Ruta para crear un género
@router.post("/genres/")
def create_genre_route(genre_data: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, genre_data.dict())

# Ruta para obtener un género por ID
@router.get("/genres/{genre_id}")
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = get_genre(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

# Ruta para obtener todos los géneros
@router.get("/genres/")
def read_all_genres(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_genres(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un género
@router.put("/genres/{genre_id}")
def update_genre_route(genre_id: int, genre_data: GenreUpdate, db: Session = Depends(get_db)):
    genre = update_genre(db, genre_id, genre_data.dict())
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

# Ruta para eliminar un género
@router.delete("/genres/{genre_id}")
def delete_genre_route(genre_id: int, db: Session = Depends(get_db)):
    genre = delete_genre(db, genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {"message": "Genre deleted"}