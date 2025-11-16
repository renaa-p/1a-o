# Definir dos diccionarios
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'c': 5, 'd': 6}

# Obtener un conjunto de todas las claves
claves_totales = set(diccionario1.keys()).union(diccionario2.keys())

# Contar coincidencias
coincidencias = {}
for clave in claves_totales:
    if clave in diccionario1 and clave in diccionario2:
        coincidencias[clave] = (diccionario1[clave], diccionario2[clave])

# Mostrar resultados
print("Coincidencias:", coincidencias)
