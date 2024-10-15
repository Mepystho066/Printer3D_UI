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
   
cursor,connection = tabla()
class Print:

    def __init__(self,name:str=None,img:str=None,printTime:int=None):#filamentFK,printCostFK):
        #self._id=_id
        self.name=name
        self.img=img
        self.printTime =printTime
        #self.filamentFK =filamentFK
        #self.printCostFK =printCostFK
        
    def __str__(self):
        return f"name={self.name},img={self.img},printTime={self.printTime}"#,filamentFK={self.filamentFK},printCostFK={self.printCostFK}"

    
    def save(self):
        string='''INSERT INTO Prints(name,img,printTime) VALUES (?,?,?)'''
        cursor.execute(string,(self.name,self.img,self.printTime))
        self.id = cursor.lastrowid
        connection.commit()
        
    @classmethod
    def create(clss,name, img, printTime):
        printCreate = clss(name, img, printTime)
        printCreate.save()
        return printCreate

    @classmethod
    def create_from_db(clss,table_file): 
        new_instance= clss(table_file[1],table_file[2],table_file[3])
        new_instance.id = table_file[0]
        return new_instance
    @classmethod
    def get_table_rows(clss):
        table = cursor.execute(f'SELECT * FROM Prints').fetchall()
        #connect.commit()
        return [ clss.create_from_db(row) for row in table]

    @classmethod
    def create_table(clss): 
        cursor.execute('''CREATE TABLE IF NOT EXISTS Prints(
        id INTEGER PRIMARY KEY,
        name TEXT,
        img TEXT,
        printTime INTEGER
        )''')
        connection.commit()
   
    @classmethod
    def drop_table(clss):
        cursor.execute('''DROP TABLE IF EXISTS Prints''')
        connection.commit()

class PrintCost:
    def __init__(self,ID,total,iva):
        self.ID=ID
        self.total=total
        self.iva=iva
        
    def __str__(self):
        return f"PrintCost(total={self.total},iva={self.iva})"

    def to_tuble(self):
        return (self.name,self.img,self.printTime,self.filamentFK,self.printCostFK)
    
    def from_tuple(clss, tupleData):
        return clss(*tupleData)


if __name__ == "__main__":
    dbPritns = Print
    dbPritns.create_table()
    dbPritns.create('Test','test',1234)
    for i in dbPritns.get_table_rows():
        print(i)