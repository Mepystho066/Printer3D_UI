import dearpygui.dearpygui as dpg 
from app.controller.search import search_user
class UserComponent():
    def __init__(self):
        self.viewport()
    
    def userInfo(self):
        with dpg.group(horizontal=True):
            with dpg.group(tag="grupUser", width=250):
                userID = dpg.add_input_text(label ="user ID", tag="userID")
                userName = dpg.add_input_text(label="User name", tag="userName",)
                lastName = dpg.add_input_text(label="Last name", tag="lastName",)
                userEmail = dpg.add_input_text(label="User email", tag="email",)
            dpg.add_button(label="search",callback=search_user)
    def addres(self):            
            with dpg.group(tag="address", width=250):
                conunty = dpg.add_input_text(label = "county" ,tag="county")
                city = dpg.add_input_text(label = "city" ,tag="city")
                addres = dpg.add_input_text(label = "addres" ,tag="addres")
                postalCode = dpg.add_input_text(label = "postalCode" ,tag="postalCode")

    def viewport(self):
        with dpg.group(horizontal=True):
            with dpg.child_window(width=400,height=105):
                self.userInfo()
            with dpg.child_window(width=400,height=105):
                self.addres()
            #with dpg.tree_node(label="Date time"):
            with dpg.child_window(width=180,height=170):
                Fecha= dpg.add_date_picker(label="Fecha",tag="Fecha",default_value={'month_day':2 , 'year': 123, 'month': 2})