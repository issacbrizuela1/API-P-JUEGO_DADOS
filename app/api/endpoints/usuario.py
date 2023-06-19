from app.models.MODEL_USUARIO import MODEL_USUARIO
from app.core import conection
from starlette.responses import Response
import uuid


class END_USUARIO:
    conn=conection.CONECTIONPYSQL

    def add(self,data: MODEL_USUARIO):
        query = 'insert into usuario(clave,nombre_usuario,nombre,apellidos,correo,correo_alt,password)values(%s,%s,%s,%s,%s,%s,%s)'
        values = (uuid.uuid4(),data.nombre_usuario,data.nombre,data.apellidos,data.correo,data.correo_alt,data.password)
        response=self.conn.insert(self.conn,query,values)
        return response
    
    def getAll(self):
        response=self.conn.select(self.conn,'select * from usuario')
        return response
    
    def update(self,data: MODEL_USUARIO,**camposAeditar):
        primerapartedelaconsulta="update usuario set "
        return data.__dict__




