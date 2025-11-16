import os
def abrir_archivo(nombre):
    f= open(nombre, 'r')
    return f.readlines()
#abre el archivo

def procesar_caso(caso_lineas):
    total_cantidad = 0
    total_unitario = 0
    #verifica el caso y si es el que se busca
    for linea in caso_lineas:
        partes = linea.split()
        if len(partes) >= 3 and partes[1].isdigit() and partes[2].replace(',', '').isdigit():
            try:
                cantidad = int(partes[1].replace(',', ''))
                unitario = float(partes[2].replace(',', ''))
                total_cantidad += cantidad
                total_unitario += unitario
            except ValueError:
                pass
    
    return total_cantidad, total_unitario

#se elige el caso
def extraer_caso(caso_id, lineas):
    caso_inicio = f'CASO {caso_id}'
    en_caso = False
    caso_lineas = []
    
    for linea in lineas:
        if caso_inicio in linea:
            en_caso = True
            continue 
        if en_caso:
            if 'CASO ' in linea and not caso_inicio in linea:
                break
            caso_lineas.append(linea.strip())
    
    return caso_lineas

#escribe el archivo nuevo que se pide
def escribir_archivo(nombre, caso_id, cantidad, unitario):
    with open(nombre, 'w' ) as f:
        f.write(f'CASO {caso_id}\n')
        f.write(f'Cantidad  {cantidad:,}\n')
        f.write(f'Unitario    {unitario:,.3f}\n')

if __name__ == "__main__":
        lineas = abrir_archivo("SetdePruebas.txt")
        caso_lineas = extraer_caso("3688580-4", lineas)
        cantidad_total, unitario_total = procesar_caso(caso_lineas)
        escribir_archivo("caso4.dat", "3688580-4", cantidad_total, unitario_total)
        print("Proceso completado exitosamente.  :)")


