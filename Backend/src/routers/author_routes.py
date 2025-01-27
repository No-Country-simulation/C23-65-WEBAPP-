# author_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import AuthorCreate, AuthorInDB
from models.mysql_models import Author as AuthorDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los autores
@router.get("/authors/", response_model=list[AuthorInDB])
def get_authors(db: Session = Depends(get_mysql_db)):
    authors = db.query(AuthorDB).all()
    return authors

# Obtener un autor por ID
@router.get("/authors/{id}", response_model=AuthorInDB)
def get_author(id: int, db: Session = Depends(get_mysql_db)):
    author = db.query(AuthorDB).filter(AuthorDB.id == id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Crear un nuevo autor
@router.post("/authors/", response_model=AuthorInDB)
def create_author(author: AuthorCreate, db: Session = Depends(get_mysql_db)):
    db_author = db.query(AuthorDB).filter(AuthorDB.name == author.name).first()
    if db_author:
        raise HTTPException(status_code=400, detail="Author already exists")
    
    db_author = AuthorDB(
        name=author.name,
        birth_date=author.birth_date,
        death_date=author.death_date,
        nationality=author.nationality
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

# Actualizar un autor
@router.put("/authors/{id}", response_model=AuthorInDB)
def update_author(id: int, author: AuthorCreate, db: Session = Depends(get_mysql_db)):
    db_author = db.query(AuthorDB).filter(AuthorDB.id == id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    db_author.name = author.name
    db_author.birth_date = author.birth_date
    db_author.death_date = author.death_date
    db_author.nationality = author.nationality

    db.commit()
    db.refresh(db_author)
    return db_author

# Eliminar un autor
@router.delete("/authors/{id}", response_model=AuthorInDB)
def delete_author(id: int, db: Session = Depends(get_mysql_db)):
    db_author = db.query(AuthorDB).filter(AuthorDB.id == id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(db_author)
    db.commit()
    return db_author