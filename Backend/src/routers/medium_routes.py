# medium_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import MediumCreate, MediumInDB
from models.mysql_models import Medium as MediumDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los medios
@router.get("/mediums/", response_model=list[MediumInDB])
def get_mediums(db: Session = Depends(get_mysql_db)):
    mediums = db.query(MediumDB).all()
    return mediums

# Obtener un medio por ID
@router.get("/mediums/{id}", response_model=MediumInDB)
def get_medium(id: int, db: Session = Depends(get_mysql_db)):
    medium = db.query(MediumDB).filter(MediumDB.id == id).first()
    if not medium:
        raise HTTPException(status_code=404, detail="Medium with ID {id} not found")
    return medium

# Crear un nuevo medio
@router.post("/mediums/", response_model=MediumInDB)
def create_medium(medium: MediumCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el medio ya existe
    db_medium = db.query(MediumDB).filter(MediumDB.name == medium.name).first()
    if db_medium:
        raise HTTPException(status_code=400, detail="Medium with this name already exists")

    db_medium = MediumDB(name=medium.name)
    db.add(db_medium)
    db.commit()
    db.refresh(db_medium)
    return db_medium

# Actualizar un medio
@router.put("/mediums/{id}", response_model=MediumInDB)
def update_medium(id: int, medium: MediumCreate, db: Session = Depends(get_mysql_db)):
    db_medium = db.query(MediumDB).filter(MediumDB.id == id).first()
    if not db_medium:
        raise HTTPException(status_code=404, detail="Medium with ID {id} not found")

    db_medium.name = medium.name

    db.commit()
    db.refresh(db_medium)
    return db_medium

# Eliminar un medio
@router.delete("/mediums/{id}", response_model=MediumInDB)
def delete_medium(id: int, db: Session = Depends(get_mysql_db)):
    db_medium = db.query(MediumDB).filter(MediumDB.id == id).first()
    if not db_medium:
        raise HTTPException(status_code=404, detail="Medium with ID {id} not found")

    db.delete(db_medium)
    db.commit()
    return db_medium
