from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.culture_period_service import (
    create_culture_period,
    get_culture_period,
    update_culture_period,
    delete_culture_period,
    get_all_culture_periods  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class CulturePeriodCreate(BaseModel):
    name: str

class CulturePeriodUpdate(BaseModel):
    name: str

# Ruta para crear un periodo cultural
@router.post("/culture-periods/")
def create_culture_period_route(culture_period_data: CulturePeriodCreate, db: Session = Depends(get_db)):
    return create_culture_period(db, culture_period_data.dict())

# Ruta para obtener un periodo cultural por ID
@router.get("/culture-periods/{culture_period_id}")
def read_culture_period(culture_period_id: int, db: Session = Depends(get_db)):
    culture_period = get_culture_period(db, culture_period_id)
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return culture_period

# Ruta para obtener todos los periodos culturales
@router.get("/culture-periods/")
def read_all_culture_periods(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_culture_periods(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un periodo cultural
@router.put("/culture-periods/{culture_period_id}")
def update_culture_period_route(culture_period_id: int, culture_period_data: CulturePeriodUpdate, db: Session = Depends(get_db)):
    culture_period = update_culture_period(db, culture_period_id, culture_period_data.dict())
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return culture_period

# Ruta para eliminar un periodo cultural
@router.delete("/culture-periods/{culture_period_id}")
def delete_culture_period_route(culture_period_id: int, db: Session = Depends(get_db)):
    culture_period = delete_culture_period(db, culture_period_id)
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return {"message": "CulturePeriod deleted"}