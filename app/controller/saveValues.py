import dearpygui.dearpygui as dpg
from app.controller.componentsEvent import tagsDates
from app.models.addres import Addres
from app.models.user import User

def saveValues():
    # User
    userVal = tagsDates()[0]
    addresVal = tagsDates()[1]
    User().create(userVal[1],userVal[2],userVal[3])

    # Addres
    if userVal[0] != '':
        Addres().create(userVal[0],addresVal[0],addresVal[1],addresVal[2],addresVal[3])
    else:
        userid = User().get_fom_db()
        Addres().create(userid[-1].id,addresVal[0],addresVal[1],addresVal[2],addresVal[3])





def SetingsValues():
    pass