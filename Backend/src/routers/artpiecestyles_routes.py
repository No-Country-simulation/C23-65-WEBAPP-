# artpiecestyles_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import ArtpieceStylesInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todos los ArtpieceStyles
@router.get("/artpiece_styles/", response_model=list[ArtpieceStylesInDB])
async def get_artpiece_styles(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    artpiece_styles = await db.artpiece_styles.find().to_list(100)
    return [ArtpieceStylesInDB.from_mongo(item) for item in artpiece_styles]

# Obtener un ArtpieceStyle por ID
@router.get("/artpiece_styles/{id}", response_model=ArtpieceStylesInDB)
async def get_artpiece_style(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    artpiece_style = await db.artpiece_styles.find_one({"_id": ObjectId(id)})
    if not artpiece_style:
        raise HTTPException(status_code=404, detail="ArtpieceStyle not found")
    return ArtpieceStylesInDB.from_mongo(artpiece_style)

# Crear un nuevo ArtpieceStyle
@router.post("/artpiece_styles/", response_model=ArtpieceStylesInDB)
async def create_artpiece_style(artpiece_style: ArtpieceStylesInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.artpiece_styles.insert_one(artpiece_style.dict(exclude_unset=True))
    artpiece_style.id = str(result.inserted_id)
    return artpiece_style

# Eliminar un ArtpieceStyle
@router.delete("/artpiece_styles/{id}", response_model=ArtpieceStylesInDB)
async def delete_artpiece_style(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.artpiece_styles.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="ArtpieceStyle not found")
    return {"id": id}