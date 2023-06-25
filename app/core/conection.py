import pymysql

class CONECTIONPYSQL:
    
    host = 'localhost'
    user = 'root'
    password = ''
    database = 'api_dados'
    port = 3306                               
    connection=pymysql.connect(host=host,user=user,password=None,db=database,port=port)
    cursor=connection.cursor()

    def select(self,query:str,values=None):
        try:
            if(values!=None):
                self.connection.connect()
                self.cursor.execute(query,values)
                result=self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return result
            else:
                self.connection.connect()
                self.cursor.execute(query)
                result=self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return result
        except Exception as e:
            return str(e)

    def insert(self,query:str,values=None):
        try:
            if(values!=None):
                self.connection.connect()
                result=self.cursor.execute(query,values)
                self.connection.commit()
                self.connection.close()
                return result
            else:
                self.connection.connect()
                result=self.cursor.execute(query)
                self.connection.commit()
                self.connection.close()
                return result
        except Exception as e:
            return str(e)

    def update(self,query:str):
        try:
            self.connection.connect()
            result=self.cursor.execute(query)
            self.connection.commit()
            self.connection.close()
            return result
        except Exception as e:
            return str(e)

    def __del__(self):
        self.connection.close()




