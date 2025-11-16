#ingresar digitos de la ecuacion
a = float(input("Ingresar numero de a: "))
b = float(input("Ingresar numero de b: "))
c = float(input("Ingresar numero de c: "))

dis = (b**2) - (4 * a * c)

if dis < 0:
    print("Tu ecuación no tiene solucion en los reales")
if dis > 0:
    r_ecua1 = (b + ((b**2) - (4 * a * c))**(1/2)) / (2 * a)
    r_ecua2 = (b - ((b**2) - (4 * a * c))**(1/2)) / (2 * a)
    print("Tu ecuación tiene 2 soluciones en los reales: ",r_ecua1 ,"y", r_ecua2)
if dis == 0:
    print("Tu ecuación tiene una solucion en los reales: ", r_ecua2)
    r_ecua2 = (b - ((b**2) - (4 * a * c))**(1/2)) / (2 * a)
