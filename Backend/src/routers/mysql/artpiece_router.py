from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.artpiece_service import (
    create_artpiece,
    get_artpiece,
    update_artpiece,
    delete_artpiece,
    get_all_artpiece  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class ArtpieceCreate(BaseModel):
    title: str
    year: int
    dimension: str
    author_id: int
    medium_id: int

class ArtpieceUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None
    dimension: Optional[str] = None

# Ruta para crear un artpiece
@router.post("/artpieces/")
def create_artpiece_route(artpiece_data: ArtpieceCreate, db: Session = Depends(get_db)):
    return create_artpiece(db, artpiece_data.dict())

# Ruta para obtener un artpiece por ID
@router.get("/artpieces/{artpiece_id}")
def read_artpiece(artpiece_id: int, db: Session = Depends(get_db)):
    artpiece = get_artpiece(db, artpiece_id)
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return artpiece

# Ruta para obtener todos los artpieces
@router.get("/artpieces/")
def read_all_artpieces(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_artpiece(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un artpiece
@router.put("/artpieces/{artpiece_id}")
def update_artpiece_route(artpiece_id: int, artpiece_data: ArtpieceUpdate, db: Session = Depends(get_db)):
    artpiece = update_artpiece(db, artpiece_id, artpiece_data.dict())
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return artpiece

# Ruta para eliminar un artpiece
@router.delete("/artpieces/{artpiece_id}")
def delete_artpiece_route(artpiece_id: int, db: Session = Depends(get_db)):
    artpiece = delete_artpiece(db, artpiece_id)
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return {"message": "Artpiece deleted"}