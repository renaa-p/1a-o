# autor: renato ortiz, s2
def calcular_tiempo(vi, m):
    tiempo_impacto = m / vi
    return tiempo_impacto

def mostrar(resultado):
    print(f"El proyectil interseptara el objetivo en {resultado} hora/s, o en {resultado * 60} minuto/s")

if __name__ == "__main__":
    millas = 1
    velocidad_objeto = 40 #nudos
    velocidad_proyectil = 50 # nudos
    velocidad_entre_obl_pro = velocidad_proyectil - velocidad_objeto
    resultado = calcular_tiempo(velocidad_entre_obl_pro, millas)
    mostrar(resultado)