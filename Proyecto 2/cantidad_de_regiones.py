def leer_fichero(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        datos.append(linea.rstrip('\n').split(','))
    ent.close()
    return datos

def funcion_a(datos):
    return [region[2] for region in datos]

def funcion_b(regiones):
    regiones_unicas = []
    for region in regiones:
        if region not in regiones_unicas:
            regiones_unicas.append(region)
    return regiones_unicas

def muestra_datos(regiones_unicas):
    print("Regiones:")
    for region in regiones_unicas:
        print(region)

if __name__ == "__main__": 
    datos= leer_fichero('mortalidad_aves.txt')
    regiones = funcion_a(datos)
    regiones_unicas = funcion_b(regiones)
    muestra_datos(regiones_unicas)