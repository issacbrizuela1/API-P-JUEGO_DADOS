from pydantic import BaseModel


class MODEL_TIPOJUEGO(BaseModel):
    id_tipo_juego: int
    clave: str
    nombre: str
    descripcion: str
    JSONCONFIG: str
    activo: int
    create_at: datetime.date
    updated_at: Optional[datetime] = None
