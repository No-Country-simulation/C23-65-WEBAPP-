from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.artpiece_service import create_artpiece, get_artpiece, update_artpiece, delete_artpiece
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class ArtpieceCreate(BaseModel):
    image_url: str
    year: int
    dimension: str
    author_id: int
    medium_id: int

class ArtpieceUpdate(BaseModel):
    image_url: str
    year: int
    dimension: str

@router.post("/artpieces/")
def create_artpiece_route(artpiece_data: ArtpieceCreate, db: Session = Depends(get_db)):
    return create_artpiece(db, artpiece_data.dict())

@router.get("/artpieces/{artpiece_id}")
def read_artpiece(artpiece_id: int, db: Session = Depends(get_db)):
    artpiece = get_artpiece(db, artpiece_id)
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return artpiece

@router.put("/artpieces/{artpiece_id}")
def update_artpiece_route(artpiece_id: int, artpiece_data: ArtpieceUpdate, db: Session = Depends(get_db)):
    artpiece = update_artpiece(db, artpiece_id, artpiece_data.dict())
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return artpiece

@router.delete("/artpieces/{artpiece_id}")
def delete_artpiece_route(artpiece_id: int, db: Session = Depends(get_db)):
    artpiece = delete_artpiece(db, artpiece_id)
    if artpiece is None:
        raise HTTPException(status_code=404, detail="Artpiece not found")
    return {"message": "Artpiece deleted"}