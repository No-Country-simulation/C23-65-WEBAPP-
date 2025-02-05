from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.favorite_service import (
    create_favorite,
    get_favorite,
    update_favorite,
    delete_favorite,
    get_all_favorites  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class FavoriteCreate(BaseModel):
    created_at: datetime
    archeopiece_id: int
    artpiece_id: int
    gallery_id: int
    user_id: int

class FavoriteUpdate(BaseModel):
    created_at: datetime

# Ruta para crear un favorito
@router.post("/favorites/")
def create_favorite_route(favorite: FavoriteCreate, db: Session = Depends(get_db)):
    return create_favorite(db, favorite.dict())

# Ruta para obtener un favorito por ID
@router.get("/favorites/{favorite_id}")
def read_favorite(favorite_id: int, db: Session = Depends(get_db)):
    db_favorite = get_favorite(db, favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return db_favorite

# Ruta para obtener todos los favoritos
@router.get("/favorites/")
def read_all_favorites(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_favorites(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un favorito
@router.put("/favorites/{favorite_id}")
def update_favorite_route(favorite_id: int, favorite: FavoriteUpdate, db: Session = Depends(get_db)):
    db_favorite = update_favorite(db, favorite_id, favorite.dict())
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return db_favorite

# Ruta para eliminar un favorito
@router.delete("/favorites/{favorite_id}")
def delete_favorite_route(favorite_id: int, db: Session = Depends(get_db)):
    db_favorite = delete_favorite(db, favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"message": "Favorite deleted"}