# gallery_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import GalleryCreate, GalleryInDB
from models.mysql_models import Gallery as GalleryDB, User as UserDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todas las galerías
@router.get("/galleries/", response_model=list[GalleryInDB])
def get_galleries(db: Session = Depends(get_mysql_db)):
    galleries = db.query(GalleryDB).all()
    return galleries

# Obtener una galería por ID
@router.get("/galleries/{id}", response_model=GalleryInDB)
def get_gallery(id: int, db: Session = Depends(get_mysql_db)):
    gallery = db.query(GalleryDB).filter(GalleryDB.id == id).first()
    if not gallery:
        raise HTTPException(status_code=404, detail="Gallery not found")
    return gallery

# Crear una nueva galería
@router.post("/galleries/", response_model=GalleryInDB)
def create_gallery(gallery: GalleryCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el owner_id existe en la base de datos
    db_user = db.query(UserDB).filter(UserDB.id == gallery.owner_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Owner not found")

    # Verificar si la galería ya existe para este owner_id e imagen
    db_gallery = db.query(GalleryDB).filter(
        GalleryDB.owner_id == gallery.owner_id,
        GalleryDB.image_url == gallery.image_url
    ).first()

    if db_gallery:
        raise HTTPException(status_code=400, detail="Gallery already exists for this owner with the same image")

    db_gallery = GalleryDB(
        image_url=gallery.image_url,
        description=gallery.description,
        owner_id=gallery.owner_id
    )
    db.add(db_gallery)
    db.commit()
    db.refresh(db_gallery)
    return db_gallery

# Actualizar una galería
@router.put("/galleries/{id}", response_model=GalleryInDB)
def update_gallery(id: int, gallery: GalleryCreate, db: Session = Depends(get_mysql_db)):
    db_gallery = db.query(GalleryDB).filter(GalleryDB.id == id).first()
    if not db_gallery:
        raise HTTPException(status_code=404, detail="Gallery not found")

    db_gallery.image_url = gallery.image_url
    db_gallery.description = gallery.description
    db_gallery.owner_id = gallery.owner_id

    db.commit()
    db.refresh(db_gallery)
    return db_gallery

# Eliminar una galería
@router.delete("/galleries/{id}", response_model=GalleryInDB)
def delete_gallery(id: int, db: Session = Depends(get_mysql_db)):
    db_gallery = db.query(GalleryDB).filter(GalleryDB.id == id).first()
    if not db_gallery:
        raise HTTPException(status_code=404, detail="Gallery not found")

    db.delete(db_gallery)
    db.commit()
    return db_gallery
