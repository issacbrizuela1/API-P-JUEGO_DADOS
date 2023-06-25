from pydantic import BaseModel, validator, root_validator
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.validaciones import validaciones

class MODEL_USUARIO(BaseModel):

    id_usuario: int = None
    clave: str = None
    nombre_usuario: str = None
    nombre: str = None
    apellidos: str = None
    correo: str = None
    correo_alt: str = None
    password: str = None
    FsA: str = None
    frase_recuperacion: str = None
    sesion_activa: int = None
    activo: int = None
    ultima_actividad: datetime.datetime = None
    create_at: datetime.datetime = None
    update_at: datetime.datetime = None

    # region VALIDAMOS LOS STRINGS

    @root_validator
    def validar(cls, values):
        return validaciones.validar_str(validaciones, values, (
            'nombre_usuario',
            'nombre',
            'apellidos',
            'correo',
            'correo_alt',
            'password',
            'FsA',
            'frase_recuperacion',
        ))

    # endregion
