from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.comment_service import (
    create_comment,
    get_comment,
    update_comment,
    delete_comment,
    get_all_comments  # Importar la nueva función
)
from src.db.database import get_db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

router = APIRouter()

# Modelos Pydantic
class CommentCreate(BaseModel):
    content: str
    created_at: datetime
    user_id: int
    gallery_id: int

class CommentUpdate(BaseModel):
    content: str

# Ruta para crear un comentario
@router.post("/comments/")
def create_comment_route(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db, comment.dict())

# Ruta para obtener un comentario por ID
@router.get("/comments/{comment_id}")
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

# Ruta para obtener todos los comentarios
@router.get("/comments/")
def read_all_comments(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_comments(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

# Ruta para actualizar un comentario
@router.put("/comments/{comment_id}")
def update_comment_route(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)):
    db_comment = update_comment(db, comment_id, comment.dict())
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

# Ruta para eliminar un comentario
@router.delete("/comments/{comment_id}")
def delete_comment_route(comment_id: int, db: Session = Depends(get_db)):
    db_comment = delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"}