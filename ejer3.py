def procesar_votos(archivo):
    with open(archivo, 'r') as f:
        #lee solo primera y segunda línea del archivo(suponiendo que el ejemplo sea asi)
        lineas = f.readlines()
        coaliciones = lineas[0].strip().split(';')
        votos = lineas[1].strip().split('$')
    votos_partidos = {}
    
    for voto in votos:
        if voto in votos_partidos:
            votos_partidos[voto] += 1
        else:
            votos_partidos[voto] = 1
    resultados = {}
    
    for coalicion in coaliciones:
        nombre_coalicion, partidos = coalicion.split(':')
        partidos = partidos.split('-')
        
        total_votos_coalicion = 0
        for partido in partidos:
            if partido in votos_partidos:
                total_votos_coalicion += votos_partidos[partido]
        
        resultados[nombre_coalicion] = (partidos, total_votos_coalicion)
    ganadora = max(resultados, key=lambda c: resultados[c][1])
    
    # resultados
    for coalicion, (partidos, total) in resultados.items():
        print(f"Coalición: {coalicion}")
        for partido in partidos:
            print(f"{partido} {votos_partidos.get(partido, 0)}")
        print(f"Total coalición {coalicion}: {total}\n")
    
    print(f"La coalición ganadora es {ganadora} con {resultados[ganadora][1]} votos.")

if __name__ == "__main__":
    procesar_votos('elección.txt')
