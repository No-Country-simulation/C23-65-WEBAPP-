# like_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import LikeCreate, LikeInDB
from models.mysql_models import Like as LikeDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los likes
@router.get("/likes/", response_model=list[LikeInDB])
def get_likes(db: Session = Depends(get_mysql_db)):
    likes = db.query(LikeDB).all()
    return likes

# Obtener un like por ID
@router.get("/likes/{id}", response_model=LikeInDB)
def get_like(id: int, db: Session = Depends(get_mysql_db)):
    like = db.query(LikeDB).filter(LikeDB.id == id).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    return like

# Crear un nuevo like
@router.post("/likes/", response_model=LikeInDB)
def create_like(like: LikeCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el like ya existe
    db_like = db.query(LikeDB).filter(LikeDB.user_id == like.user_id, LikeDB.gallery_id == like.gallery_id).first()
    if db_like:
        raise HTTPException(status_code=400, detail="User already liked this gallery")

    db_like = LikeDB(user_id=like.user_id, gallery_id=like.gallery_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

# Eliminar un like
@router.delete("/likes/{id}", response_model=LikeInDB)
def delete_like(id: int, db: Session = Depends(get_mysql_db)):
    db_like = db.query(LikeDB).filter(LikeDB.id == id).first()
    if not db_like:
        raise HTTPException(status_code=404, detail="Like not found")

    db.delete(db_like)
    db.commit()
    return db_like
