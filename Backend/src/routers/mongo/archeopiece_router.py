from fastapi import APIRouter, HTTPException, Query
from src.services.mongo.archeopiece_service import (
    create_archeopiece,
    get_archeopiece,
    update_archeopiece,
    delete_archeopiece,
    get_all_archeopieces  # Importar la nueva función
)
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class ArcheopieceCreate(BaseModel):
    name: str
    object_type: str
    production_date: str
    material: str
    technique: str
    dimensions: str
    description: str
    findspot: str
    current_location: str
    culture_period_id: int

class ArcheopieceUpdate(BaseModel):
    name: str
    description: str

# Ruta para crear un archeopiece
@router.post("/archeopieces/")
def create_archeopiece_route(archeopiece: ArcheopieceCreate):
    archeopiece_id = create_archeopiece(archeopiece.dict())
    return {"id": archeopiece_id}

# Ruta para obtener un archeopiece por ID
@router.get("/archeopieces/{archeopiece_id}")
def read_archeopiece(archeopiece_id: str):
    archeopiece = get_archeopiece(archeopiece_id)
    if archeopiece is None:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return archeopiece

# Ruta para obtener todos los archeopieces
@router.get("/archeopieces/")
def read_all_archeopieces(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_archeopieces(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

# Ruta para actualizar un archeopiece
@router.put("/archeopieces/{archeopiece_id}")
def update_archeopiece_route(archeopiece_id: str, archeopiece: ArcheopieceUpdate):
    updated = update_archeopiece(archeopiece_id, archeopiece.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return {"message": "Archeopiece updated"}

# Ruta para eliminar un archeopiece
@router.delete("/archeopieces/{archeopiece_id}")
def delete_archeopiece_route(archeopiece_id: str):
    deleted = delete_archeopiece(archeopiece_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return {"message": "Archeopiece deleted"}