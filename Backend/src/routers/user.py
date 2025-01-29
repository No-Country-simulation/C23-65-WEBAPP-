from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from config.db import get_db
from models.user import User
from schemas.user import UserRegister, UserLogin, UserResponse

router = APIRouter()

# Configuración de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Proceso de la Registrar usuario
@router.post("/register", response_model=UserResponse)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    hashed_password = hash_password(user.password)
    db_user = User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
        nationality=user.nationality
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al registrar usuario")

# Proceso de Login de usuario
@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {
        "id": db_user.id,
        "email": db_user.email,
        "name": db_user.name,
        "message": "Inicio de sesión exitoso"
    }

