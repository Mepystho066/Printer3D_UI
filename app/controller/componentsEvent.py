import dearpygui.dearpygui as dpg
from app.service.db import *
def tagsDates():
    #User
    userID = dpg.get_value("userID")
    userName = dpg.get_value("userName")
    lastName = dpg.get_value("lastName")
    email = dpg.get_value("email")

    userList=[userID,userName,lastName,email]
    #address
    county = dpg.get_value("county")
    city = dpg.get_value("city")
    addres = dpg.get_value("addres")
    postalCode = dpg.get_value("postalCode")
    address = [county,city,addres,postalCode]
    #Print
    printName = dpg.get_value("printName")
    FilamentoColor = dpg.get_value("FilamentoColor")
    Tipo = dpg.get_value("Tipo")
    cuantityTands = dpg.get_value("cuantityTands")
    Cantidad = dpg.get_value("Cantidad")
    filamentUsed = dpg.get_value("filamentUsed")
    pintList = [printName,FilamentoColor,Tipo,cuantityTands,Cantidad,filamentUsed]
    #Values
    hours =dpg.get_value("hours")
    minuts = dpg.get_value("minuts")
    ValorLaminador = dpg.get_value("ValorLaminador")
    Electricidad = dpg.get_value("Electricidad")
    PagoTrabajador = dpg.get_value("PagoTrabajador")
    ahorroImpresora = dpg.get_value("ahorroImpresora")
    ValorTotal = dpg.get_value("ValorTotal")
    ValorNeto = dpg.get_value("ValorNeto")
    valuestList = [hours,minuts,ValorLaminador,Electricidad,PagoTrabajador,ahorroImpresora,ValorTotal,ValorNeto]

    Fecha = dpg.get_value("Fecha")

    return [userList, address ,pintList ,valuestList,Fecha]

def userAddDates():
    print(tagsDates())

def settingsDate():
    MoneyType
    IVA
    energyConsumption
    EnergyCost
    PrinterCost
    ReturnYeas
    hoursCommercialUse
    repairCosts
    maintenanceCostTotal