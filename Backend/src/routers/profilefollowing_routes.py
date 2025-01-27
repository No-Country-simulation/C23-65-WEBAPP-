# profile_following_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import ProfileFollowingInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todos los ProfileFollowings
@router.get("/profile_followings/", response_model=list[ProfileFollowingInDB])
async def get_profile_followings(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    profile_followings = await db.profile_following.find().to_list(100)
    return [ProfileFollowingInDB.from_mongo(item) for item in profile_followings]

# Obtener un ProfileFollowing por ID
@router.get("/profile_followings/{id}", response_model=ProfileFollowingInDB)
async def get_profile_following(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    profile_following = await db.profile_following.find_one({"_id": ObjectId(id)})
    if not profile_following:
        raise HTTPException(status_code=404, detail="ProfileFollowing not found")
    return ProfileFollowingInDB.from_mongo(profile_following)

# Crear un nuevo ProfileFollowing
@router.post("/profile_followings/", response_model=ProfileFollowingInDB)
async def create_profile_following(profile_following: ProfileFollowingInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    # Verificar si el seguimiento ya existe
    existing_following = await db.profile_following.find_one({
        "follower_id": profile_following.follower_id,
        "followed_id": profile_following.followed_id
    })
    if existing_following:
        raise HTTPException(status_code=400, detail="Profile following already exists")
    
    result = await db.profile_following.insert_one(profile_following.dict(exclude_unset=True))
    profile_following.id = str(result.inserted_id)
    return profile_following

# Eliminar un ProfileFollowing
@router.delete("/profile_followings/{id}", response_model=ProfileFollowingInDB)
async def delete_profile_following(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    profile_following = await db.profile_following.find_one({"_id": ObjectId(id)})
    if not profile_following:
        raise HTTPException(status_code=404, detail="ProfileFollowing not found")
    
    await db.profile_following.delete_one({"_id": ObjectId(id)})
    return ProfileFollowingInDB.from_mongo(profile_following)
