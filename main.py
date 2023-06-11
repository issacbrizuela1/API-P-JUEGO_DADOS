
from typing import Union
from app.api.endpoints import usuario
import traceback
from app.models import MODEL_USUARIO
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/USER/ADD/{data}")
def ADD(data:MODEL_USUARIO):
    #response=usuario.END_USUARIO.add(data)
    datos=json.load(data)
    return datos

if __name__ == '__main__':
    #uvicorn main:app --reload
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
