#autor renato ortiz

def cal_prome():
    estudiantes = {
        "Ana": [8, 9, 7, 10],
        "Julia": [8, 9, 7, 10],
        "Adriana": [8, 9, 7, 10],
        "Benjamín": [8, 9, 7, 10],
        "Diego": [8, 9, 7, 10],
        "Juan": [8, 9, 7, 10],
        "María": [9, 10, 9, 8],
        "Pedro": [7, 8, 6, 9]
    }
    promedios = {}
    minimo = {}
    maximo = {}
    for nombre, notas in estudiantes.items():
        promedios[nombre] = sum(notas) / len(notas)
        minimo[nombre] = min(notas)
        maximo[nombre] = max(notas)


    return promedios, minimo, maximo

if __name__ == "__main__":
    promedios, minimo, maximo = cal_prome()  
    print("                              Promedio      Min        Max     ")
    print("___________________________________________________________")
    for nombre in promedios:
        print(f"El promedio de {nombre:10} {promedios[nombre]:10.2f} {minimo[nombre]:10} {maximo[nombre]:10}")