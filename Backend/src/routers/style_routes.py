# style_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import StyleCreate, StyleInDB
from models.mysql_models import Style as StyleDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los estilos
@router.get("/styles/", response_model=list[StyleInDB])
def get_styles(db: Session = Depends(get_mysql_db)):
    styles = db.query(StyleDB).all()
    return styles

# Obtener un estilo por ID
@router.get("/styles/{id}", response_model=StyleInDB)
def get_style(id: int, db: Session = Depends(get_mysql_db)):
    style = db.query(StyleDB).filter(StyleDB.id == id).first()
    if not style:
        raise HTTPException(status_code=404, detail="Style not found")
    return style

# Crear un nuevo estilo
@router.post("/styles/", response_model=StyleInDB)
def create_style(style: StyleCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el estilo ya existe
    existing_style = db.query(StyleDB).filter(StyleDB.name == style.name).first()
    if existing_style:
        raise HTTPException(status_code=400, detail="Style already exists")

    db_style = StyleDB(name=style.name)
    db.add(db_style)
    db.commit()
    db.refresh(db_style)
    return db_style

# Actualizar un estilo
@router.put("/styles/{id}", response_model=StyleInDB)
def update_style(id: int, style: StyleCreate, db: Session = Depends(get_mysql_db)):
    db_style = db.query(StyleDB).filter(StyleDB.id == id).first()
    if not db_style:
        raise HTTPException(status_code=404, detail="Style not found")

    if db_style.name != style.name:
        db_style.name = style.name

    db.commit()
    db.refresh(db_style)
    return db_style

# Eliminar un estilo
@router.delete("/styles/{id}", response_model=StyleInDB)
def delete_style(id: int, db: Session = Depends(get_mysql_db)):
    db_style = db.query(StyleDB).filter(StyleDB.id == id).first()
    if not db_style:
        raise HTTPException(status_code=404, detail="Style not found")

    db.delete(db_style)
    db.commit()
    return db_style
