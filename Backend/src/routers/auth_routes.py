# from fastapi import APIRouter, Depends
# from . import models, schemas
# from ..db import get_mysql_db

# router = APIRouter()

# @router.post("/login")
# def login(credentials: schemas.LoginCredentials, db: Session = Depends(get_mysql_db)):
#     # Lógica para iniciar sesión
#     pass

# @router.post("/register")
# def register(user: schemas.UserCreate, db: Session = Depends(get_mysql_db)):
#     # Lógica para registrar un nuevo usuario
#     pass
