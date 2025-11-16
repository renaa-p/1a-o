def bisiesto(año):
    if año%4 == 0 and (año%100!=0 or año%400==0):
        print("Tu año si es bisiesto")
    else:
        print("No es bisiesto")
        

bisiesto(int(input("Ingresa tu año:")))