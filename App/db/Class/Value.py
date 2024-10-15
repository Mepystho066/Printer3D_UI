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
class Value:
    def __init__(self,ValorLaminador,Electricidad,PagoTrabajador,ahorroImpresora,ValorTotal,ValorNeto):
        self.ValorLaminador = ValorLaminador
        self.Electricidad = Electricidad
        self.PagoTrabajador = PagoTrabajador
        self.ahorroImpresora = ahorroImpresora
        self.ValorTotal = ValorTotal
        self.ValorNeto = ValorNeto
    
    def save (self):
        string = ''''''
        cursor.execute(string,
                    self.ValorLaminador,self.Electricidad,
                    self.PagoTrabajador,self.ahorroImpresora,
                    self.ValorTotal,self.ValorNeto)

    @classmethod
    def create (clss):
        pass
    
   # @classmethod

    @classmethod
    def create_table(clsss): 
        cursor.execute('''CREATE TABLE IF NOT EXISTS 
        Filament(
            ValorLaminador INTEGER,
            Electricidad INTEGER,
            PagoTrabajador INTEGER,
            ahorroImpresora INTEGER,
            ValorTotal INTEGER,
            ValorNeto INGEGER )''')
        connection.commit()
    @classmethod
    def drop_table(clss):
        cursor.execute('''DROP TABLE IF EXISTS Filament''')
        connection.commit()