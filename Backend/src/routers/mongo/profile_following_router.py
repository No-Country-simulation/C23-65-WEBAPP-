from fastapi import APIRouter, HTTPException, Query
from src.services.mongo.profile_following_service import create_profile_following, get_profile_following, update_profile_following, delete_profile_following, get_all_profile_following
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

class ProfileFollowingCreate(BaseModel):
    from_profile_id: int
    to_profile_id: int

class ProfileFollowingUpdate(BaseModel):
    to_profile_id: int

@router.post("/profile-followings/")
def create_profile_following_route(profile_following: ProfileFollowingCreate):
    profile_following_id = create_profile_following(profile_following.dict())
    return {"id": profile_following_id}

@router.get("/profile-followings/{profile_following_id}")
def read_profile_following(profile_following_id: str):
    profile_following = get_profile_following(profile_following_id)
    if profile_following is None:
        raise HTTPException(status_code=404, detail="Profile Following not found")
    return profile_following

# Ruta para obtener todos los gallery_artpieces
@router.get("/gallery-artpieces/")
def read_all_gallery_artpieces(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_profile_following(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

@router.put("/profile-followings/{profile_following_id}")
def update_profile_following_route(profile_following_id: str, profile_following: ProfileFollowingUpdate):
    updated = update_profile_following(profile_following_id, profile_following.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Profile Following not found")
    return {"message": "Profile Following updated"}

@router.delete("/profile-followings/{profile_following_id}")
def delete_profile_following_route(profile_following_id: str):
    deleted = delete_profile_following(profile_following_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Profile Following not found")
    return {"message": "Profile Following deleted"}