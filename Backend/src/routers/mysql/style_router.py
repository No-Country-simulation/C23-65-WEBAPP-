from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.style_service import (
    create_style,
    get_style,
    update_style,
    delete_style,
    get_all_style
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

class StyleCreate(BaseModel):
    name: str

class StyleUpdate(BaseModel):
    name: str

@router.post("/styles/")
def create_style_route(style_data: StyleCreate, db: Session = Depends(get_db)):
    return create_style(db, style_data.dict())

@router.get("/styles/{style_id}")
def read_style(style_id: int, db: Session = Depends(get_db)):
    style = get_style(db, style_id)
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    return style

# Ruta para obtener todos los likes
@router.get("/styles/")
def read_all_styles(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_style(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

@router.put("/styles/{style_id}")
def update_style_route(style_id: int, style_data: StyleUpdate, db: Session = Depends(get_db)):
    style = update_style(db, style_id, style_data.dict())
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    return style

@router.delete("/styles/{style_id}")
def delete_style_route(style_id: int, db: Session = Depends(get_db)):
    style = delete_style(db, style_id)
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    return {"message": "Style deleted"}