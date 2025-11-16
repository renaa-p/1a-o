#autor renato ortiz sec.2

import random #biblioteca que genera un sorteo (se ocupa en una funcion mas adelante)

def toma_precio():
    total = float(input("Ingresar el Total de los productos (sin punto/coma): "))
    return total

def verifica_total(total):
    if total >= 100000:
        return True
    else:
        return False

def ruleta_descuento(verificacion):
    if verificacion is True:
        descuentos = [
            {"color": "BLANCA", "descuento": 0},
            {"color": "ROJA", "descuento": 10},
            {"color": "AZUL", "descuento": 20},
            {"color": "AMARILLO", "descuento": 25},
            {"color": "VERDE", "descuento": 50}
        ]
        seleccion = random.choice(descuentos)
        color = seleccion["color"]
        descuento = seleccion["descuento"]
        return color, descuento, color

def calcula_total(descuento, total):
    total_f = (total * descuento)/100
    return total_f

def imprime():
    pass

if __name__ == "__main__":
    total = toma_precio()
    verificacion = verifica_total(total)
    descuento = ruleta_descuento(verificacion)
    final_descuento = calcula_total(descuento, total)
    imprime(final_descuento, descuento)
    print(descuento)