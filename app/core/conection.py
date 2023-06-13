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
                result=self.cursor.fetchall(query,values)
                self.connection.commit()
                self.connection.close()
                return result
            else:
                self.connection.connect()
                result=self.cursor.fetchall(query)
                self.connection.commit()
                self.connection.close()
                return result
        except Exception as e:
            return e

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
            return e

    def __del__(self):
        self.connection.close()






