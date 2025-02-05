from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.medium_service import (
    create_medium,
    get_medium,
    update_medium,
    delete_medium,
    get_all_medium
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

class MediumCreate(BaseModel):
    name: str

class MediumUpdate(BaseModel):
    name: str

@router.post("/mediums/")
def create_medium_route(medium_data: MediumCreate, db: Session = Depends(get_db)):
    return create_medium(db, medium_data.dict())

@router.get("/mediums/{medium_id}")
def read_medium(medium_id: int, db: Session = Depends(get_db)):
    medium = get_medium(db, medium_id)
    if medium is None:
        raise HTTPException(status_code=404, detail="Medium not found")
    return medium

# Ruta para obtener todos los likes
@router.get("/mediums/")
def read_all_mediums(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_medium(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

@router.put("/mediums/{medium_id}")
def update_medium_route(medium_id: int, medium_data: MediumUpdate, db: Session = Depends(get_db)):
    medium = update_medium(db, medium_id, medium_data.dict())
    if medium is None:
        raise HTTPException(status_code=404, detail="Medium not found")
    return medium

@router.delete("/mediums/{medium_id}")
def delete_medium_route(medium_id: int, db: Session = Depends(get_db)):
    medium = delete_medium(db, medium_id)
    if medium is None:
        raise HTTPException(status_code=404, detail="Medium not found")
    return {"message": "Medium deleted"}