from pydantic import BaseModel


class MODEL_MOVIMIENTOS(BaseModel):
    id_movimiento:int
    clave: str
    usuario: int
    registro: str
    sala: int
    activo: int
    create_at: datetime.date
    updated_at: Optional[datetime] = None