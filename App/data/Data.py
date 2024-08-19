"""
Cobrabrar 10 pesos por hora de diseño 
coste de tiempo de imprecion 5000 por hora 
costo luz filamento y maquina lo del valorLaminador y agregar el coste de maquina 
dos años y medio de vida ultil 20.283
la depreciación por hora 1.500.000 /  = 75 pesos por hora de uso. lo cambio a 1.000
lo minimo que se paga de tiempo es 1 hora 

coste de luz , filamento, 75 pesos por hora 
#diseño de producto de continudidad es unao pero el precio de un moñeco es uno 
#sacar una tabla de cuanto custa vivir 

crear una tabla diferente para el coste del diseño 
"""
"""
Variables que se deberia tener en la base de datos 
Fecha 
Nombre 
tipo De impresion
valorLaminador
Valor Trabajador
Tiempo
ValorTotal

"""
fecha_actual = datetime.datetime.now()
year_actual = fecha_actual.year
month_actual = fecha_actual.month
day_actual = fecha_actual.day

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
