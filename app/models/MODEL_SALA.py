from pydantic import BaseModel


class MODEL_SALA(BaseModel):
    #is_offer: Union[bool, None] = None
    id_sala: int
    clave: str
    password: str
    configsala: int
    owner: int
    ganador: int
    activo: int
    create_at:  datetime.date
    updated_at:  Optional[datetime] = None
