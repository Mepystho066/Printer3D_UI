import sqlite3 as sql
import os
#from controlTables import pathDB
   

def tabla(path="../data/dataBaseTest.db"):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        connection = sql.connect(path) 
        cursor = connection.cursor()
    else: 
        connection = sql.connect(path) 
        cursor = connection.cursor()
    return cursor , connection
   
   

cursor , connection = tabla()
class Users:
    def __init__(self,name:str=None,lastname:str=None,email:str=None): #,addresFK:str=None,facturaFK:str=None):
        #self._id=_id
        self.name=name
        self.lastname=lastname
        self.email=email
        #self.addresFK=addresFK
        #self.facturaFK= facturaFK
    
    def __str__(self):
        return f"name={self.name},lastname={self.lastname},email={self.email}"
    
    def seve(self):
        string='''INSERT INTO Users (name,lastname,email) VALUES (?,?,?)'''
        cursor.execute(string,(self.name,self.lastname,self.email))
        self.id = cursor.lastrowid
        connection.commit()

    @classmethod
    def create(clss,name,lastName,email):
        userCreate = clss(name,lastName,email)
        userCreate.seve()
        return userCreate

    @classmethod
    def create_from_db(clss, table_file):
        new_instance = clss(table_file[1],table_file[2],table_file[3])
        new_instance.id = table_file[0]
        return new_instance
    
    @classmethod
    def get_table_rows(clss):
        table = cursor.execute('''SELECT * FROM Users''').fetchall()
        #connect.commit()
        return  [ clss.create_from_db(row) for row in table]

    @classmethod
    def create_table(clss):
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                lastname TEXT,
                email TEXT
            )''')
                #facturaFK Integer,
                #FOREIGN key (facturaFK) References factura(Id)
        connection.commit()
        print("La Tabla Usuaro fue creada")
    
    @classmethod
    def drop_table(clss):
        cursor.execute('''DROP TABLE IF EXISTEN Users''')
        connect.commit()
if __name__ == "__main__":
    #Users.drop_table
    #Users().create_table()
    lista = Users.get_table_rows()
    for i in lista:
        print(i)
    
