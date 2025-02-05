from fastapi import APIRouter, HTTPException, Query
from src.services.mongo.artpiece_styles_service import (
    create_artpiece_styles,
    get_artpiece_styles,
    update_artpiece_styles,
    delete_artpiece_styles,
    get_all_artpiece_styles  # Importar la nueva función
)
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class ArtpieceStylesCreate(BaseModel):
    artpiece_id: int
    style_id: int

class ArtpieceStylesUpdate(BaseModel):
    style_id: int

# Ruta para crear un artpiece_styles
@router.post("/artpiece-styles/")
def create_artpiece_styles_route(artpiece_styles: ArtpieceStylesCreate):
    artpiece_styles_id = create_artpiece_styles(artpiece_styles.dict())
    return {"id": artpiece_styles_id}

# Ruta para obtener un artpiece_styles por ID
@router.get("/artpiece-styles/{artpiece_styles_id}")
def read_artpiece_styles(artpiece_styles_id: str):
    artpiece_styles = get_artpiece_styles(artpiece_styles_id)
    if artpiece_styles is None:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return artpiece_styles

# Ruta para obtener todos los artpiece_styles
@router.get("/artpiece-styles/")
def read_all_artpiece_styles(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_artpiece_styles(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

# Ruta para actualizar un artpiece_styles
@router.put("/artpiece-styles/{artpiece_styles_id}")
def update_artpiece_styles_route(artpiece_styles_id: str, artpiece_styles: ArtpieceStylesUpdate):
    updated = update_artpiece_styles(artpiece_styles_id, artpiece_styles.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return {"message": "Artpiece Styles updated"}

# Ruta para eliminar un artpiece_styles
@router.delete("/artpiece-styles/{artpiece_styles_id}")
def delete_artpiece_styles_route(artpiece_styles_id: str):
    deleted = delete_artpiece_styles(artpiece_styles_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return {"message": "Artpiece Styles deleted"}