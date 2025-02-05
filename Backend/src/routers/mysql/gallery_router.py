from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.gallery_service import (
    create_gallery,
    get_gallery,
    update_gallery,
    delete_gallery,
    get_all_galleries  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class GalleryCreate(BaseModel):
    title: str
    description: str
    created_at: str
    owner_id: int

class GalleryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Ruta para crear una galería
@router.post("/galleries/")
def create_gallery_route(gallery_data: GalleryCreate, db: Session = Depends(get_db)):
    return create_gallery(db, gallery_data.dict())

# Ruta para obtener una galería por ID
@router.get("/galleries/{gallery_id}")
def read_gallery(gallery_id: int, db: Session = Depends(get_db)):
    gallery = get_gallery(db, gallery_id)
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return gallery

# Ruta para obtener todas las galerías
@router.get("/galleries/")
def read_all_galleries(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_galleries(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar una galería
@router.put("/galleries/{gallery_id}")
def update_gallery_route(gallery_id: int, gallery_data: GalleryUpdate, db: Session = Depends(get_db)):
    gallery = update_gallery(db, gallery_id, gallery_data.dict())
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return gallery

# Ruta para eliminar una galería
@router.delete("/galleries/{gallery_id}")
def delete_gallery_route(gallery_id: int, db: Session = Depends(get_db)):
    gallery = delete_gallery(db, gallery_id)
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return {"message": "Gallery deleted"}