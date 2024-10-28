from app.service.db_service import request_query

class Print :
    NAME_CLASS = 'Print'

    #  Definimos los atributos
    def __init__(self, id: str = None,name: str = None,image:str = None,filamentFK:str = None,timePrint:str = None):

        self.id = id
        self.name = name
        self.image = image
        self.filamentFK = filamentFK
        self.timePrint = timePrint
        
    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"id={self.id},name={self.name},image={self.image},filamentFK={self.filamentFK},timePrint={self.timePrint}"

    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"id={self.id},name={self.name},image={self.image},filamentFK={self.filamentFK},timePrint={self.timePrint}"

    # -- Definimos metodos el objeto --

    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(name,image,filamentFK,timePrint) VALUES(?,?,?,?)'
        parameter = (self.name,self.image,self.filamentFK,self.timePrint)
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, name,image,filamentFK,timePrint):
        # Agregar los atributos que van a entrar
        obj = clss(name,image,filamentFK,timePrint)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(name= param[1], image=param[2],filamentFK=param[3],timePrint=param[4])
        obj.id = param[0] # Para objener el id si el objeto tine un id
        return obj

    @classmethod
    def get_for_id (clss,ID):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE id = ?'
        row = request_query(query,(ID)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        return obj

    @classmethod
    def get_for_name (clss,name):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE name = ?'
        row = request_query(query,(name)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        return obj


    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    name TEXT DEFAULT None,
                    image TEXT DEFAULT None,
                    filamentFK INTEGER,
                    timePrint INTEGER 
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)


class PrintCost:
    pass