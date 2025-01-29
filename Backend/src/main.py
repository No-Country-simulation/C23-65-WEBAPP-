from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user
from config.db import engine, Base

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(user.router, prefix="/api", tags=["users"])