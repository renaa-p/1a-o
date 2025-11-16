#calcular la masa del aire

pres = float(input("Variable Presion: "))
volu = float(input("Variable Volumen: "))
temp = float(input("Variable Temperatura: "))
masa = ((pres + volu )/(0.37 * (temp +  460)))

print("La masa del aire elegido es de: ", masa)