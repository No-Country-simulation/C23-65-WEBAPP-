from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

# Para incriptar la contraseña, que me permite crifrarla
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get('/users')
def get_users():
 return conn.execute(users.select()).fetchall()


@user.post('/users')
def create_user(user: User):
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": f.encrypt(user.password.encode("utf-8"))
    }
    try:
        # Inserta el nuevo usuario
        result = conn.execute(users.insert().values(new_user))
        
        # Realiza el commit para confirmar los cambios
        conn.commit()
        
        return {"message": "Usuario creado exitosamente", "user_id": result.lastrowid}
    except Exception as e:
        print(f"Error al crear el usuario: {e}")  # Agrega un print para depurar
        return {"error": str(e)}



# @user.post('/users')
# def create_user(user: User):
#  new_user = {"name": user.name, "email": user.email}
#  encrypted_password = f.encrypt(user.password.encode("utf-8"))
#  print(len(encrypted_password))
#  result = conn.execute(users.insert().values(new_user))
#  print(result)
#  conn.commit()
#  return {"message": "Usuario Creado exitosamente", "user_id": result.lastrowid}

