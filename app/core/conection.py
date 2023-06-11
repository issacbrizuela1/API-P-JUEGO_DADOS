import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class CONECTIONPYSQL:
    
    host = 'localhost'
    user = ''
    password = ''
    database = 'api_dados'
    port = '3306'
    connection: pymysql
    cursorclass = pymysql.cursors.DictCursor

    def __init__():
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          database=self.database,
                                          cursorclass=self.cursorclass)                                          

    # Connect to the database

    def query(self, query,values):
        db = self.connection.cursor()
        query = query
        values=values
        data = db.execute(query,values)
        db.commit()
        return data

class ALCHEMYCONECTION:
    # DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/api_dados"

    # engine = create_engine(DATABASE_URL)

    # SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

    # Base = declarative_base()

    """
        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)
    """
