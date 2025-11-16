#Autores Kevin Navarro - Renato Ortiz sec.2
import random # biblioteca que da un valor aleatorio de una lista que nosotros proporcionemos.

def mostrar_tablero(tablero):
    for i in range(0, 9, 3):
        print(f"{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
        if i < 6:
            print("--+---+--")

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in combinacion):
            return True
    return False

def jugada_computadora(tablero):
    # verificar si puede ganar en esta jugada
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "C"
            if verificar_ganador(tablero, "C"):
                return i
            tablero[i] = " "  # deshacer jugada

    # verificar si debe bloquear al jugador
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = "H"
            if verificar_ganador(tablero, "H"):
                tablero[i] = "C"
                return i
            tablero[i] = " "  # deshacer jugada

    # jugar aleatoriamente en una posicion disponible
    posiciones_disponibles = [i for i in range(9) if tablero[i] == " "]
    eleccion = random.choice(posiciones_disponibles)
    tablero[eleccion] = "C"
    return eleccion

def jugar(): #Crea la interfaz del juego y ofrece un menu semi-interactivo
    print("¡Bienvenido al juego del Gato!")
    while True:
        tablero = [" "] * 9
        dado_humano = random.randint(1, 6) 
        dado_computadora = random.randint(1, 6)

        print(f"Lanzamiento de dados: Humano -> {dado_humano}, Computadora -> {dado_computadora}")
        turno_humano = dado_humano >= dado_computadora # las lineas anteriores son para decidir quien parte el juego

        while " " in tablero:
            mostrar_tablero(tablero)
            if turno_humano:
                print("Turno del Humano.")
                while True:
                    posicion = int(input("Elige una posición (1-9): ")) - 1
                    if tablero[posicion] == " ":
                        tablero[posicion] = "H"
                        break
                    else:
                        print("Esa posición ya está ocupada. Intenta nuevamente.")
            else:
                print("Turno de la Computadora.")
                jugada_computadora(tablero)

            if verificar_ganador(tablero, "H"):
                mostrar_tablero(tablero)
                print("¡Felicidades! Ganaste.")
                break
            elif verificar_ganador(tablero, "C"):
                mostrar_tablero(tablero)
                print("¡La Computadora gana!")
                break

            turno_humano = not turno_humano

        else:
            mostrar_tablero(tablero)
            print("¡Es un empate!")
        reiniciar = input("¿Quieres jugar de nuevo? (0 = Sí, 1 = No): ")
        if reiniciar != "0":
            print("¡Gracias por jugar!")
            break #termina el recorrido del codigo

if __name__ == "__main__":
    jugar()
