# comment_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.pydantic_models import CommentCreate, CommentInDB
from models.mysql_models import Comment as CommentDB
from db.mysql import get_mysql_db

router = APIRouter()

# Obtener todos los comentarios
@router.get("/comments/", response_model=list[CommentInDB])
def get_comments(db: Session = Depends(get_mysql_db)):
    comments = db.query(CommentDB).all()
    return comments

# Obtener un comentario por ID
@router.get("/comments/{id}", response_model=CommentInDB)
def get_comment(id: int, db: Session = Depends(get_mysql_db)):
    comment = db.query(CommentDB).filter(CommentDB.id == id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

# Crear un nuevo comentario
@router.post("/comments/", response_model=CommentInDB)
def create_comment(comment: CommentCreate, db: Session = Depends(get_mysql_db)):
    # Verificar si el comentario ya existe para evitar duplicados (misma galería y usuario)
    db_comment = db.query(CommentDB).filter(
        CommentDB.user_id == comment.user_id,
        CommentDB.gallery_id == comment.gallery_id
    ).first()
    if db_comment:
        raise HTTPException(status_code=400, detail="Comment already exists")
    
    # Crear y almacenar el nuevo comentario
    db_comment = CommentDB(content=comment.content, user_id=comment.user_id, gallery_id=comment.gallery_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# Eliminar un comentario
@router.delete("/comments/{id}", response_model=CommentInDB)
def delete_comment(id: int, db: Session = Depends(get_mysql_db)):
    db_comment = db.query(CommentDB).filter(CommentDB.id == id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    db.delete(db_comment)
    db.commit()
    return db_comment
