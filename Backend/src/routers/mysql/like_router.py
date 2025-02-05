from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.like_service import (
    create_like,
    get_like,
    update_like,
    delete_like,
    get_all_likes  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class LikeCreate(BaseModel):
    created_at: datetime
    user_id: int
    gallery_id: int

class LikeUpdate(BaseModel):
    created_at: datetime

# Ruta para crear un like
@router.post("/likes/")
def create_like_route(like: LikeCreate, db: Session = Depends(get_db)):
    return create_like(db, like.dict())

# Ruta para obtener un like por ID
@router.get("/likes/{like_id}")
def read_like(like_id: int, db: Session = Depends(get_db)):
    db_like = get_like(db, like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

# Ruta para obtener todos los likes
@router.get("/likes/")
def read_all_likes(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_likes(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un like
@router.put("/likes/{like_id}")
def update_like_route(like_id: int, like: LikeUpdate, db: Session = Depends(get_db)):
    db_like = update_like(db, like_id, like.dict())
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

# Ruta para eliminar un like
@router.delete("/likes/{like_id}")
def delete_like_route(like_id: int, db: Session = Depends(get_db)):
    db_like = delete_like(db, like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"message": "Like deleted"}