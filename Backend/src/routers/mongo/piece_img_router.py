from fastapi import APIRouter, HTTPException
from src.services.mongo.piece_img_service import create_piece_img, get_piece_img, update_piece_img, delete_piece_img
from pydantic import BaseModel

router = APIRouter()

class PieceImgCreate(BaseModel):
    file: bytes
    name: str
    archeopiece_id: int
    artpiece_id: int

class PieceImgUpdate(BaseModel):
    name: str

@router.post("/piece-imgs/")
def create_piece_img_route(piece_img: PieceImgCreate):
    piece_img_id = create_piece_img(piece_img.dict())
    return {"id": piece_img_id}

@router.get("/piece-imgs/{piece_img_id}")
def read_piece_img(piece_img_id: str):
    piece_img = get_piece_img(piece_img_id)
    if piece_img is None:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return piece_img

@router.put("/piece-imgs/{piece_img_id}")
def update_piece_img_route(piece_img_id: str, piece_img: PieceImgUpdate):
    updated = update_piece_img(piece_img_id, piece_img.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return {"message": "Piece Image updated"}

@router.delete("/piece-imgs/{piece_img_id}")
def delete_piece_img_route(piece_img_id: str):
    deleted = delete_piece_img(piece_img_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Piece Image not found")
    return {"message": "Piece Image deleted"}