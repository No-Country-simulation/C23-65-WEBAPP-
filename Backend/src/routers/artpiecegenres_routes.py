# artpiece_genres_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import ArtpieceGenresInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todos los ArtpieceGenres
@router.get("/artpiece_genres/", response_model=list[ArtpieceGenresInDB])
async def get_artpiece_genres(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    artpiece_genres = await db.artpiece_genres.find().to_list(100)
    return [ArtpieceGenresInDB.from_mongo(item) for item in artpiece_genres]

# Obtener un ArtpieceGenre por ID
@router.get("/artpiece_genres/{id}", response_model=ArtpieceGenresInDB)
async def get_artpiece_genre(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    artpiece_genre = await db.artpiece_genres.find_one({"_id": ObjectId(id)})
    if not artpiece_genre:
        raise HTTPException(status_code=404, detail="ArtpieceGenre not found")
    return ArtpieceGenresInDB.from_mongo(artpiece_genre)

@router.post("/artpiece_genres/", response_model=ArtpieceGenresInDB)
async def create_artpiece_genre(artpiece_genre: ArtpieceGenresInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.artpiece_genres.insert_one(artpiece_genre.dict(exclude_unset=True))
    artpiece_genre.id = str(result.inserted_id)
    return ArtpieceGenresInDB.from_mongo(artpiece_genre)

@router.delete("/artpiece_genres/{id}", response_model=ArtpieceGenresInDB)
async def delete_artpiece_genre(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.artpiece_genres.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="ArtpieceGenre not found")
    # Cuando se elimina, se debe retornar el objeto como ArtpieceGenresInDB
    return ArtpieceGenresInDB(id=id)  # O retornar un objeto con más detalles si es necesario

