from pydantic import BaseModel, validator
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core import validaciones


class BASE_MODEL_USUARIO:
    # __tablename__ = "users"
    # Column('id_usuario',Integer, primary_key=True)
    # Column('clave',String(255),unique=true)
    # Column('nombre_usuarios',String(255),unique=true)
    # Column('nombre',String(255),unique=true)
    # Column('apellidos',String(255),unique=true)
    # Column('correo',String(255),unique=true)
    # Column('correo_alt',String(255),unique=true)
    # Column('password',String(255),unique=true)
    # Column('FA',String(255),unique=true)
    # Column('frase_recuperacion',String(255),unique=true)
    # Column('sesion_activa',int(1))
    # Column('activo',int(1))
    # Column('ultima_actividad',datetime.datetime)
    # Column('create_at',datetime.datetime)
    # Column('update_at',datetime.datetime)
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
    
