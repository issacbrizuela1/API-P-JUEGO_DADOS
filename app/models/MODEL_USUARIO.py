from pydantic import BaseModel,validator
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core import validaciones


class BASE_MODEL_USUARIO():
    __tablename__ = "users"
    id_usuario = Column(Integer, primary_key=True)
    clave = Column(str)
    nombre_usuarios = Column(str)
    nombre = Column(str)
    apellidos = Column(str)
    correo = Column(str)
    correo_alt = Column(str)
    password = Column(str)
    FA = Column(str)
    frase_recuperacion = Column(str)
    sesion_activa = Column(int)
    activo = Column(int)
    ultima_actividad = Column(datetime.datetime)
    create_at = Column(datetime.datetime)
    update_at = Column(datetime.datetime)
    pass


class MODEL_USUARIO(BaseModel,validaciones):
    id_usuario: int
    clave: str
    nombre_usuario: str
    nombre: str
    apellidos: str
    correo: str
    correo_alt: str
    password: str
    FA: str
    frase_recuperacion: str
    sesion_activa: int
    activo: int
    ultima_actividad: Optional[datetime] = None
    create_at: datetime.datetime
    update_at: Optional[datetime] = None

    @validator(clave)
    _normalize_clave = validator(
        'clave', allow_reuse=true)(self.validar_str)

    @validator(nombre_usuarios)
    _normalize_nombre_usuarios = validator(
        'nombre_usuarios', allow_reuse=true)(self.validar_str)

    @validator(nombre)
    _normalize_nombre = validator(
        'nombre', allow_reuse=true)(self.validar_str)

    @validator(apellidos)
    _normalize_apellidos = validator(
        'apellidos', allow_reuse=true)(self.validar_str)

    @validator(correo)
    _normalize_correo = validator(
        'correo', allow_reuse=true)(self.validar_str)

    @validator(correo_alt)
    _normalize_correo_alt = validator(
        'correo_alt', allow_reuse=true)(self.validar_str)

    @validator(password)
    _normalize_password = validator(
        'password', allow_reuse=true)(self.validar_str)

    @validator(FA)
    _normalize_FA = validator('FA', allow_reuse=true)(self.validar_str)

    @validator(frase_recuperacion)
    _normalize_frase_recuperacion = validator(
        'frase_recuperacion', allow_reuse=true)(self.validar_str)
    pass
