# gallery_artpiece_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import GalleryArtpieceInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todos los GalleryArtpieces
@router.get("/gallery_artpieces/", response_model=list[GalleryArtpieceInDB])
async def get_gallery_artpieces(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    gallery_artpieces = await db.gallery_artpiece.find().to_list(100)
    return [GalleryArtpieceInDB.from_mongo(item) for item in gallery_artpieces]

# Obtener un GalleryArtpiece por ID
@router.get("/gallery_artpieces/{id}", response_model=GalleryArtpieceInDB)
async def get_gallery_artpiece(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    # Validar el ID antes de usarlo
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    gallery_artpiece = await db.gallery_artpiece.find_one({"_id": ObjectId(id)})
    if not gallery_artpiece:
        raise HTTPException(status_code=404, detail="GalleryArtpiece not found")
    return GalleryArtpieceInDB.from_mongo(gallery_artpiece)

# Crear un nuevo GalleryArtpiece
@router.post("/gallery_artpieces/", response_model=GalleryArtpieceInDB)
async def create_gallery_artpiece(gallery_artpiece: GalleryArtpieceInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    # Verificar si ya existe el GalleryArtpiece con los mismos datos
    existing_artpiece = await db.gallery_artpiece.find_one({"gallery_id": gallery_artpiece.gallery_id, "artpiece_id": gallery_artpiece.artpiece_id})
    if existing_artpiece:
        raise HTTPException(status_code=400, detail="GalleryArtpiece already exists")

    # Insertar el nuevo GalleryArtpiece
    result = await db.gallery_artpiece.insert_one(gallery_artpiece.dict(exclude_unset=True))
    gallery_artpiece.id = str(result.inserted_id)
    return gallery_artpiece

# Eliminar un GalleryArtpiece
@router.delete("/gallery_artpieces/{id}", response_model=GalleryArtpieceInDB)
async def delete_gallery_artpiece(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    # Validar el ID antes de usarlo
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await db.gallery_artpiece.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="GalleryArtpiece not found")
    return {"id": id}
