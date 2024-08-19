import dearpygui.dearpygui as dpg
class Settings():
    def __init__(self):
       self.viewport()
    
    def body(self):
        with dpg.group(horizontal=True):

            with dpg.child_window(height=150,width=400):
                with dpg.group(tag="Values",width=200):
                    dpg.add_text("Values")
                    moneyValue = dpg.add_input_double(label="Money value")
                    iva = dpg.add_input_int(label="IVA")
                with dpg.group(tag="Electricity",width=200):
                    dpg.add_text("Electricity")
                    energyConsumption=dpg.add_input_double(label="Energy consumption | W |")
                    energyCost = dpg.add_input_double(label="Energy cost | kw/h |")
       
            with dpg.child_window(height=150,width=420):
                dpg.add_text("Maintenance and machine cost")
                with dpg.group(tag="MaintenanceAndMachineCost",width=200):
                    printerCost= dpg.add_input_double(label="Printer Cost")
                    returnOnInvestment = dpg.add_input_int(label="Return on investment | Yeas |")
                    hoursCommercialUse= dpg.add_slider_int(label="hours of commercial use",tag="hoursCommercialUse",vertical=False,default_value=1,max_value=24,width=25)
                    repairCosts = dpg.add_slider_int(label="Repair costs | % |",tag="repairCosts",vertical=False,default_value=1,max_value=100,width=25)
                    #callback llamada para que se actualice
                    maintenanceCostTotal = dpg.add_slider_double(label="Maintenance cost total",tag="maintenanceCostTotal",vertical=False,width=25)
        with dpg.child_window(height=153):
            self.laborCost()
       
       
        #with dpg.group(tag="PostProcessing"):
        #with dpg.group(tag="PostProcessing"):
        #with dpg.group(tag="PostProcessing"):

    def viewport(self):
            self.body()
   #def visualEvent(self): 
       

    def laborCost(self):
        dpg.add_text("Labor cost")
        with dpg.group(height=90,horizontal=True):
            with dpg.child_window(height=90,width=500):
                with dpg.group(tag="LaborCost"):
                    dpg.add_text("Preparación de la impresión")
                    workingTime = dpg.add_input_int(label="working time | Hours |")
                    costWorkinTime =dpg.add_input_double(label="Cost working time")
            with dpg.child_window(height=90,width=650):
                with dpg.group(tag="PostProcessing"):
                    dpg.add_text("Post-processing")
                    postProcessingTime= dpg.add_input_double(label="Post-processing time | Hours |")
                    postProcessingCost = dpg.add_input_double(label="Post-processing time")
        totalLaborCost = dpg.add_input_double(label="totalLaborCost")

    # Agregar descripciones 
    #with dpg.tooltip("tag"):
    #    dpg.add_text("texto")