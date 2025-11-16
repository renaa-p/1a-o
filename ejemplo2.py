# Autores Felipe Jara - Renato Ortriz     (Sec.2) 25/10/2024

def leer_archivo(nombre):
    f = open(nombre, 'r')
    contenido = f.read().replace("\n", " ")  # cambia \n por un espacio
    f.close()

    # separa los numeros y filtra ceros
    secuencia = [int(num) for num in contenido.split()]
    secuencia.append(0)  # añade un 0 al final

    return secuencia  # devuelve la lista de enteros

def encontrar_cimas(secuencia):
    cimas_info = []  # lista para almacenar información sobre las cimas
    n = len(secuencia)

    i = 1
    while i < n - 1:  # Recorre la secuencia
        # Se verifica si es cima
        if secuencia[i] > secuencia[i - 1] and secuencia[i] > secuencia[i + 1]:
            cimas_info.append((i, 1))  # Almacena la posición y la longitud (1)
            i += 1  # Avanza para seguir buscando
        # Se verifica si hay una secuencia de números iguales
        elif (i > 1 and secuencia[i] == secuencia[i - 1]) and (i < n - 2 and secuencia[i] == secuencia[i + 1]):
            j = i
            while j < n - 1 and secuencia[j] == secuencia[j + 1]:
                j += 1
            # Comprueba si los extremos son cimas
            if secuencia[i - 1] < secuencia[i] and secuencia[j + 1] < secuencia[j]:
                cimas_info.append((i, j - i + 1))  # Posición y cantidad de iguales
            i = j + 1  # Avanza después de la secuencia de iguales
        else:
            i += 1  # Si no es cima, solo avanza

    return cimas_info

def escribir_archivo(secuencias, nombre_archivo):
    f = open(nombre_archivo, 'w')

    for secuencia in secuencias:
        cimas = encontrar_cimas(secuencia)
        for posicion, longitud in cimas:
            f.write(f"{posicion + 1} {longitud}\n")
            f.write("\n")
        f.write("***\n")  # linea separadora
        f.write("\n") # reglon a los valores
    f.close()
    

if __name__ == "__main__":
    datos = leer_archivo("datos.txt")
    # agrupa los datos en secuencias separadas por el valor 0
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
