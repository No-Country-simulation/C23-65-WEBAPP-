from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.medium_service import create_medium, get_medium, update_medium, delete_medium
from src.db.database import get_db
from pydantic import BaseModel

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