#hola renato, para este caso se supone que es una mtrazi 16x16

def revisa(i):
    lista = []
    z = 1
    if len(i) <= 5 and len(i) >= 2 and i[-1] == "x":
        i[-1] = 0
        while z <= len(i):
            if int(i[z - 1]) < 5:
                pass
            else:
                return (f"El valor {int(i[z - 1])} no cumple las condiciones")
            z = z + 1
    else:
        return "No es un valor aceptable para la matriz 16x16"
    return "Los valores si cumplen para la matriz"

def equis(datos):
    ci = 1
    cf = 16
    fi = 1
    ff = 16
    j = 0
    while j < len(datos):
        if datos[0] == "1":
            cf = ff // 2
            ff = cf // 2
        elif datos[0] == "2":
            pass
        elif datos[0] == "3":
            pass
        elif datos[0] == "4":
            pass
        j = j + 1


if __name__ == "__main__":
    datos = input("Ingresar valores: ").split(" ")
    comprueba = revisa(datos)
    equis(datos)
    print(comprueba)
    print(datos)
