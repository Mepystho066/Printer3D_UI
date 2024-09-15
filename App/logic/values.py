import dearpygui.dearpygui as dpg
def Cost():
#se agrega un valor agregado que seria el del trabajador 
    cantidad =dpg.get_value("cuantityTands")
    valorLaminador=dpg.get_value("ValorLaminador")
    filamentoUtilizado=dpg.get_value("filamentUsed")
    trabajador= 200 * filamentoUtilizado  
    impresoraAhorro = (200 *Time())+(2000000/20000)*Time()
    if dpg.get_value("Tipo")=="Tanda":
        cantidadTanda= dpg.get_value("CantidadTanda")
        TiempoTotal= (Time()*cantidadTanda)
        
    else:
        TiempoTotal= Time()    
    Total = cantidad *(valorLaminador+trabajador)
    valorNeto = Total -(cantidad*(trabajador+ValueElectricity()))
    dpg.set_value("Electricidad",ValueElectricity())
    dpg.set_value("PagoTrabajador",trabajador)
    dpg.set_value("ValorAhorroImpresora",impresoraAhorro)
    dpg.set_value("ValorTotal",Total)
    dpg.set_value("ValorNeto",valorNeto)
   
def Time():
    horas= dpg.get_value("Horas") or 0
    minutos = dpg.get_value("Minutos") or 0
    tiempoT = (minutos/60) + horas
    return tiempoT

def ValueElectricity():
    precioLuzKWh = 800.74
    consumoImpresora = 0.3
    valorTotal= (Time()*consumoImpresora)*precioLuzKWh
    return valorTotal

def Values(sender,app_data,user_data):
    fechas= dpg.get_value(user_data[0])
    fecha = "{}/{}/20{}".format(fechas['month_day'],fechas['month'],(fechas['year']-100))
    nombre = dpg.get_value(user_data[1])
    impresion= dpg.get_value(user_data[2])
    filamentoColor= dpg.get_value(user_data[3])
    tipoDeCantidades= dpg.get_value(user_data[4])
    cantidad= dpg.get_value(user_data[5])
    filamentoUtilizado= dpg.get_value(user_data[6])
    ValorLaminador= dpg.get_value(user_data[7])
    tiempo= user_data[8]
    valorElectricidad= dpg.get_value(user_data[9])
    pagoTrabajador= dpg.get_value(user_data[10])
    ahorroImpresora= dpg.get_value(user_data[11])
    valorTotal= dpg.get_value(user_data[12])
    valorNeto= dpg.get_value(user_data[13])

    DiccionarioVentas["fecha"].append(fecha)
    DiccionarioVentas["nombre"].append(nombre)
    DiccionarioVentas["tipo_Impresion"].append(impresion)
    DiccionarioVentas["filamentoColor"].append(filamentoColor)
    DiccionarioVentas["tipoDeCantidades"].append(tipoDeCantidades)
    DiccionarioVentas["cantidad"].append(cantidad)
    DiccionarioVentas["filamentoUtilizado"].append(filamentoUtilizado)
    DiccionarioVentas["valorLaminador"].append(ValorLaminador)
    DiccionarioVentas["Tiempo"].append(tiempo)
    DiccionarioVentas["electricidadValor"].append(valorElectricidad)
    DiccionarioVentas["PagoTrabajador"].append(pagoTrabajador)
    DiccionarioVentas["ahorroImpresora"].append(ahorroImpresora)
    DiccionarioVentas["valorTotal"].append(valorTotal)
    DiccionarioVentas["valorNeto"].append(valorNeto)
    insertRow(fecha,nombre,impresion,filamentoColor,tipoDeCantidades,cantidad,
                filamentoUtilizado,ValorLaminador,tiempo,valorElectricidad,
                pagoTrabajador,ahorroImpresora,valorTotal,valorNeto)
    """Fecha,Nombre,Impresion,FilamentoColor,Tipo,
        Cantidad,FlamentoUtilizado,ValorLaminador,
        Tiempo(),ValorElectricidad(),PagoTrabajador,
        ahorroImpresora,ValorTotal,valorNeto"""
