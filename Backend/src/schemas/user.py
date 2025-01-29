from pydantic import BaseModel


# Organizacion de los datos dentro de la base de datos, SIENDO RELACIONAL
class UserRegister(BaseModel):
    name: str
    last_name: str
    email: str
    password: str
    nationality: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    nationality: str

    class Config:
        from_attributes = True