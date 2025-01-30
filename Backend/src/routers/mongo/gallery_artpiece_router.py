from fastapi import APIRouter, HTTPException
from src.services.mongo.gallery_artpiece_service import create_gallery_artpiece, get_gallery_artpiece, update_gallery_artpiece, delete_gallery_artpiece
from pydantic import BaseModel

router = APIRouter()

class GalleryArtpieceCreate(BaseModel):
    gallery_id: int
    artpiece_id: int
    note: str

class GalleryArtpieceUpdate(BaseModel):
    note: str

@router.post("/gallery-artpieces/")
def create_gallery_artpiece_route(gallery_artpiece: GalleryArtpieceCreate):
    gallery_artpiece_id = create_gallery_artpiece(gallery_artpiece.dict())
    return {"id": gallery_artpiece_id}

@router.get("/gallery-artpieces/{gallery_artpiece_id}")
def read_gallery_artpiece(gallery_artpiece_id: str):
    gallery_artpiece = get_gallery_artpiece(gallery_artpiece_id)
    if gallery_artpiece is None:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return gallery_artpiece

@router.put("/gallery-artpieces/{gallery_artpiece_id}")
def update_gallery_artpiece_route(gallery_artpiece_id: str, gallery_artpiece: GalleryArtpieceUpdate):
    updated = update_gallery_artpiece(gallery_artpiece_id, gallery_artpiece.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return {"message": "Gallery Artpiece updated"}

@router.delete("/gallery-artpieces/{gallery_artpiece_id}")
def delete_gallery_artpiece_route(gallery_artpiece_id: str):
    deleted = delete_gallery_artpiece(gallery_artpiece_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Gallery Artpiece not found")
    return {"message": "Gallery Artpiece deleted"}