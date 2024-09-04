import dearpygui.dearpygui as dpg
from db.db import *
def tagsDates():
    #User
    userID = dpg.get_value("userID")
    userName = dpg.get_value("userName")
    lastName = dpg.get_value("lastName")
    email = dpg.get_value("email")
    Fecha = dpg.get_value("Fecha")
    
    #address
    conunty = dpg.get_value("conunty")
    city = dpg.get_value("city")
    addres = dpg.get_value("addres")
    postalCode = dpg.get_value("postalCode")

    #Print
    printName = dpg.get_value("printName")
    FilamentoColor = dpg.get_value("FilamentoColor")
    Tipo = dpg.get_value("Tipo")
    cuantityTands = dpg.get_value("cuantityTands")
    Cantidad = dpg.get_value("Cantidad")
    filamentUsed = dpg.get_value("filamentUsed")
   
    #Values 
    ValorLaminador = dpg.get_value("ValorLaminador")
    Electricidad = dpg.get_value("Electricidad")
    PagoTrabajador = dpg.get_value("PagoTrabajador")
    ahorroImpresora = dpg.get_value("ahorroImpresora")
    ValorTotal = dpg.get_value("ValorTotal")
    ValorNeto = dpg.get_value("ValorNeto")
    
    return[userID,userName,lastName,userAddres,Fecha,printName,filamentUsed,FilamentoColor,Tipo,Cantidad,FlamentoUtilizado,ValorLaminador,Electricidad,PagoTrabajador,ahorroImpresora,ValorTotal,ValorNeto]

def userAddDates():
    print(tagsDates())

    