# cultureperiod_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import CulturePeriodCreate, CulturePeriodInDB
from models.mysql_models import CulturePeriod as CulturePeriodDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los periodos culturales
@router.get("/culture_periods/", response_model=list[CulturePeriodInDB])
def get_culture_periods(db: Session = Depends(get_mysql_db)):
    culture_periods = db.query(CulturePeriodDB).all()
    return culture_periods

# Obtener un periodo cultural por ID
@router.get("/culture_periods/{id}", response_model=CulturePeriodInDB)
def get_culture_period(id: int, db: Session = Depends(get_mysql_db)):
    culture_period = db.query(CulturePeriodDB).filter(CulturePeriodDB.id == id).first()
    if not culture_period:
        raise HTTPException(status_code=404, detail="Culture Period not found")
    return culture_period

# Crear un nuevo periodo cultural
@router.post("/culture_periods/", response_model=CulturePeriodInDB)
def create_culture_period(culture_period: CulturePeriodCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el periodo cultural ya existe por nombre
    db_culture_period = db.query(CulturePeriodDB).filter(CulturePeriodDB.name == culture_period.name).first()
    if db_culture_period:
        raise HTTPException(status_code=400, detail="Culture Period with this name already exists")
    
    db_culture_period = CulturePeriodDB(name=culture_period.name)
    db.add(db_culture_period)
    db.commit()
    db.refresh(db_culture_period)
    return db_culture_period

# Actualizar un periodo cultural
@router.put("/culture_periods/{id}", response_model=CulturePeriodInDB)
def update_culture_period(id: int, culture_period: CulturePeriodCreate, db: Session = Depends(get_mysql_db)):
    db_culture_period = db.query(CulturePeriodDB).filter(CulturePeriodDB.id == id).first()
    if not db_culture_period:
        raise HTTPException(status_code=404, detail="Culture Period not found")

    db_culture_period.name = culture_period.name

    db.commit()
    db.refresh(db_culture_period)
    return db_culture_period

# Eliminar un periodo cultural
@router.delete("/culture_periods/{id}", response_model=CulturePeriodInDB)
def delete_culture_period(id: int, db: Session = Depends(get_mysql_db)):
    db_culture_period = db.query(CulturePeriodDB).filter(CulturePeriodDB.id == id).first()
    if not db_culture_period:
        raise HTTPException(status_code=404, detail="Culture Period not found")

    db.delete(db_culture_period)
    db.commit()
    return db_culture_period
