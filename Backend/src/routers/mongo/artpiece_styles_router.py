from fastapi import APIRouter, HTTPException
from src.services.mongo.artpiece_styles_service import create_artpiece_styles, get_artpiece_styles, update_artpiece_styles, delete_artpiece_styles
from pydantic import BaseModel

router = APIRouter()

class ArtpieceStylesCreate(BaseModel):
    artpiece_id: int
    style_id: int

class ArtpieceStylesUpdate(BaseModel):
    style_id: int

@router.post("/artpiece-styles/")
def create_artpiece_styles_route(artpiece_styles: ArtpieceStylesCreate):
    artpiece_styles_id = create_artpiece_styles(artpiece_styles.dict())
    return {"id": artpiece_styles_id}

@router.get("/artpiece-styles/{artpiece_styles_id}")
def read_artpiece_styles(artpiece_styles_id: str):
    artpiece_styles = get_artpiece_styles(artpiece_styles_id)
    if artpiece_styles is None:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return artpiece_styles

@router.put("/artpiece-styles/{artpiece_styles_id}")
def update_artpiece_styles_route(artpiece_styles_id: str, artpiece_styles: ArtpieceStylesUpdate):
    updated = update_artpiece_styles(artpiece_styles_id, artpiece_styles.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return {"message": "Artpiece Styles updated"}

@router.delete("/artpiece-styles/{artpiece_styles_id}")
def delete_artpiece_styles_route(artpiece_styles_id: str):
    deleted = delete_artpiece_styles(artpiece_styles_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Artpiece Styles not found")
    return {"message": "Artpiece Styles deleted"}