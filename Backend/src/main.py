from fastapi import FastAPI
import uvicorn
from src.routers.upload_routes import router as upload_router
from src.routers.archepiece_routes import router as archepiece_router

# Inicializar FastAPI
app = FastAPI()

# Incluir las rutas
app.include_router(upload_router, prefix="/api/uploads", tags=["Uploads"])
app.include_router(archepiece_router, prefix="/api/archepieces", tags=["Archepieces"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
