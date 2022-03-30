import pymysql
import os
from LoadEnv import load_env
load_env()
#Default DB Values
USER = os.getenv('DB_USER')
PASS = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DEFAULT_DB')

class MySQLConnection:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySQLConnection, cls).__new__(cls)
        return cls.instance
    
    def __init__(self,user=USER, password=PASS, host=HOST, database=DATABASE) -> None:
        super().__init__()
        self.user = user or USER
        self.password = password or PASS
        self.host = host or HOST
        self.database = database or DATABASE
        self.connection = pymysql.connect(user=user, password=password,
                              host=host,
                              database=database)
        self.cursor = self.connection.cursor()      
        

    def execute(self,query):
        self.cursor.execute(query)
        return self.cursor
    
    def close(self):
        self.cnx.close()

if __name__ == '__main__': 
    connection = MySQLConnection(USER, PASS, HOST, DATABASE)  
    print(connection)      
    query = ("SELECT * FROM Persons")
    cursor = connection.execute(query)
    for (Person) in cursor:
        print(f"{Person[2]} {Person[1]}, {Person[3]}, {Person[4]}")
                             