from fastapi import APIRouter, HTTPException
from src.services.mongo.artpiece_genres_service import create_artpiece_genres, get_artpiece_genres, update_artpiece_genres, delete_artpiece_genres
from pydantic import BaseModel

router = APIRouter()

class ArtpieceGenresCreate(BaseModel):
    artpiece_id: int
    genre_id: int

class ArtpieceGenresUpdate(BaseModel):
    genre_id: int

@router.post("/artpiece-genres/")
def create_artpiece_genres_route(artpiece_genres: ArtpieceGenresCreate):
    artpiece_genres_id = create_artpiece_genres(artpiece_genres.dict())
    return {"id": artpiece_genres_id}

@router.get("/artpiece-genres/{artpiece_genres_id}")
def read_artpiece_genres(artpiece_genres_id: str):
    artpiece_genres = get_artpiece_genres(artpiece_genres_id)
    if artpiece_genres is None:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return artpiece_genres

@router.put("/artpiece-genres/{artpiece_genres_id}")
def update_artpiece_genres_route(artpiece_genres_id: str, artpiece_genres: ArtpieceGenresUpdate):
    updated = update_artpiece_genres(artpiece_genres_id, artpiece_genres.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return {"message": "Artpiece Genres updated"}

@router.delete("/artpiece-genres/{artpiece_genres_id}")
def delete_artpiece_genres_route(artpiece_genres_id: str):
    deleted = delete_artpiece_genres(artpiece_genres_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return {"message": "Artpiece Genres deleted"}