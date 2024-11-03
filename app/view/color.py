import dearpygui.dearpygui as dpg
from app.controller.saveValues import saveColor
from app.models.filaments import Filament
class Color():
    def __init__(self):
        self.viewport()
    def body(self):
        with dpg.group(height=115,horizontal=True):
            with dpg.group(horizontal=True,width=225):
                self.table_color()
            with dpg.child_window(height=115, width=200):
               # with dpg.tree_node(label="add"):
                dpg.add_color_picker(height=100, width=100)
            with dpg.group(horizontal=False,height=100, width=120):
                dpg.add_input_text(label="Name", tag="filamentName")
                dpg.add_input_text(label="Color", tag= "filamentColor")
                dpg.add_input_text(label="Company",tag="company")
                dpg.add_input_text(label="Value", tag="filamentValue")
            dpg.add_button(label="Add",height=50,width=50,callback= saveColor)

    def viewport(self):
            self.body()
    def table_color (self):
        with dpg.child_window(height=115):
            with dpg.table(tag="color_table", header_row=True) as selectablerows:
                dpg.add_table_column(label="name")
                dpg.add_table_column(label="color")
                dpg.add_table_column(label="value")

                for i in Filament().get_fom_db():
                    with dpg.table_row():
                        for j in range(3):
                            dpg.add_selectable(label=f"{j}", callback=self.clb_selectable, user_data=j)
               
    def clb_selectable(self, sender, app_data, user_data):
        print(f"Row {user_data}")