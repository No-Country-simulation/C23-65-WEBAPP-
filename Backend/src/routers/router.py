from fastapi.routing import APIRouter

routersApp = APIRouter()

@routersApp.get("/")
def get():
    pass