
def lectura():
    edad = input('Ingresar edad: ')
    ed_an = bool(input('Meses = False  / Año = True : '))
    hemo = float(input("Ingresar hemoglobina: "))
    sexo = input('1 = Mujer / 0 = Hombre : ')
    return[edad, ed_an, hemo, sexo]

def analis(datos):
    
    return

def mostrar_resul(resultado):
    print(resultado)

if __name__ == '__main__':
   datos = lectura()
   resultado = analis(datos)
   mostrar_resul(resultado)
   print(datos)