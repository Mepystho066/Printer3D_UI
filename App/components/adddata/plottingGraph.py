import dearpygui.dearpygui as dpg
class PlottingGraphs():
    def __init__(self):
       self.viewport()
    
    def body(self):
        DiccionarioVentas ={
        "fecha":[],
        "nombre":[],
        "tipo_Impresion":[],
        "filamentoColor":[],
        "tipoDeCantidades":[], 
        "cantidad":[],
        "filamentoUtilizado":[],
        "valorLaminador":[],
        "Tiempo":[],
        "electricidadValor":[],
        "PagoTrabajador":[],
        "ahorroImpresora":[], 
        "valorTotal":[],
        "valorNeto":[]
        }

        espacio=[]
        for i in range(len(DiccionarioVentas["valorNeto"])):
            espacio.append(i)
        with dpg.tab(label="Gafica"):
            dpg.add_button(label="Actualizacion", callback=self.visualEvent)
            with dpg.plot(tag="GraficaInferior",width=-1,height=-1):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
                
                dpg.add_line_series(espacio,DiccionarioVentas["PagoTrabajador"],label="Pago Trabajador",parent="y_axis",tag="series 0")
                dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 0"))#MenuPersonalizado
                dpg.add_line_series(espacio,DiccionarioVentas["ahorroImpresora"],label="Ahorro Impresora",parent="y_axis",tag="series 1")
                dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 1"))
                dpg.add_line_series(espacio,DiccionarioVentas["valorTotal"],label="Valor Total",parent="y_axis",tag="series 2")
                dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 2"))
                dpg.add_line_series(espacio,DiccionarioVentas["valorNeto"],label="Valor Neto",parent="y_axis",tag="series 3")
                dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 3"))
                
    def viewport(self):
        self.body()

    def visualEvent(self): 
        espacio=[]
        for i in range(len(DiccionarioVentas["valorNeto"])):
            espacio.append(i)   

        dpg.set_value("series 0",[espacio,DiccionarioVentas["PagoTrabajador"]])
        dpg.set_value("series 1",[espacio,DiccionarioVentas["ahorroImpresora"]])
        dpg.set_value("series 2",[espacio,DiccionarioVentas["valorTotal"]])
        dpg.set_value("series 3",[espacio,DiccionarioVentas["valorNeto"]])

        espacio1 = [i*10 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio2 = [i*10+1 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio3 = [i*10+2 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio4 = [i*10+3 for i in range(len(DiccionarioVentas["valorNeto"]))]
        dpg.set_value("series 0.0",[espacio1,DiccionarioVentas["PagoTrabajador"]])
        dpg.set_value("series 0.1",[espacio2,DiccionarioVentas["ahorroImpresora"]])
        dpg.set_value("series 0.2",[espacio3,DiccionarioVentas["valorTotal"]])
        dpg.set_value("series 0.3",[espacio4,DiccionarioVentas["valorNeto"]])


   