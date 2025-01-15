from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hellworld():
 return "Hola mundo"