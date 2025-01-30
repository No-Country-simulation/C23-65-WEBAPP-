from fastapi import FastAPI
from src.db.database import init_db
from src.routers.mysql.user_router import router as user_router
from src.routers.mysql.profile_router import router as profile_router
from src.routers.mysql.gallery_router import router as gallery_router
from src.routers.mysql.artpiece_router import router as artpiece_router
from src.routers.mysql.author_router import router as author_router
from src.routers.mysql.genre_router import router as genre_router
from src.routers.mysql.style_router import router as style_router
from src.routers.mysql.medium_router import router as medium_router
from src.routers.mysql.culture_period_router import router as culture_period_router
from src.routers.mysql.favorite_router import router as favorite_router
from src.routers.mysql.like_router import router as like_router
from src.routers.mysql.comment_router import router as comment_router
from src.routers.mongo.gallery_artpiece_router import router as gallery_artpiece_router
from src.routers.mongo.artpiece_styles_router import router as artpiece_styles_router
from src.routers.mongo.artpiece_genres_router import router as artpiece_genres_router
from src.routers.mongo.piece_img_router import router as piece_img_router
from src.routers.mongo.profile_following_router import router as profile_following_router
from src.routers.mongo.archeopiece_router import router as archeopiece_router

# Inicializar la aplicación FastAPI
app = FastAPI()

# Inicializar la base de datos al iniciar la aplicación
@app.on_event("startup")
def startup_event():
    init_db()

# Incluir routers de MySQL
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(profile_router, prefix="/profiles", tags=["profiles"])
app.include_router(gallery_router, prefix="/galleries", tags=["galleries"])
app.include_router(artpiece_router, prefix="/artpieces", tags=["artpieces"])
app.include_router(author_router, prefix="/authors", tags=["authors"])
app.include_router(genre_router, prefix="/genres", tags=["genres"])
app.include_router(style_router, prefix="/styles", tags=["styles"])
app.include_router(medium_router, prefix="/mediums", tags=["mediums"])
app.include_router(culture_period_router, prefix="/culture-periods", tags=["culture-periods"])
app.include_router(favorite_router, prefix="/favorites", tags=["favorites"])
app.include_router(like_router, prefix="/likes", tags=["likes"])
app.include_router(comment_router, prefix="/comments", tags=["comments"])

# Incluir routers de MongoDB
app.include_router(gallery_artpiece_router, prefix="/gallery-artpieces", tags=["gallery-artpieces"])
app.include_router(artpiece_styles_router, prefix="/artpiece-styles", tags=["artpiece-styles"])
app.include_router(artpiece_genres_router, prefix="/artpiece-genres", tags=["artpiece-genres"])
app.include_router(piece_img_router, prefix="/piece-imgs", tags=["piece-imgs"])
app.include_router(profile_following_router, prefix="/profile-followings", tags=["profile-followings"])
app.include_router(archeopiece_router, prefix="/archeopieces", tags=["archeopieces"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Art Gallery API!"}