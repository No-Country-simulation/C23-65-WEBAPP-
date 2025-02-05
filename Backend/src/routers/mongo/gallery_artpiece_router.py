from fastapi import APIRouter, HTTPException, Query
from src.services.mongo.gallery_artpiece_service import (
    create_gallery_artpiece,
    get_gallery_artpiece,
    update_gallery_artpiece,
    delete_gallery_artpiece,
    get_all_gallery_artpieces  # Importar la nueva función
)
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class GalleryArtpieceCreate(BaseModel):
    gallery_id: int
    artpiece_id: int
    note: str

class GalleryArtpieceUpdate(BaseModel):
    note: str

# Ruta para crear un gallery_artpiece
@router.post("/gallery-artpieces/")
def create_gallery_artpiece_route(gallery_artpiece: GalleryArtpieceCreate):
    gallery_artpiece_id = create_gallery_artpiece(gallery_artpiece.dict())
    return {"id": gallery_artpiece_id}

# Ruta para obtener un gallery_artpiece por ID
@router.get("/gallery-artpieces/{gallery_artpiece_id}")
def read_gallery_artpiece(gallery_artpiece_id: str):
    gallery_artpiece = get_gallery_artpiece(gallery_artpiece_id)
    if gallery_artpiece is None:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return gallery_artpiece

# Ruta para obtener todos los gallery_artpieces
@router.get("/gallery-artpieces/")
def read_all_gallery_artpieces(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_gallery_artpieces(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

# Ruta para actualizar un gallery_artpiece
@router.put("/gallery-artpieces/{gallery_artpiece_id}")
def update_gallery_artpiece_route(gallery_artpiece_id: str, gallery_artpiece: GalleryArtpieceUpdate):
    updated = update_gallery_artpiece(gallery_artpiece_id, gallery_artpiece.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return {"message": "Gallery Artpiece updated"}

# Ruta para eliminar un gallery_artpiece
@router.delete("/gallery-artpieces/{gallery_artpiece_id}")
def delete_gallery_artpiece_route(gallery_artpiece_id: str):
    deleted = delete_gallery_artpiece(gallery_artpiece_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return {"message": "Gallery Artpiece deleted"}