import sys
import math

def resol_ec(a, b, c):
    discrimi = b**2 - 4 * a * c
    formul = (-b + (discrimi)**(1/2))/2*a
    formul1 = (-b - (discrimi)**(1/2))/2*a

    if discrimi < 0:
        print("no tiene solucion en los reales")
        sys.exit()
    elif discrimi == 0:
        raiz = -b / (2*a)
        print("La unica raiz es : ",raiz)
    elif discrimi > 0:
        raiz1 = (-b + math.sqrt(discrimi)) / (2*a)
        raiz2 = (-b - math.sqrt(discrimi)) / (2*a)
        print("Las raices son: ",raiz1 , "y", raiz2)


    x_vertice = -b / 2*a
    y_vertice = a * x_vertice**2 + b*x_vertice + c 
    print("El/Los vertice(s) son: ",x_vertice, y_vertice)

    concavidad = "hacia arriba" if a > 0 else "hacia abajo"
    print("La concavidad es",concavidad)

    longitud_lado_recto = abs(1/(4*a))
    print("La longitud del lado recto es de:", longitud_lado_recto)
    #ccordenadas foco
    if a > 0:
        x_foco = x_vertice
        y_foco = y_vertice + longitud_lado_recto
    else:
        x_foco = x_vertice
        y_foco = x_vertice - longitud_lado_recto
    print("El foco x son: ", x_foco, "y el foco y es:", y_foco)
    return

def resultado():
    a = float(input ("ingrese valor de a: "))
    b = float(input ("ingrese valor de b: "))
    c = float(input ("ingrese valor de c: "))
    
    x = resol_ec(a, b, c)

    

if  __name__ == "__main__":
    resultado()