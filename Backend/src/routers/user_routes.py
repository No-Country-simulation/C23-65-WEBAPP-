# user_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.mysql_models import User
from db.mysql import get_mysql_db
from pydantic import BaseModel
from passlib.context import CryptContext  # Para encriptar contraseñas

router = APIRouter()

# Configuración de bcrypt para encriptar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic modelo de entrada para User
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

from models.pydantic_models import UserResponse

# Función para encriptar contraseñas
def hash_password(password: str):
    return pwd_context.hash(password)

# Obtener todos los usuarios
@router.get("/users/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_mysql_db)):
    users = db.query(User).all()
    return users

# Obtener un usuario por ID
@router.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_mysql_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Crear un nuevo usuario
@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_mysql_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)  # Encriptar la contraseña
    new_user = User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Actualizar un usuario
@router.put("/users/{id}", response_model=UserResponse)
async def update_user(id: int, user: UserCreate, db: Session = Depends(get_mysql_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Verificar si el email ya está registrado (excepto el propio usuario)
    if user.email != db_user.email:
        db_user_with_same_email = db.query(User).filter(User.email == user.email).first()
        if db_user_with_same_email:
            raise HTTPException(status_code=400, detail="Email already registered")

    db_user.name = user.name
    db_user.email = user.email
    db_user.password = hash_password(user.password)  # Encriptar la contraseña
    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar un usuario
@router.delete("/users/{id}", response_model=UserResponse)
async def delete_user(id: int, db: Session = Depends(get_mysql_db)):
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return db_user
