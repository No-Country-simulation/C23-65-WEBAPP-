from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import ArtpieceCreate, ArtpieceInDB
from models.mysql_models import Artpiece as ArtpieceDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los artpieces
@router.get("/artpieces/", response_model=list[ArtpieceInDB])
def get_artpieces(db: Session = Depends(get_mysql_db)):
    artpieces = db.query(ArtpieceDB).all()
    return artpieces

# Obtener un artpiece por ID
@router.get("/artpieces/{id}", response_model=ArtpieceInDB)
def get_artpiece(id: int, db: Session = Depends(get_mysql_db)):
    artpiece = db.query(ArtpieceDB).filter(ArtpieceDB.id == id).first()
    if not artpiece:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return artpiece

# Crear un nuevo artpiece
@router.post("/artpieces/", response_model=ArtpieceInDB)
def create_artpiece(artpiece: ArtpieceCreate, db: Session = Depends(get_mysql_db)):
    db_artpiece = ArtpieceDB(
        image_url=artpiece.image_url,
        year=artpiece.year,
        dimension=artpiece.dimension,
        author_id=artpiece.author_id,
        medium_id=artpiece.medium_id
    )
    db.add(db_artpiece)
    db.commit()
    db.refresh(db_artpiece)
    return ArtpieceInDB.from_orm(db_artpiece)

# Actualizar un artpiece
@router.put("/artpieces/{id}", response_model=ArtpieceInDB)
def update_artpiece(id: int, artpiece: ArtpieceCreate, db: Session = Depends(get_mysql_db)):
    db_artpiece = db.query(ArtpieceDB).filter(ArtpieceDB.id == id).first()
    if not db_artpiece:
        raise HTTPException(status_code=404, detail="Artpiece not found")

    db_artpiece.image_url = artpiece.image_url
    db_artpiece.year = artpiece.year
    db_artpiece.dimension = artpiece.dimension
    db_artpiece.author_id = artpiece.author_id
    db_artpiece.medium_id = artpiece.medium_id

    db.commit()
    db.refresh(db_artpiece)
    return ArtpieceInDB.from_orm(db_artpiece)

# Eliminar un artpiece
@router.delete("/artpieces/{id}", response_model=ArtpieceInDB)
def delete_artpiece(id: int, db: Session = Depends(get_mysql_db)):
    db_artpiece = db.query(ArtpieceDB).filter(ArtpieceDB.id == id).first()
    if not db_artpiece:
        raise HTTPException(status_code=404, detail="Artpiece not found")

    db.delete(db_artpiece)
    db.commit()
    return ArtpieceInDB.from_orm(db_artpiece)
