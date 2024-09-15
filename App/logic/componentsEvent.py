import dearpygui.dearpygui as dpg
from logic.values import * 
from db.db import *

def tagsDates():
    User={
        "userID":[],
        "Name":[],
        "LastName":[],
        "Email":[],
    }
    #User
    User["userID"].append(dpg.get_value("userID"))
    User["Name"].append(dpg.get_value("userName"))
    User["LastName"].append(dpg.get_value("lastName"))
    User["Email"].append(dpg.get_value("email"))
    Addres={
        "Country":[],
        "city":[],
        "addres":[],
        "postalCode":[]
    }
    #address
    Addres["Country"].append(dpg.get_value("country"))
    Addres["city"].append(dpg.get_value("city"))
    Addres["addres"].append(dpg.get_value("addres"))
    Addres["postalCode"].append(dpg.get_value("postalCode"))
    Print={
        "name":[],
        "img":[],
        "printTime":[],
        "filamentFK":[],
        "printCostFK":[]
    }
    #Print
    Print["name"].append(dpg.get_value("printName"))
    Print["img"].append("")
    Print["printTime"].append(Time())
    Print["filamentFK"].append("")
    Print["printCostFK"].append("")
    Value = {
        "ValorLaminador":[],
        "Electricidad":[],
        "PagoTrabajador":[],
        "ahorroImpresora":[],
        "ValorTotal":[],
        "ValorNeto":[]
    }
    #Values 
    Value["ValorLaminador"].append(dpg.get_value("ValorLaminador"))
    Value["Electricidad"].append(dpg.get_value("Electricidad"))
    Value["PagoTrabajador"].append(dpg.get_value("PagoTrabajador"))
    Value["ahorroImpresora"].append(dpg.get_value("ahorroImpresora"))
    Value["ValorTotal"].append(dpg.get_value("ValorTotal"))
    Value["ValorNeto"].append(dpg.get_value("ValorNeto"))
    #Date bill

    Fecha = dpg.get_value("Fecha")
    dpg.get_value("FilamentoColor")
    dpg.get_value("Tipo")
    dpg.get_value("Cantidad")
    dpg.get_value("cuantityTands")
    dpg.get_value("filamentUsed")
    
    return User,Addres,Print,Value,Fecha

def userAddDates():
    User,Addres,Print,Value,Fecha= tagsDates()
    print(User,"\n",Addres,"\n",Print,"\n",Value,"\n",Fecha)

def addData():
    tabla = Tables("App/db/data/dataBase.db")
    tablas.createTables()
    User,Addres,Print,Value,Fecha = tagsDates()
    print(Fecha)
    #table.insert_factura()
    tabla.insert_users(User["userID"],User["Name"],User["LastName"],User["Email"],Addres["Country"],Addres["city"],Addres["addres"],Addres["PostalCode"])
    #table.insert_printCosts()
    #table.insert_filaments()
    tabla.insert_prints(Print["name"],Print["img"],Print["printTime"],Print["filamentFK"],Print["printCostFK"])
    #table.insert_filamentCosts()
    #table.insert_userPrints()
    


## Agragar factura 