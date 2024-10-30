from app.models.addres import Addres
from app.models.user import User
from app.models.settings import Setting
def createTables ():
    User().create_table()
    Addres().create_table()
    Setting().create_table()
