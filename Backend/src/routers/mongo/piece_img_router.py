from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from src.services.mongo.piece_img_service import create_piece_img, get_piece_img, update_piece_img, delete_piece_img, get_all_piece_imgs
from pydantic import BaseModel
from typing import Optional, Dict
import cloudinary
import cloudinary.uploader

router = APIRouter()

# Modelos Pydantic
class PieceImgCreate(BaseModel):
    name: str
    archeopiece_id: Optional[int] = None  # Hacerlo opcional
    artpiece_id: Optional[int] = None  # Hacerlo opcional

class PieceImgUpdate(BaseModel):
    name: Optional[str] = None  # Hacerlo opcional
    archeopiece_id: Optional[int] = None  # Hacerlo opcional
    artpiece_id: Optional[int] = None  # Hacerlo opcional

# Ruta para crear un piece_img
@router.post("/piece-imgs/")
async def create_piece_img_route(
    name: str = Query(...),  # Nombre de la imagen
    archeopiece_id: Optional[int] = Query(None),  # Opcional
    artpiece_id: Optional[int] = Query(None),  # Opcional
    image: UploadFile = File(...)  # El cliente debe enviar la imagen como archivo
):
    # Leer el archivo de imagen
    image_file = await image.read()

    # Crear el diccionario con los datos del registro
    piece_img_data = {
        "name": name,
        "archeopiece_id": archeopiece_id,
        "artpiece_id": artpiece_id
    }

    # Llamar al servicio para crear el registro y subir la imagen
    piece_img_id = create_piece_img(piece_img_data, image_file)

    return {"id": piece_img_id}

# Ruta para obtener un piece_img por ID
@router.get("/piece-imgs/{piece_img_id}")
def read_piece_img(piece_img_id: str):
    piece_img = get_piece_img(piece_img_id)
    if piece_img is None:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return piece_img

# Ruta para obtener todos los piece_imgs
@router.get("/piece-imgs/")
def read_all_piece_imgs(
    skip: int = Query(0, description="Número de documentos a omitir"),
    limit: int = Query(100, description="Número máximo de documentos a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    sort_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
):
    return get_all_piece_imgs(skip=skip, limit=limit, filter_by=filter_by, sort_by=sort_by)

# Ruta para actualizar un piece_img
@router.put("/piece-imgs/{piece_img_id}")
async def update_piece_img_route(
    piece_img_id: str,
    name: Optional[str] = Query(None),  # Opcional
    archeopiece_id: Optional[int] = Query(None),  # Opcional
    artpiece_id: Optional[int] = Query(None),  # Opcional
    image: Optional[UploadFile] = File(None)  # Opcional: nueva imagen
):
    # Crear el diccionario con los datos a actualizar
    update_data = {}
    if name is not None:
        update_data["name"] = name
    if archeopiece_id is not None:
        update_data["archeopiece_id"] = archeopiece_id
    if artpiece_id is not None:
        update_data["artpiece_id"] = artpiece_id

    # Si se proporciona una nueva imagen, subirla a Cloudinary
    if image is not None:
        image_file = await image.read()
        upload_result = cloudinary.uploader.upload(image_file, public_id=name)
        update_data["file_url"] = upload_result["secure_url"]

    # Llamar al servicio para actualizar el registro
    updated = update_piece_img(piece_img_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return {"message": "Piece Image updated"}

# Ruta para eliminar un piece_img
@router.delete("/piece-imgs/{piece_img_id}")
def delete_piece_img_route(piece_img_id: str):
    deleted = delete_piece_img(piece_img_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return {"message": "Piece Image deleted"}