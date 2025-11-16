#Autor : Renato Ortiz
def abrir1(nombre):
#abre el primer texto y guarda los datos
    f = open(nombre, encoding="UTF-8")
    x1 = []
    for linea in f:
        x1.append(linea.rstrip("\n"))
        f.close
    return x1

def abrir2(nombre):
#abre segundo texto y guarda los datos
    f = open(nombre, encoding="UTF-8")
    x2 = []
    for linea in f:
        x2.append(linea.rstrip("\n"))
        f.close
    return x2

def time(x1,x2):
#saca los tiempos
    tiempos100 = []
    tiempos200 = []
    for linea in x1:
        if len(linea) > 22:
            tiempos100.append(linea.split("- ")[-1])
    for linea in x2:
        if len(linea) > 22:
            tiempos200.append(linea.split("- ")[-1])
    return tiempos100, tiempos200

def dat_nom(x1,x2):
#saca nombres
    nombre100 = []
    nombre200 = []
    for linea in x1:
        if len(linea) >22:
            nombre100.append(linea.split("(")[0])
    for linea in x2:
        if len(linea) >22:
            nombre200.append(linea.split("(")[0])
    return nombre100, nombre200

def diferencia():
    dif1001= 9.77 - 9.58 
    dif1002 =  9.77 - 9.63
    dif2001 = 19.53 - 19.19 
    dif2002 = 19.53 - 19.30 
    return dif1001, dif1002, dif2001, dif2002

def escribir_archivo(nombre, datos):
    with open(nombre, 'w', encoding="UTF-8") as f:
        for dato in datos:
            f.write(dato + "\n")

def salida100(nombres, tiempos, dif):
    with open("record100.txt", 'w', encoding="UTF-8") as f:
        f.write("Año          Atleta              Tiempo(seg)")
        f.write("\n"f"2009   wr   {nombres[0][0]:20}    {tiempos[0][0]}")
        f.write("\n"f"2012   wo   {nombres[0][1]:20}    {tiempos[0][1]}")
        f.write("\n"f"2024   1    {nombres[0][2]:20}    {tiempos[0][2]}")
        f.write("\n"f"2024   2    {nombres[0][3]:20}    {tiempos[0][3]}")
        f.write("\n"f"2024   wr   diferencia de tiempo    {dif[0]}")
        f.write("\n"f"2024   wo   diferencia de tiempo    {dif[1]}")


def salida200(nombres, tiempos,dif):
    with open("record200.txt", 'w', encoding="UTF-8") as f:
        f.write("Año          Atleta              Tiempo(seg)")
        f.write("\n"f"2009   wr   {nombres[1][0]:20}    {tiempos[1][0]}")
        f.write("\n"f"2012   wo   {nombres[1][1]:20}    {tiempos[1][1]}")
        f.write("\n"f"2024   1    {nombres[1][2]:20}    {tiempos[1][2]}")
        f.write("\n"f"2024   2    {nombres[1][3]:20}    {tiempos[1][3]}")
        f.write("\n"f"2024   wr   diferencia de tiempo    {dif[2]}")
        f.write("\n"f"2024   wo   diferencia de tiempo    {dif[3]}")

if __name__=="__main__":
    x1 = abrir1("wr100.txt")
    x2 = abrir2("wr200.txt")
    tiempos = time(x1,x2)
    nombres = dat_nom(x1,x2)
    dif = diferencia()
    salida100(nombres,tiempos,dif)
    salida200(nombres,tiempos,dif)

    
