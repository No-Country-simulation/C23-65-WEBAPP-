# piece_img_routes.py

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_models import PieceImgInDB
from db.mongo import get_mongo_db
from bson import ObjectId

router = APIRouter()

# Obtener todas las PieceImgs
@router.get("/piece_imgs/", response_model=list[PieceImgInDB])
async def get_piece_imgs(db: AsyncIOMotorClient = Depends(get_mongo_db)):
    piece_imgs = await db.piece_img.find().to_list(100)
    return [PieceImgInDB.from_mongo(item) for item in piece_imgs]

# Obtener una PieceImg por ID
@router.get("/piece_imgs/{id}", response_model=PieceImgInDB)
async def get_piece_img(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    piece_img = await db.piece_img.find_one({"_id": ObjectId(id)})
    if not piece_img:
        raise HTTPException(status_code=404, detail=f"PieceImg with ID {id} not found")
    return PieceImgInDB.from_mongo(piece_img)

# Crear una nueva PieceImg
@router.post("/piece_imgs/", response_model=PieceImgInDB)
async def create_piece_img(piece_img: PieceImgInDB, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    # Verificar si ya existe una imagen con la misma URL (o cualquier otro atributo único)
    existing_piece_img = await db.piece_img.find_one({"url": piece_img.url})
    if existing_piece_img:
        raise HTTPException(status_code=400, detail="PieceImg with this URL already exists")

    result = await db.piece_img.insert_one(piece_img.dict(exclude_unset=True))
    piece_img.id = str(result.inserted_id)
    return piece_img

# Eliminar una PieceImg
@router.delete("/piece_imgs/{id}", response_model=PieceImgInDB)
async def delete_piece_img(id: str, db: AsyncIOMotorClient = Depends(get_mongo_db)):
    result = await db.piece_img.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"PieceImg with ID {id} not found")
    return {"id": id}
