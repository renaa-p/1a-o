def ecua(a,b,c):
    x1 = (c - b) / a
    return x1

def datos():
    a = float(input("Ingresa el coeficiente a: "))
    b = float(input("Ingresa el coeficiente b: "))
    c = float(input("Ingresa el coeficiente c: "))

    x = ecua(a,b,c)

    print("El valor de x es:", x)

if  __name__ == "__main__":
    datos()