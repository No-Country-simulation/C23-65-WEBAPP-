# archeopiece_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import ArcheopieceInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todos los Archeopieces
@router.get("/", response_model=list[ArcheopieceInDB])
async def get_archeopieces(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    archeopieces = await db.archeopiece.find().to_list(100)
    return [ArcheopieceInDB.from_mongo(item) for item in archeopieces]

# Obtener un Archeopiece por ID
@router.get("/{id}", response_model=ArcheopieceInDB)
async def get_archeopiece(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    archeopiece = await db.archeopiece.find_one({"_id": ObjectId(id)})
    if not archeopiece:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    return ArcheopieceInDB.from_mongo(archeopiece)

# Crear un nuevo Archeopiece
@router.post("/", response_model=ArcheopieceInDB)
async def create_archeopiece(archeopiece: ArcheopieceInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.archeopiece.insert_one(archeopiece.dict(exclude_unset=True))
    archeopiece.id = str(result.inserted_id)
    return archeopiece

# Eliminar un Archeopiece
@router.delete("/{id}", response_model=ArcheopieceInDB)
async def delete_archeopiece(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    archeopiece = await db.archeopiece.find_one({"_id": ObjectId(id)})
    if not archeopiece:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    
    # Eliminar el archeopiece
    result = await db.archeopiece.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Archeopiece not found")
    
    return ArcheopieceInDB.from_mongo(archeopiece)
