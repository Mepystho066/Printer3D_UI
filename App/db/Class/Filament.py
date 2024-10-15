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

class Filament: 
    def __init__(self,name,color,company,cuantity):
        self.name=name
        self.color=color
        self.company=company
        self.cuantity=cuantity
        #self.filamentCost_id=filamentCost_id
    def __str__(self):
        return f"name={self.name},color={self.color},company={self.company},cuantity={self.cuantity}"
    
    def save(self):
        cursor.execute('''
        INSERT INTO Filaments(name,color,company,cuantity) 
        VALUES (?,?,?,?)''',(self.name, self.color, self.company, self.cuantity))
        self.id = cursor.lastrowid
        connection.commit()
    @classmethod
    def create(clss,name,color,company,cuantity):
        filamentCreate = clss(name,color,company,cuantity)
        filamentCreate.save()
        return filamentCreate
    @classmethod
    def create_from_db(clss,table_file):
        
        new_instance = clss(table_file[1],table_file[2],table_file[3],table_file[4])
        new_instance.id = table_file[0]
        return new_instance
    @classmethod 
    def get_table_rows(clss):
        table = cursor.execute('''SELECT * FROM Filaments''').fetchall()
        return [clss.create_from_db(row) for row in table]
    @classmethod
    def create_table(clss):
        cursor.execute('''CREATE TABLE IF NOT EXISTS Filaments(
        id INTEGER PRIMARY KEY ,
        name TEXT,
        color TEXT,
        company TEXT,
        cuantity INTEGER
        )''')
        connection.commit()
    
    @classmethod
    def drop_table(clss):
        cursor.execute('''DROP TABLE IF EXISTS Filaments''')
        connection.commit()

class FilamentCost:
    def __init__(self,cost,dateBuy):
        #self.ID=ID
        self.cost=cost
        self.dateBuy=dateBuy
        
    def __str__(self):
        return f"cost={self.cost},dateBuy={self.dateBuy}"
    

if __name__== "__main__":
    db_filament = Filament
    #db_filament.drop_table()
    #db_filament.create_table()
    #db_filament.create('TEST','TEST','TEST',123)
    for i in db_filament.get_table_rows():
        print(i)