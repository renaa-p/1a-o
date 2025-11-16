import math
import os

def limpiar_consola(respuesta):
    if respuesta.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')    
    return 

def volumen_cubo(lado):
    return lado ** 3

def area_cubo(lado):
    return 6 * lado ** 2

def vol_piramide(base_p, altura):
    area_p = base_p * base_p
    return (area_p * altura) / 3

def area_piramide(base_p, altura):
    apotema = math.sqrt(base_p**2-(altura**2)/4)
    return base_p**2 + ((base_p*4)*apotema)/2

def vol_rectangulo(ancho, altura, largo):
    return ancho * altura * largo

def area_parale(ancho, altura, largo):
    return 2*(ancho + largo)*altura + 2*(largo*ancho)

def vol_esfera(radio):
    return math.pi * (radio ** 3) * (4/3)

def area_esfera(radio):
    return math.pi *4 *radio**2

def vol_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura

def area_cilindro(radio, altura):
    return math.pi *2 * radio *(radio + altura)

def main():
    print("Bienvenido al calculador de áreas y volúmenes")
    print("Ahora se te dara a conocer las opciones de calculo y luego elegiras una de ellas.")
    print("Recuerda ingresar los datos sin unidades y transformados en centimetros respectivamente.")
    print("1. Volumen de un Cubo y su área")
    print("2. Volumen de un Paralelepipedo rectángular y su área")
    print("3. Volumen de una Piramide ,(Con base cuadrada) y área")
    print("4. Volumen de una Esfera y su área")
    print("5. Volumen del Cilindro y su área")
    
    opcion = int(input("Elige una opción para calcular, (1 hasta el 5): "))
    
    if opcion == 1:
        lado = float(input("Ingresa un lado del cubo: "))
        print("El Volumen de un Cubo es:", volumen_cubo(lado),"cm^3")
        print("El área del Cubo es:",area_cubo(lado),"cm^2")
        respuesta = input("¿Deseas limpiar la consola? (s/n): ")
        print("           s = Si        n = No            ")
        limpiar_consola(respuesta)
        print("-------------------------------------------FIN DE LA OPERACION-----------------------------------------------")

    elif opcion == 2:
        ancho = float(input("Ingresa la base del paralelepído: "))
        altura = float(input("Ingresa la altura del paralelepipedo: "))
        largo = float(input("Ingresar el largo del paralelepipedo"))
        print("El Volumen de un Paralelepipedo rectangular es:", vol_rectangulo(ancho, altura, largo),"cm^3")
        print("El área del paralelepipedo es rectangular:",area_parale(ancho, altura, largo),"cm^2")
        respuesta = input("¿Deseas limpiar la consola? (s/n): ")
        print("           s = Si        n = No            ")
        limpiar_consola(respuesta)
        print("-------------------------------------------FIN DE LA OPERACION-----------------------------------------------")

    elif opcion == 3:
        base_p = float(input("Ingresa un lado del cuadrado de la base de la piramide: "))
        altura = float(input("Ingresa la altura de la Piramide: "))
        print("El Volumen de la Piramide es:", vol_piramide(base_p, altura),"cm^3")
        print("El área de la piramide es:",area_piramide(base_p, altura),"cm^2")
        respuesta = input("¿Deseas limpiar la consola? (s/n): ")
        print("           s = Si        n = No            ")
        limpiar_consola(respuesta)
        print("-------------------------------------------FIN DE LA OPERACION-------------------------------------------------")

    elif opcion == 4:
        radio = float(input("Ingresa el radio de la esfera,(sin haberlo elevado): "))
        print("El Volumen de la esfera es:", vol_esfera(radio),"cm^3")
        print("El área de la esfera es:", area_esfera(radio),"cm^2")
        print("ten en cuenta que el resultado dado ya esta multiplicado por π")
        respuesta = input("¿Deseas limpiar la consola? (s/n): ")
        print("           s = Si        n = No            ")
        limpiar_consola(respuesta)
        print("-------------------------------------------FIN DE LA OPERACION------------------------------------------------")

    elif opcion == 5:
        radio = float(input("Ingresa el radio del cilindro(sin elevar): "))
        altura = float(input("Ingresa la altura del cilindro: "))
        print("El volumen del cilindro es:", vol_cilindro(radio, altura),"cm^3")
        print("El área del cilindro es :", area_cilindro(radio, altura),"cm^2")
        print("ten en cuenta que el resultado dado ya esta multiplicado por π")
        respuesta = input("¿Deseas limpiar la consola? (s/n): ")
        print("           s = Si        n = No            ")
        print("-------------------------------------------FIN DE LA OPERACION-------------------------------------------------")

    else:
        print("Eligio una opción no válida. Por favor, selecciona una opción válida..")
        print("-------------------------------------------FIN---------------------------------------------------")

if __name__ == "__main__":
    main()