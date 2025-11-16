import sys
def resol_ec(a, b, c):
    discrimi = b**2 - 4 * a * c
    formul = (-b + (discrimi)**(1/2))/2*a
    formul1 = (-b - (discrimi)**(1/2))/2*a

    if discrimi < 0:
        print("no tiene solucion en los reales")
        sys.exit()
    elif discrimi == 0:
        print("tiene una solucion en los reales")
    elif discrimi > 0:
        print("tiene dos soluciones en los reales")

    return formul, formul1

def resultado():
    a = float(input ("ingrese valor de a: "))
    b = float(input ("ingrese valor de b: "))
    c = float(input ("ingrese valor de c: "))
    
    x = resol_ec(a, b, c)

    print("El valor de x es:", x)

if  __name__ == "__main__":
    resultado()