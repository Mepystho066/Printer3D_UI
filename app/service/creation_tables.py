from app.models.addres import Addres
from app.models.user import User

def createTables ():
    User().create_table()
    Addres().create_table()