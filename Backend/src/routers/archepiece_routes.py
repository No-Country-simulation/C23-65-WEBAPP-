from fastapi import APIRouter, Depends
from src.db.mongo import get_mongo_db
from src.models.mongo_models import Archepiece

router = APIRouter()

@router.post("/archepieces/")
async def create_archepiece(archepiece: Archepiece, db=Depends(get_mongo_db)):
    collection = db["archepieces"]
    result = await collection.insert_one(archepiece.dict())
    return {"id": str(result.inserted_id)}

@router.get("/archepieces/{archepiece_id}")
async def get_archepiece(archepiece_id: str, db=Depends(get_mongo_db)):
    collection = db["archepieces"]
    archepiece = await collection.find_one({"id": archepiece_id})
    if not archepiece:
        return {"error": "Archepiece not found"}
    return archepiece
