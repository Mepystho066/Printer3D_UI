import dearpygui.dearpygui as dpg 
import dearpygui.demo as demo
from view.userComponent import UserComponent
from view.printComponent import PrintComponent
from view.adddata.graphs import ViewGraphs
from view.settings import Settings
from view.style import Sytle
class Main():
    def __init__(self):
        self.viewport()
    
    def body(self):
        with dpg.window(label="Principal",tag="Principal"):
            with dpg.tab_bar():
                with dpg.tab(label="Add data"):
                    dpg.add_button(label="Documentos",callback=self.domuments)
                    UserComponent()
                    PrintComponent()
                    ViewGraphs()
                with dpg.tab(label="Settings"):
                    Settings()
                
    def viewport(self):
        dpg.create_context()
        dpg.create_viewport(title="DashBoard")
        #Ventana Principal
        self.body()    
        Sytle()    
        dpg.set_primary_window("Principal",True)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    def domuments(self):
        demo.show_demo()
    
if __name__ == "__main__":
    Main()