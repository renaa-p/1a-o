peso = float(input("Ingresa tu peso(kg):"))
estatura = float(input("Ingresa tu estatura(mts):"))

imc = (peso / estatura**2)
print(imc)
if imc<15:
    print("Delgadez muy severa")
elif 15<=imc<=15.9:
    print("Delgadez severa")
elif 16<=imc<=18.9:
    print("Delgadez")
elif 19.5<=imc<=24.5:
    print("Peso saludable")
elif 25<=imc<=29.9:
    print("Sobre-peso")
elif imc>40:
    print("Waton")