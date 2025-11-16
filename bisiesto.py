año = int(input("Ingresar el año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0 ):
    print("El año",año,'si es bisiesto')
else:
    print("El año",año,"no es bisiesto")