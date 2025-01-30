from fastapi import APIRouter, HTTPException
from src.services.mongo.archeopiece_service import create_archeopiece, get_archeopiece, update_archeopiece, delete_archeopiece
from pydantic import BaseModel

router = APIRouter()

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

@router.post("/archeopieces/")
def create_archeopiece_route(archeopiece: ArcheopieceCreate):
    archeopiece_id = create_archeopiece(archeopiece.dict())
    return {"id": archeopiece_id}

@router.get("/archeopieces/{archeopiece_id}")
def read_archeopiece(archeopiece_id: str):
    archeopiece = get_archeopiece(archeopiece_id)
    if archeopiece is None:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return archeopiece

@router.put("/archeopieces/{archeopiece_id}")
def update_archeopiece_route(archeopiece_id: str, archeopiece: ArcheopieceUpdate):
    updated = update_archeopiece(archeopiece_id, archeopiece.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return {"message": "Archeopiece updated"}

@router.delete("/archeopieces/{archeopiece_id}")
def delete_archeopiece_route(archeopiece_id: str):
    deleted = delete_archeopiece(archeopiece_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return {"message": "Archeopiece deleted"}