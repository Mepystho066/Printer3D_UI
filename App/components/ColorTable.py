import dearpygui.dearpygui as dpg 
from db.db import *

class ColorTable():
    def __init__(self):
        self.viewport()

    def body(self):
        ColorDictionary = self.dataColor()
        with dpg.table(tag="TableColor"):
            Nombre = dpg.add_table_column(label="Name")
            Color = dpg.add_table_column(label="Color")
            Company = dpg.add_table_column(label="Company")
            for i in ColorDictionary:
                with dpg.table_row():
                    for j in range(1,len(i)):
                        dpg.add_selectable(label=f"{i[j]}", callback=self.userEvent, user_data=(i))

    def userEvent(self,sender,app_data,user_data):
        print(user_data)
        #return user_data

    def dataColor(self):
        Filaments = Tables().querysTable('filaments')
        return Filaments

    def viewport(self):
        with dpg.tree_node(label="Color table"):
            with dpg.child_window(height=100,width=250):
                self.body()