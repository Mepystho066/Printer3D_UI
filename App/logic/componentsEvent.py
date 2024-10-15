import dearpygui.dearpygui as dpg
from logic.values import * 
from db.db import *
from db.Class import User,Addres,Print,Value
def tagsDates():
    #User={
    #    "ID":[],
    #    "Name":[],
    #    "LastName":[],
    #    "Email":[],
    #}
    user = User.User(
            ID=dpg.get_value("userID"),
            name=dpg.get_value("userName"),
            lastname= dpg.get_value("lastName"),
            email= dpg.get_value("email")
            )
   
    #User["userID"].append(dpg.get_value("userID"))
    #User["Name"].append(dpg.get_value("userName"))
    #User["LastName"].append(dpg.get_value("lastName"))
    #User["Email"].append(dpg.get_value("email"))
    addres= Addres.Addres(
        Country = dpg.get_value("country"),
        city = dpg.get_value("city"),
        addres = dpg.get_value("addres"),
        postalCode = dpg.get_value("postalCode")
    )
    #Addres={
    #    "Country":[],
    #    "city":[],
    #    "addres":[],
    #    "postalCode":[]
    #}
    #address
    #Addres["Country"].append(dpg.get_value("country"))
    #Addres["city"].append(dpg.get_value("city"))
    #Addres["addres"].append(dpg.get_value("addres"))
    #Addres["postalCode"].append(dpg.get_value("postalCode"))
    
    printClass = Print.Print(
                name= dpg.get_value("printName"),
                img="" ,
                printTime=Time() ,
                filamentFK="" ,
                printCostFK= ""
    )
    #Print={
    #    "name":[],
    #    "img":[],
    #    "printTime":[],
    #    "filamentFK":[],
    #    "printCostFK":[]
    #}
    #Print
    #Print["name"].append(dpg.get_value("printName"))
    #Print["img"].append("")
    #Print["printTime"].append(Time())
    #Print["filamentFK"].append("")
    #Print["printCostFK"].append("")
    
    value = Value.Value(
        ValorLaminador=dpg.get_value("ValorLaminador") ,
        Electricidad=dpg.get_value("Electricidad") ,
        PagoTrabajador=dpg.get_value("PagoTrabajador") ,
        ahorroImpresora=dpg.get_value("ahorroImpresora") ,
        ValorTotal=dpg.get_value("ValorTotal") ,
        ValorNeto=dpg.get_value("ValorNeto")
    )
    #Value = {
    #    "ValorLaminador":[],
    #    "Electricidad":[],
    #    "PagoTrabajador":[],
    #    "ahorroImpresora":[],
    #    "ValorTotal":[],
    #    "ValorNeto":[]
    #}
    #Values 
    #Value["ValorLaminador"].append(dpg.get_value("ValorLaminador"))
    #Value["Electricidad"].append(dpg.get_value("Electricidad"))
    #Value["PagoTrabajador"].append(dpg.get_value("PagoTrabajador"))
    #Value["ahorroImpresora"].append(dpg.get_value("ahorroImpresora"))
    #Value["ValorTotal"].append(dpg.get_value("ValorTotal"))
    #Value["ValorNeto"].append(dpg.get_value("ValorNeto"))
    #Date bill

    Fecha = dpg.get_value("Fecha")
    dpg.get_value("FilamentoColor")
    dpg.get_value("Tipo")
    dpg.get_value("Cantidad")
    dpg.get_value("cuantityTands")
    dpg.get_value("filamentUsed")
    
    return user,addres,printClass,value #User,Addres,Print,Value,Fecha

def userAddDates():
    user,addres,printClass,value = tagsDates()
     
    #,Addres,Print,Value,Fecha=
    print(user,"\n",addres,"\n",printClass,"\n",value ) #,"\n",Addres,"\n",Print,"\n",Value,"\n",Fecha)

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