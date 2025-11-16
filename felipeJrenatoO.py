def leer_archivo(nombre):
    f = open(nombre, 'r')
    contenido = f.read().replace("\n", " ")  # cambia \n por un espacio
    f.close()
    # separa los numeros y filtra ceros
    secuencia = [int(num) for num in contenido.split()]
    secuencia.append(0)  # añade un 0 al final
    return secuencia  # devuelve la lista de enteros

def encontrar_cimas(secuencia):
    cimas_info = []  # Lista para almacenar información sobre las cimas
    n = len(secuencia)

    i = 1  # se inicia en 1 para evitar indice negativo
    while i < n - 1 :  # se recorre la secuencia
        # se verifica si es cima
        if secuencia[i] > secuencia[i - 1] and secuencia[i] > secuencia[i + 1]:
            cimas_info.append((i , 1)) 
            i += 1  # avanza para seguir buscando dentro de la misma secuencia
        if (i > 1 and secuencia[i] == secuencia[i - 1]) or (i < n - 2 and secuencia[i] == secuencia[i + 1]):
            j = i
            while j < n - 1 and secuencia[j] == secuencia[j + 1]:
                j += 1

            # comprueba si los extremos son cimas
            if secuencia[i - 1] < secuencia[i] and secuencia[j + 1] < secuencia[j]:
                cimas_info.append((i, j - i + 1))  # posicion y cantidad de iguales
            i = j + 1  # avanza después de la secuencia de iguales
        else:
            i += 1# si no es cima, solo avanza

    return cimas_info

def escribir_archivo(secuencias, nombre_archivo):
    f = open(nombre_archivo, 'w')
    for secuencia in secuencias:
        cimas = encontrar_cimas(secuencia)
        for posicion, longitud in cimas:
            print(cimas)
            f.write(f"\n{posicion + 1} {longitud}\n")  
        f.write("\n***\n")
    f.close()

if __name__ == "__main__":
    datos = leer_archivo("datos.txt")

    # Agrupa los datos en secuencias separadas por el valor 0
    secuencias = []
    secuencia_actual = []

    for num in datos:
        if num == 0:
            if secuencia_actual:  # solo si hay algo en la secuencia actual
                secuencias.append(secuencia_actual)
                secuencia_actual = []
        else:
            secuencia_actual.append(num)

    # agregar la ultima secuencia si no termino en 0
    if secuencia_actual:
        secuencias.append(secuencia_actual)

    escribir_archivo(secuencias, "cima.txt")
