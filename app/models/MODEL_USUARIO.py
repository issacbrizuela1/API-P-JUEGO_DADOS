from pydantic import BaseModel, validator
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core import validaciones


class BASE_MODEL_USUARIO:
    __tablename__ = "users"
    Column('id_usuario',Integer, primary_key=True)
    Column('clave',text)
    Column('nombre_usuarios',text)
    Column('nombre',text)
    Column('apellidos',text)
    Column('correo',text)
    Column('correo_alt',text)
    Column('password',text)
    Column('FA',text)
    Column('frase_recuperacion',text)
    Column('sesion_activa',int)
    Column('activo',int)
    Column('ultima_actividad',datetime.datetime)
    Column('create_at',datetime.datetime)
    Column('update_at',datetime.datetime)
    pass


class MODEL_USUARIO(BaseModel):
    
    id_usuario: int= None
    clave: str= None
    nombre_usuario: str= None
    nombre: str= None
    apellidos: str= None
    correo: str= None
    correo_alt: str= None
    password: str= None
    FA: str= None
    frase_recuperacion: str= None
    sesion_activa: int= None
    activo: int= None
    ultima_actividad: datetime.datetime = None
    create_at: datetime.datetime = None
    update_at: datetime.datetime = None
    
