import dearpygui.dearpygui as dpg
from components.adddata.valuePrint import ValuePrint
from logic.componentsEvent import *
class PrintComponent():
    def __init__(self):
       self.viewport()
    
    def body(self):
        with dpg.group(tag="GrupoTextos",horizontal=False,width=300):
            printName = dpg.add_input_text(label="Print name",tag="printName",parent="GrupoTextos")
            dpg.add_button(label="Add img",callback=self.addFileView)
            dpg.add_file_dialog(directory_selector=True, show=False, callback=self.fileCall, tag="file_dialog_id",cancel_callback=self.cancel_callback, width=700 ,height=400)
            with dpg.tree_node(label="Add color"):
                dpg.add_color_picker(height=100,width=100)
        Tipo= dpg.add_radio_button(label="Tipo",tag="Tipo",items=["Cantidad","Tanda"],callback=self.viewBatches,horizontal=True) 
        cuantityTands = dpg.add_input_int(label="Cuantity tands",tag="cuantityTands",show=False,default_value=1)  
        with dpg.group(tag="GrupoValores",horizontal=True,width=200):
            cantidad = dpg.add_input_int(label="Cantidad",tag="Cantidad",parent="GrupoValores")
            flamentoUtilizado =dpg.add_input_double(label="Filament used",tag="filamentUsed",parent="GrupoValores",format='%.2f')
            valorLaminador = dpg.add_input_double(label="Valor Laminador",tag="ValorLaminador",parent="GrupoValores",format='%.2f')
        dpg.add_spacing(count = 2)
        with dpg.group(horizontal=True):
            ValuePrint()
            dpg.add_button(label="Enviar", width=50 ,height= 50, callback=userAddDates)
    
    def viewport(self):
        with dpg.child_window(height=240):
            self.body()
    
    def addFileView(self): 
            dpg.configure_item("file_dialog_id",show=True)
      
    def viewBatches(self): 
        if dpg.get_value("Tipo") == "Tanda":
            dpg.configure_item("cuantityTands",show=True)
        else:
            dpg.configure_item("cuantityTands",show=False,default_value=0)

    def fileCall(self,sender, app_data):
        print('OK was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)

    def cancel_callback(self,sender, app_data):
        print('Cancel was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)

