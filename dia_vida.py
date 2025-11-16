from datetime import date
print()
año = int(input("Ingresar el año: "))
mes = int(input("Ingresar el mes: "))
dia = int(input("Ingresar el Dia: "))
fecha_nacimiento = (date(año, mes, dia))
hoy = date.today()
calcular_dias_vida = (hoy - fecha_nacimiento)
print("La persona ha vivido aproximadamente: ",calcular_dias_vida)