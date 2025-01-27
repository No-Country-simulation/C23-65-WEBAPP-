from fastapi import FastAPI
import uvicorn
from routers.archeopiece_routes import router as archeopiece_routes
from routers.artpiece_routes import router as artpiece_routes
from routers.artpiecegenres_routes import router as artpiecegenres_routes
from routers.artpiecestyles_routes import router as artpiecestyles_routes
from routers.author_routes import router as author_routes
from routers.comment_routes import router as comment_routes
from routers.cultureperiod_routes import router as cultureperiod_routes
from routers.favorite_routes import router as favorite_routes
from routers.gallery_routes import router as gallery_routes
from routers.galleryartpiece_routes import router as galleryartpiece_routes
from routers.genre_routes import router as genre_routes
from routers.like_routes import router as like_routes
from routers.medium_routes import router as medium_routes
from routers.pieceimg_routes import router as pieceimg_routes
from routers.profile_routes import router as profile_routes
from routers.profilefollowing_routes import router as profilefollowing_routes
from routers.style_routes import router as style_routes
from routers.user_routes import router as user_routes

# Importar inicialización de bases de datos
from db import mysql, mongo
from contextlib import asynccontextmanager

# Inicializar FastAPI
app = FastAPI()

# Función para inicializar bases de datos
async def init_databases():
    try:
        # Inicialización de MongoDB (asíncrona)
        await mongo.initialize_collections()
    except Exception as e:
        print(f"Error initializing MongoDB: {e}")
    try:
        # Inicialización de MySQL (sincrónica)
        mysql.initialize_connection()
    except Exception as e:
        print(f"Error initializing MySQL: {e}")

# Definir el manejador de eventos lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializar las bases de datos al iniciar la aplicación
    await init_databases()
    yield
    # Cerrar las conexiones al terminar la aplicación
    mongo.close_mongo_connection()  # Cerrar MongoDB
    mysql.close_connection()  # Cerrar MySQL

# Configuración de FastAPI para usar lifespan
app = FastAPI(lifespan=lifespan)

# Incluir las rutas
app.include_router(archeopiece_routes, prefix="/api/archeopieces", tags=["Archeopieces"])
app.include_router(artpiece_routes, prefix="/api/artpieces", tags=["Artpieces"])
app.include_router(artpiecegenres_routes, prefix="/api/artpiecegenres", tags=["Artpiecegenres"])
app.include_router(artpiecestyles_routes, prefix="/api/artpiecestyles", tags=["Artpiecestyles"])
app.include_router(author_routes, prefix="/api/authors", tags=["Authors"])
app.include_router(comment_routes, prefix="/api/comments", tags=["Comments"])
app.include_router(cultureperiod_routes, prefix="/api/cultureperiods", tags=["cultureperiods"])
app.include_router(favorite_routes, prefix="/api/favorites", tags=["Favorites"])
app.include_router(gallery_routes, prefix="/api/galleries", tags=["Galleries"])
app.include_router(galleryartpiece_routes, prefix="/api/galleryartpiece_routes", tags=["Galleriesgalleryartpieces"])
app.include_router(genre_routes, prefix="/api/genre_routes", tags=["Genres"])
app.include_router(like_routes, prefix="/api/like_routes", tags=["Likes"])
app.include_router(medium_routes, prefix="/api/medium_routes", tags=["Medium"])
app.include_router(pieceimg_routes, prefix="/api/pieceimg_routes", tags=["Pieceimg"])
app.include_router(profile_routes, prefix="/api/profiles", tags=["Profiles"])
app.include_router(profilefollowing_routes, prefix="/api/profilefollowing_routes", tags=["Profilefollowing"])
app.include_router(style_routes, prefix="/api/style_routes", tags=["Styles"])
app.include_router(user_routes, prefix="/api/users", tags=["Users"])

# Ejecutar la aplicación con Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)