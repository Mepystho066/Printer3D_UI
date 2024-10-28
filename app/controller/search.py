import dearpygui.dearpygui as dpg
from app.controller.componentsEvent import *
from app.models.user import User

def search_user():

    userData = tagsDates()[0]
    addresData = tagsDates()[1]
    def setInfo(ObjetUser,ObjetAddres):
        # User
        userID = dpg.set_value("userID", ObjetUser.id)
        userName = dpg.set_value("userName", ObjetUser.name)
        lastName = dpg.set_value("lastName", ObjetUser.lastname)
        email = dpg.set_value("email", ObjetUser.email)
        # Addres
        county = dpg.set_value("county",ObjetAddres)
        city = dpg.set_value("city",ObjetAddres)
        addres = dpg.set_value("addres",ObjetAddres)
        postalCode = dpg.set_value("postalCode",ObjetAddres)

    if userData[0] != '' :
        date_search = User().get_for_id(userData[0])
        setInfo(date_search)

    elif userData[1] != ''  :
        date_search = User().get_for_name(userData[1])
        setInfo(date_search)




