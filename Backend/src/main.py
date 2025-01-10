from fastapi import FastAPI
import uvicorn
from routers.router import routersApp

mainApp = FastAPI()

mainApp.include_router(routersApp)

if __name__ == "__main__":
    uvicorn.run(mainApp, host="0.0.0.0", port=8000) #// command: uvicorn Backend.src.main:mainApp --reload