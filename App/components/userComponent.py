import dearpygui.dearpygui as dpg 

class UserComponent():
    def __init__(self):
        self.viewport()
    
    def body(self):
            with dpg.group(tag="grupUser", width=300):
                userID = dpg.add_input_text(label ="user ID", tag="userID")
                userName = dpg.add_input_text(label="User name", tag="userName",)
                lastName = dpg.add_input_text(label="Last name", tag="lastName",)
                userAddres = dpg.add_input_text(label="User addres", tag="userAddres",)
    def viewport(self):
        with dpg.group(horizontal=True):
            with dpg.child_window(width=400,height=105):
                self.body()
            with dpg.tree_node(label="Date time"):
                with dpg.child_window(width=200,height=180):
                    Fecha= dpg.add_date_picker(label="Fecha",tag="Fecha",default_value={'month_day':2 , 'year': 123, 'month': 2})