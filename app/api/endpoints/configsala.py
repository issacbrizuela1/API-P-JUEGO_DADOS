from app.models.MODEL_TIPOJUEGO import MODEL_TIPOJUEGO
from app.core import conection
from starlette.responses import Response
import uuid


class END_TIPO_JUEGO:
    conn = conection.CONECTIONPYSQL

    def add(self, data: MODEL_TIPOJUEGO):
        query = f"INSERT INTO tipo_juego(clave, nombre, descripcion, JSONCONFIG, activo)\
                    VALUES({uuid.uuid4},{data.nombre}, {data.descripcion},{data.JSONCONFIG}, 1)"
        response = self.conn.insert(self.conn, query)
        return response

    def getAll(self):
        response = self.conn.select(self.conn, 'select * from tipo_juego')
        return response

    def update(self, diccionario: MODEL_USUARIO, campo_id, valor_id, tabla):
        campos_valores = []
        DATOS = diccionario
        for campo, valor in DATOS:
            if valor == None:
                ''
            else:
                campos_valores.extend([f"{campo}={valor}"])
        set_parte = ", ".join(campos_valores)
        consulta = f"UPDATE {tabla} SET {set_parte} WHERE {campo_id}='{valor_id}'"
        print(consulta)
        RESPONSE = self.conn.update(self.conn, consulta)
        return RESPONSE
