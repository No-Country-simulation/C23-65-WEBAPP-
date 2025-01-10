from fastapi.routing import APIRouter

routersApp = APIRouter()

@routersApp.get("/")
def get_example():
    return {"message":"hola que tal"}

@routersApp.get("/")
def get_example2():
    return {"message":"hola que tal"}