from pydantic import BaseModel


class MODEL_CONFIGSALA(BaseModel):
  id_config_sala: int
  clave: str
  tipo_juego: int
  cantjugadores: int
  activo: int
  create_at: datetime.date
  updated_at: datetime.date