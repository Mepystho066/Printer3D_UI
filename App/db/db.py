import sqlite3 as sql

class Tables:
    def __init__(self, path="App/db/data/dataBase.db"):
        self.connection = sql.connect(path) 
        self.cursor = self.connection.cursor()

    def createTables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas ( 
                id INTEGER PRIMARY KEY,
                printName TEXT,
                cuantityPrints integer,
                totalCost integer
        )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                lastName TEXT NOT NULL,
                email TEXT 
                country TEXT,
                city TEXT , 
                addres TEXT, 
                postalCode  INTEGER,
                facturaFK Integer,
                FOREIGN key (facturaFK) References factura(Id)
            )
        ''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS filamentCosts (
                id INTEGER PRYMARY KEY,
                cost INTEGER, 
                dateBuy date
            )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filaments  (
                id INTEGER PRIMARY KEY,
                filamentName TEXT,
                color COLOR ,
                companyName TEXT,
                filamentCostFK INTEGER,
                FOREIGN KEY (filamentCostFK) REFERENCES filamentCosts(id)
        )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS printCosts (
                id INTEGER PRYMARY KEY,
                iva DOUBLE, 
                totalValue INTEGER,
                date date
        )''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS prints (
                id INTEGER PRYMARY KEY, 
                name TEXT not null,
                img IMAGE,
                printTime INTEGER not null,
                filamentFK INTEGER,
                printCostFK INTEGER,
                FOREIGN KEY (filamentFK) REFERENCES filaments(id),
                FOREIGN KEY (printCostFK) REFERENCES  printCosts(id)
            )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS userPrints(
                userIdFK integer,
                printIdFK integer,
                cuantityPrints integer,
                dateSell date,
                FOREIGN KEY (printIdFK) REFERENCES prints(id),
                FOREIGN KEY (userIdFK) REFERENCES users(id),
                PRIMARY KEY (userIdFK, printIdFK)
            )''')

        self.connection.commit()
    # Tables insetions 
    def insert_factura(self,printName,cuantityPrints,totalCost):
        self.connection.execute(''' INSERT INTO facturas (printName ,cuantityPrints ,totalCost) VALUES (?,?,?)''',
         (printName,cuantityPrints,totalCost))
        self.connection.commit()

    def insert_users(self, id,name,lastName,email,conunty,city,addres,postalCode,facturaFK):
        self.cursor.execute('''
            INSERT INTO users (id,name,lastName,email,conunty,city,addres,postalCode,facturaFK) VALUES (?,?,?,?,?,?,?,?,?)''',
             (name,lastName,email,conunty,city,addres,postalCode,facturaFK))
        self.connection.commit()

    def insert_filamentCosts(self,cost,dateBuy):
        self.connection.execute(''' INSERT INTO filamentCosts (cost,dateBuy) VALUES (?,?)''', 
        (cost,dateBuy))
        self.connection.commit()

    def insert_filaments(self,filamentName,color,companyName,filamentCostFK):
        self.connection.execute(''' INSERT INTO filaments (filamentName,color,companyName,filamentCostFK) VALUES (?,?,?,?)''', 
        (filamentName,color,companyName,filamentCostFK))
        self.connection.commit()

    def insert_printCosts(self,iva,totalValue,date):
        self.connection.execute(''' INSERT INTO printCosts (iva,totalValue,date) VALUES (?,?,?,?)''', (
            iva,totalValue,date))
        self.connection.commit()

    def insert_prints(self,name,img,printTime,filamentFK,printCostFK):
        self.connection.execute(''' INSERT INTO prints (name,img,printTime,filamentFK,printCostFK) VALUES (?,?,?,?,?)''', 
        (name,img,printTime,filamentFK,printCostFK))
        self.connection.commit()

    def insert_userPrints(self,userIdFK,printIdFK,cuantityPrints,dateSell):
        self.connection.execute('''
        INSERT INTO userPrints (userIdFK,printIdFK,cuantityPrints,dateSell) VALUES (?,?,?,?)''', 
        (userIdFK,printIdFK,cuantityPrints,dateSell))
        self.connection.commit()

    def querysTable(self,nameTable):
        try :
            tables = ['facturas','users','filamentCosts','filaments','printCosts','prints','userPrints']
            if nameTable in tables:
                self.cursor.execute(f'SELECT * FROM {nameTable}')
                return self.cursor.fetchall()
        except ValueError: 
            print("filtro error ")
            return ValueError
            
    def SearchColumTable(self,nameTable,Colum,name):
        try :
            tables = ['facturas','users','filamentCosts','filaments','printCosts','prints','userPrints']
            if nameTable in tables:
                self.cursor.execute(f'SELECT * FROM {nameTable} where {nameTable}.{Colum} = {name}')
                return self.cursor.fetchall()
        except ValueError: 
            print("filtro error ")
            return ValueError
    def querysTableCombine (self, num):
        Combination = [['user','Factura' ,'facturaFK'], ['prints','printCosts','printCostFK'],['filament','filamentCosts','filamentCostFK']]
        try :
            #tables = ['facturas','users','filamentCosts','filaments','printCosts','prints','userPrints']
            if True:
                self.cursor.execute(f'SELECT * FROM {Combination[num][1]} join {Combination[num][2]} on {Combination[num][1]}.id = {Combination[num][2]}.{Combination[num][3]}  ')
                return self.cursor.fetchall() 
            #elif : 
        except ValueError: 
            print("filtro error ")
            return ValueError
        
"""
if __name__ =="__main__":
    tablas = Tables("App/db/data/dataBase.db")
    tablas.createTables()
    #tablas.insert_user()
    # #filamentName,color,companyName
   # tablas.insert_filaments('verde','#94bce0','Teste compani',1)
   
    #tablas.insert_factura('mascara larga',3,60000)
    users = tablas.querysTable('filaments')
    print(users)
""" 