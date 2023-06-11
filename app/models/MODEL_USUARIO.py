from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class BASE_MODEL_USUARIO():
    __tablename__ = "users"
    pass


class MODEL_USUARIO(BaseModel):
    id_usuario: int
    nombre_usuario: str
    nombre: str
    apellidos: str
    correo: str
    correo_alt: str
    password: str
    '2FA': str
    frase_recuperacion: str
    sesion_activa: int
    activo: int
    ultima_actividad: Optional[datetime] = None
    create_at: datetime.date
    update_at: Optional[datetime] = None
    pass