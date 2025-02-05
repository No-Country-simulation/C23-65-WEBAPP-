from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.services.mysql.user_service import (
    create_user,
    get_user,
    update_user,
    delete_user,
    get_all_user
)
from src.db.database import get_db
from src.models.mysql.user import User
from pydantic import BaseModel
from typing import Optional, Dict

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str
    password: str

@router.post("/users/")
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.dict())

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Ruta para obtener todos los users
@router.get("/users/")
def read_all_users(
    skip: int = Query(0, description="Número de registros a omitir"),
    limit: int = Query(100, description="Número máximo de registros a devolver"),
    filter_by: Optional[Dict[str, str]] = Query(None, description="Filtros para la consulta"),
    order_by: Optional[str] = Query(None, description="Campo para ordenar los resultados"),
    db: Session = Depends(get_db)
):
    return get_all_user(db, skip=skip, limit=limit, filter_by=filter_by, order_by=order_by)

@router.put("/users/{user_id}")
def update_user_route(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user.dict())
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}