# genre_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import GenreCreate, GenreInDB
from models.mysql_models import Genre as GenreDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los géneros
@router.get("/genres/", response_model=list[GenreInDB])
def get_genres(db: Session = Depends(get_mysql_db)):
    genres = db.query(GenreDB).all()
    return genres

# Obtener un género por ID
@router.get("/genres/{id}", response_model=GenreInDB)
def get_genre(id: int, db: Session = Depends(get_mysql_db)):
    genre = db.query(GenreDB).filter(GenreDB.id == id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

# Crear un nuevo género
@router.post("/genres/", response_model=GenreInDB)
def create_genre(genre: GenreCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el género ya existe
    db_genre = db.query(GenreDB).filter(GenreDB.name == genre.name).first()
    if db_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")

    # Crear el género
    db_genre = GenreDB(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

# Actualizar un género
@router.put("/genres/{id}", response_model=GenreInDB)
def update_genre(id: int, genre: GenreCreate, db: Session = Depends(get_mysql_db)):
    db_genre = db.query(GenreDB).filter(GenreDB.id == id).first()
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    db_genre.name = genre.name

    db.commit()
    db.refresh(db_genre)
    return db_genre

# Eliminar un género
@router.delete("/genres/{id}", response_model=GenreInDB)
def delete_genre(id: int, db: Session = Depends(get_mysql_db)):
    db_genre = db.query(GenreDB).filter(GenreDB.id == id).first()
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    db.delete(db_genre)
    db.commit()
    return db_genre
