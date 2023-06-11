from pydantic import BaseModel


class MODEL_PARTICIPANTES(BaseModel):
    id_participantes: int
    clave: str
    sala: int
    usuario: int
    activo: int
    create_at: datetime.date
    updated_at: Optional[datetime] = None