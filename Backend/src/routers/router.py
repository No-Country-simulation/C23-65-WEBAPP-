from fastapi.routing import APIRouter

routersApp = APIRouter()

@routersApp.get("/")
def get_example():
    return {"message":"hola que tal"}