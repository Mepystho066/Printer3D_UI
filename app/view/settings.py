import dearpygui.dearpygui as dpg
class Settings():
    def __init__(self):
       self.viewport()
    
    def body(self):
        with dpg.group(horizontal=True):

            with dpg.child_window(height=150,width=400):
                with dpg.group(tag="Values",width=200):
                    dpg.add_text("Values")
                    moneyValue = dpg.add_input_double(label="Money type",tag='MoneyType')
                    iva = dpg.add_input_double(label="IVA",tag='IVA')
                with dpg.group(tag="Electricity",width=200):
                    dpg.add_text("Electricity")
                    energyConsumption=dpg.add_input_double(label="Energy consumption"+" Kw",tag="energyConsumption")
                    # Agregar descripciones 
                    with dpg.tooltip("energyConsumption"):
                        dpg.add_text("Energia consumida por la impresora")
                    energyCost = dpg.add_input_double(label="Energy cost kw/h ",tag='EnergyCost')

            with dpg.child_window(height=150,width=420):
                dpg.add_text("Maintenance and machine cost")
                with dpg.group(tag="MaintenanceAndMachineCost",width=200):
                    printerCost= dpg.add_input_int(label="Printer Cost",tag='PrinterCost')
                    returnOnInvestment = dpg.add_slider_int(label="Return on investment Yeas",max_value=10,tag='ReturnYeas')
                    hoursCommercialUse= dpg.add_slider_int(label="hours of commercial use",tag="hoursCommercialUse",vertical=False,default_value=1,max_value=24,width=25)
                    repairCosts = dpg.add_slider_int(label="Repair costs %",tag="repairCosts",vertical=False,default_value=1,max_value=100,width=25)
                    #callback llamada para que se actualice
                    maintenanceCostTotal = dpg.add_slider_int(label="Maintenance cost total",tag="maintenanceCostTotal",vertical=False,width=25)
        with dpg.child_window(height=153):
            self.laborCost()

    def viewport(self):
            self.body()
   #def visualEvent(self): 
       

    def laborCost(self):
        dpg.add_text("Labor cost")
        with dpg.group(height=90,horizontal=True):
            with dpg.child_window(height=90,width=500):
                with dpg.group(tag="LaborCost"):
                    dpg.add_text("Preparación de la impresión")
                    workingTime = dpg.add_input_int(label="working time Hours",tag="workingTime")
                    # Agregar descripciones 
                    with dpg.tooltip("workingTime"):
                        dpg.add_text("texto")
                    costWorkinTime =dpg.add_input_double(label="Cost working time",tag="costWorkinTime")
            with dpg.child_window(height=90,width=650):
                with dpg.group(tag="PostProcessing"):
                    dpg.add_text("Post-processing")
                    postProcessingTime= dpg.add_slider_int(label="Post-processing time Hours",tag="postProcessingTime")
                    postProcessingCost = dpg.add_input_double(label="Post-processing time Cost",tag="postProcessingCost")

            dpg.add_button(label='save', height=50, width=50)
        totalLaborCost = dpg.add_input_double(label="Total labor cost",width=200,tag="totalLaborCost")

    