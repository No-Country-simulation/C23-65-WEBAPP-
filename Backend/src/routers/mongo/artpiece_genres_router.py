from fastapi import APIRouter, HTTPException, Query
from src.services.mongo.artpiece_genres_service import (
    create_artpiece_genres,
    get_artpiece_genres,
    update_artpiece_genres,
    delete_artpiece_genres,
    get_all_artpiece_genres  # Importar la nueva función
)
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class ArtpieceGenresCreate(BaseModel):
    artpiece_id: int
    genre_id: int

class ArtpieceGenresUpdate(BaseModel):
    genre_id: int

# Ruta para crear un artpiece_genres
@router.post("/artpiece-genres/")
def create_artpiece_genres_route(artpiece_genres: ArtpieceGenresCreate):
    artpiece_genres_id = create_artpiece_genres(artpiece_genres.dict())
    return {"id": artpiece_genres_id}

# Ruta para obtener un artpiece_genres por ID
@router.get("/artpiece-genres/{artpiece_genres_id}")
def read_artpiece_genres(artpiece_genres_id: str):
    artpiece_genres = get_artpiece_genres(artpiece_genres_id)
    if artpiece_genres is None:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return artpiece_genres

# Ruta para obtener todos los artpiece_genres
@router.get("/artpiece-genres/")
def read_all_artpiece_genres(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_artpiece_genres(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

# Ruta para actualizar un artpiece_genres
@router.put("/artpiece-genres/{artpiece_genres_id}")
def update_artpiece_genres_route(artpiece_genres_id: str, artpiece_genres: ArtpieceGenresUpdate):
    updated = update_artpiece_genres(artpiece_genres_id, artpiece_genres.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return {"message": "Artpiece Genres updated"}

# Ruta para eliminar un artpiece_genres
@router.delete("/artpiece-genres/{artpiece_genres_id}")
def delete_artpiece_genres_route(artpiece_genres_id: str):
    deleted = delete_artpiece_genres(artpiece_genres_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Artpiece Genres not found")
    return {"message": "Artpiece Genres deleted"}