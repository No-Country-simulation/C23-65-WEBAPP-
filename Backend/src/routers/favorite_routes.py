# favorite_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import FavoriteCreate, FavoriteInDB
from models.mysql_models import Favorite as FavoriteDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los favoritos
@router.get("/favorites/", response_model=list[FavoriteInDB])
def get_favorites(db: Session = Depends(get_mysql_db)):
    favorites = db.query(FavoriteDB).all()
    return favorites

# Obtener un favorito por ID
@router.get("/favorites/{id}", response_model=FavoriteInDB)
def get_favorite(id: int, db: Session = Depends(get_mysql_db)):
    favorite = db.query(FavoriteDB).filter(FavoriteDB.id == id).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite

# Crear un nuevo favorito
@router.post("/favorites/", response_model=FavoriteInDB)
def create_favorite(favorite: FavoriteCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el favorito ya existe (para evitar duplicados)
    db_favorite = db.query(FavoriteDB).filter(
        FavoriteDB.archepiece_id == favorite.archepiece_id,
        FavoriteDB.artpiece_id == favorite.artpiece_id,
        FavoriteDB.gallery_id == favorite.gallery_id,
        FavoriteDB.user_id == favorite.user_id
    ).first()

    if db_favorite:
        raise HTTPException(status_code=400, detail="Favorite already exists")

    db_favorite = FavoriteDB(
        archepiece_id=favorite.archepiece_id,
        artpiece_id=favorite.artpiece_id,
        gallery_id=favorite.gallery_id,
        user_id=favorite.user_id
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

# Eliminar un favorito
@router.delete("/favorites/{id}", response_model=FavoriteInDB)
def delete_favorite(id: int, db: Session = Depends(get_mysql_db)):
    db_favorite = db.query(FavoriteDB).filter(FavoriteDB.id == id).first()
    if not db_favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(db_favorite)
    db.commit()
    return db_favorite
