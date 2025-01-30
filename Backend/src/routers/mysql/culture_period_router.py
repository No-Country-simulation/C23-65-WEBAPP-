from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.culture_period_service import create_culture_period, get_culture_period, update_culture_period, delete_culture_period
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class CulturePeriodCreate(BaseModel):
    name: str

class CulturePeriodUpdate(BaseModel):
    name: str

@router.post("/culture-periods/")
def create_culture_period_route(culture_period_data: CulturePeriodCreate, db: Session = Depends(get_db)):
    return create_culture_period(db, culture_period_data.dict())

@router.get("/culture-periods/{culture_period_id}")
def read_culture_period(culture_period_id: int, db: Session = Depends(get_db)):
    culture_period = get_culture_period(db, culture_period_id)
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return culture_period

@router.put("/culture-periods/{culture_period_id}")
def update_culture_period_route(culture_period_id: int, culture_period_data: CulturePeriodUpdate, db: Session = Depends(get_db)):
    culture_period = update_culture_period(db, culture_period_id, culture_period_data.dict())
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return culture_period

@router.delete("/culture-periods/{culture_period_id}")
def delete_culture_period_route(culture_period_id: int, db: Session = Depends(get_db)):
    culture_period = delete_culture_period(db, culture_period_id)
    if culture_period is None:
        raise HTTPException(status_code=404, detail="CulturePeriod not found")
    return {"message": "CulturePeriod deleted"}