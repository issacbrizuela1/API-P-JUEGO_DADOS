
from typing import Union
from app.api.endpoints import usuario
from app.models import MODEL_USUARIO
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/",tags=['user'],description="creacion de usuarios")
def ADD(nombre_usuario,nombre,apellidos,correo,correo_alt,password):
    endpoint=usuario.END_USUARIO
    new_user=MODEL_USUARIO.MODEL_USUARIO
    new_user.nombre_usuario=nombre_usuario
    new_user.nombre=nombre
    new_user.apellidos=apellidos
    new_user.correo=correo
    new_user.correo_alt=correo_alt
    new_user.password=password
    response=endpoint.add(endpoint,data=new_user)
    return response


if __name__ == '__main__':
    #uvicorn main:app --reload
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
