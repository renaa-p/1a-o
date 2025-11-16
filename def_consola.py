import os

def limpiar_consola(valor):
    respuesta = valor
    if respuesta.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif respuesta.lower() == 'n':
        print("--------------------------------------------Ok---------------------------------------------------")

# Llama a la función para limpiar la consola si el usuario lo desea
if __name__ == '__main__':
    print("S: si, limpiar terminal                           N:no, mantener terminal")
    valor =(input("¿Deseas limpiar la consola? (s/n): "))
    limpiar_consola(valor)
