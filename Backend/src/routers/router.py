# from fastapi.routing import APIRouter
# from .auth_routes import router as auth_router
# from .gallery_routes import router as gallery_router

# # Crear un router principal
# routersApp = APIRouter()

# # Registrar routers de otros módulos
# routersApp.include_router(auth_router, prefix="/auth", tags=["Auth"])
# routersApp.include_router(gallery_router, prefix="/gallery", tags=["Gallery"])