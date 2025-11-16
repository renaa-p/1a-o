def leer_archivo(nombre):
    f = open(nombre, 'r', encoding='UTF-8')
    return f.readlines()

def procesar_productos(productos_lineas):
#procesa los codigos(valores) y los devuelve en un diccioanrio
    productos = {}
    for linea in productos_lineas:
        partes = linea.strip().split(maxsplit=1)
        if len(partes) == 2:
            codigo = partes[0]
            descripcion = partes[1]
            productos[codigo] = descripcion
    return productos

def procesar_precios(precios_lineas):
#se procesam los precios y devuelve un diccionario
    precios = {}
    for linea in precios_lineas:
        partes = linea.strip().split()
        if len(partes) == 2:
            codigo = partes[0]
            try: #ocupo el try en caso de que se cambien los valores por error
                precio = float(partes[1].replace(',', ''))
                precios[codigo] = precio
            except ValueError:
                pass
    return precios

def procesar_ajustes(ajustes_lineas):
#se separan los ajustes
    ajustes = {}
    for linea in ajustes_lineas:
        partes = linea.strip().split()
        if len(partes) == 2:
            codigo = partes[0]
            ajuste = partes[1].replace('(', '').replace(')', '')
            try:
                if ajuste.endswith('%'):
                    ajuste = float(ajuste[:-1])
                else:
                    ajuste = float(ajuste)
                ajustes[codigo] = ajuste
            except ValueError:
                pass
    return ajustes

def aplicar_ajustes(precios, ajustes):
#se hacen los ajustes a los precios del diccioanrio
    resultados = []
    for codigo, precio in precios.items():
        ajuste = ajustes.get(codigo, 0)
        if ajuste > 0:
            precio_ajustado = precio * (1 + ajuste / 100)
        elif ajuste < 0:
            precio_ajustado = precio * (1 + ajuste / 100)
        else:
            precio_ajustado = precio
        resultados.append((codigo, precio, ajuste, precio_ajustado))
    return resultados

def salida( resultados, productos):
    print('Código   Producto                         Precio   Ajuste  Pventa.')
    print("__________________________________________________________________")
    total_precio = 0
    total_pventa = 0
    for resultado in resultados:
        codigo, precio, ajuste, pventa = resultado
        descripcion = productos.get(codigo, 'Desconocido')
        total_precio += precio
        total_pventa += pventa
        print(f'{codigo:<8} {descripcion:<30} {precio:>7,.0f} {ajuste:>7.1f}  {pventa:>7,.0f}')
    print("_________________________________________________________________")
    print(f'         Totales                                          ${total_pventa:,.0f}')

if __name__ == "__main__":
    productos_lineas = leer_archivo("productos.txt")
    precios_lineas = leer_archivo("precios.txt")
    ajustes_lineas = leer_archivo("ajuste.txt")
    productos = procesar_productos(productos_lineas)
    precios = procesar_precios(precios_lineas)
    ajustes = procesar_ajustes(ajustes_lineas)
    resultados = aplicar_ajustes(precios, ajustes)
    salida( resultados, productos)