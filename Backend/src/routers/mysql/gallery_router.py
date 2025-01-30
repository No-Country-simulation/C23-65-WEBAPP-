from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.mysql.gallery_service import create_gallery, get_gallery, update_gallery, delete_gallery
from src.db.database import get_db
from pydantic import BaseModel

router = APIRouter()

class GalleryCreate(BaseModel):
    image_url: str
    description: str
    created_at: str
    owner_id: int

class GalleryUpdate(BaseModel):
    image_url: str
    description: str

@router.post("/galleries/")
def create_gallery_route(gallery_data: GalleryCreate, db: Session = Depends(get_db)):
    return create_gallery(db, gallery_data.dict())

@router.get("/galleries/{gallery_id}")
def read_gallery(gallery_id: int, db: Session = Depends(get_db)):
    gallery = get_gallery(db, gallery_id)
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return gallery

@router.put("/galleries/{gallery_id}")
def update_gallery_route(gallery_id: int, gallery_data: GalleryUpdate, db: Session = Depends(get_db)):
    gallery = update_gallery(db, gallery_id, gallery_data.dict())
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return gallery

@router.delete("/galleries/{gallery_id}")
def delete_gallery_route(gallery_id: int, db: Session = Depends(get_db)):
    gallery = delete_gallery(db, gallery_id)
    if gallery is None:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return {"message": "Gallery deleted"}