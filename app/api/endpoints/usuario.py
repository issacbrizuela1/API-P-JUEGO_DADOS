from app.models import MODEL_USUARIO
from app.core import conection
import uuid


class END_USUARIO:

    def add(self, data: MODEL_USUARIO):
        query = 'insert into usuario(clave,nombre_usuario,nombre,apellidos,correo,correo_alt,password)values(%s,%s,%s,%s,%s,%s,%s)'
        values = (uuid.uuid4(),data.nombre_usuario,data.nombre,data.apellidos,data.correo,data.correo_alt,data.password)
        response=conection.CONECTIONPYSQL.query(query,values)
        return response
    

