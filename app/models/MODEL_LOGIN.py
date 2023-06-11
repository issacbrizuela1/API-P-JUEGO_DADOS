from pydantic import BaseModel


class MODEL_LOGIN(BaseModel):
    usernameoremail:str
    password:str

