import pymysql

class CONECTIONPYSQL:
    
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'api_dados'
    port = 3306                               
    connection=pymysql.connect(
            host=host,
            user=user,
            password=None,
            db=database,
            port=port,
        )
    cursor=connection.cursor()

    def execute_query(self,query,values):
        self.connection.connect()
        result=self.cursor.execute(query,values)
        self.connection.commit()
        self.connection.close()
        return result

    def __del__(self):
        self.connection.close()
