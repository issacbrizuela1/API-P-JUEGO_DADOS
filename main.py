
from typing import Union
from app.api.endpoints.usuario import END_USUARIO
from app.models.MODEL_USUARIO import MODEL_USUARIO
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/ADD",tags=['user'],description="creacion de usuarios")
def ADD(values:MODEL_USUARIO):
    endpoint=END_USUARIO
    response=endpoint.add(endpoint,data=values)
    return response
    
@app.get("/GETALL",tags=['user'],description="mostrar todos los usuarios")
def GETALL():
    return END_USUARIO.getAll(END_USUARIO)

@app.put("/UPDATE",tags=['user'],description="Editar usuarios")
def UPDATE(data: MODEL_USUARIO,id:str):
    return END_USUARIO.update(END_USUARIO,data,'clave',id,'usuario')

if __name__ == '__main__':
    #uvicorn main:app --reload
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
