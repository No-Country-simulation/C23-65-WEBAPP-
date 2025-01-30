from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.profile_service import create_profile, get_profile, update_profile, delete_profile
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class ProfileCreate(BaseModel):
    bio: str
    profile_picture: str
    user_id: int

class ProfileUpdate(BaseModel):
    bio: str
    profile_picture: str

@router.post("/profiles/")
def create_profile_route(profile_data: ProfileCreate, db: Session = Depends(get_db)):
    return create_profile(db, profile_data.dict())

@router.get("/profiles/{profile_id}")
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = get_profile(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/profiles/{profile_id}")
def update_profile_route(profile_id: int, profile_data: ProfileUpdate, db: Session = Depends(get_db)):
    profile = update_profile(db, profile_id, profile_data.dict())
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.delete("/profiles/{profile_id}")
def delete_profile_route(profile_id: int, db: Session = Depends(get_db)):
    profile = delete_profile(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted"}