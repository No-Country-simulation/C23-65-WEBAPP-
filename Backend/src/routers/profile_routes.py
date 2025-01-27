# profile_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.mysql_models import Profile, User
from db.mysql import get_mysql_db
from pydantic import BaseModel

router = APIRouter()

# Pydantic modelo de entrada para Profile
class ProfileCreate(BaseModel):
    bio: str
    profile_picture: str
    user_id: int

from models.pydantic_models import ProfileResponse

# Obtener todos los perfiles
@router.get("/profiles/", response_model=list[ProfileResponse])
async def get_profiles(db: Session = Depends(get_mysql_db)):
    profiles = db.query(Profile).all()
    return profiles

# Obtener un perfil por ID
@router.get("/profiles/{id}", response_model=ProfileResponse)
async def get_profile(id: int, db: Session = Depends(get_mysql_db)):
    profile = db.query(Profile).filter(Profile.id == id).first()
    if not profile:
        raise HTTPException(status_code=404, detail=f"Profile with ID {id} not found")
    return profile

# Crear un nuevo perfil
@router.post("/profiles/", response_model=ProfileResponse)
async def create_profile(profile: ProfileCreate, db: Session = Depends(get_mysql_db)):
    db_user = db.query(User).filter(User.id == profile.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with ID {profile.user_id} not found")
    
    new_profile = Profile(bio=profile.bio, profile_picture=profile.profile_picture, user_id=profile.user_id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

# Actualizar un perfil
@router.put("/profiles/{id}", response_model=ProfileResponse)
async def update_profile(id: int, profile: ProfileCreate, db: Session = Depends(get_mysql_db)):
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail=f"Profile with ID {id} not found")
    
    db_user = db.query(User).filter(User.id == profile.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail=f"User with ID {profile.user_id} not found")

    db_profile.bio = profile.bio
    db_profile.profile_picture = profile.profile_picture
    db.commit()
    db.refresh(db_profile)
    return db_profile

# Eliminar un perfil
@router.delete("/profiles/{id}", response_model=ProfileResponse)
async def delete_profile(id: int, db: Session = Depends(get_mysql_db)):
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail=f"Profile with ID {id} not found")
    
    db.delete(db_profile)
    db.commit()
    return db_profile
