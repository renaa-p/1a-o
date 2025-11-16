def valores():
    print("Ingresar valores enteros porfavor (menos el %)")
    monto = int(input('Escribe el monto inicial: '))
    num_cuotas = int(input('Cantidad de cuotas mensuales: '))
    tasa_inte = int(input('Ingresar la tasa (%):'))
    return [monto , num_cuotas , tasa_inte]

def interes_comp(datos):
    tasa_mensual = datos[2] / 12 / 100 #tasa interes mensual
    cuota = datos[0] * (tasa_mensual / ( 1 - (1 + tasa_mensual)**(datos[1])))
    total_pagado = cuota * datos[1]
    return cuota , total_pagado, tasa_mensual

def interes_fijo(datos):
    pass

if __name__ == '__main__':
    datos = valores()
    compuesto = interes_comp(datos)
    print(compuesto)