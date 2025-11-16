#autor renato ortiz sec2
gripe_porcina_diccionario = {
    "Escualeno": ["C", "H"],
    "DL-α-tocoferol": ["C", "H", "O"],
    "Polisorbato 80": ["C", "H", "O"],
    "Fenol": ["C", "H", "O"],
    "Timerosal": ["Hg"],
    "Lactosa": ["C", "H", "O"],
    "Neomicina": ["N", "O"],
    "Gentamicina": ["N", "O"],
    "Formaldehído": ["C", "H", "O"]
}

gripe_aviar_diccionario = {
    "Hidróxido de aluminio": ["Al"],
    "Timerosal": ["Hg"],
    "Sacarosa": ["C", "H", "O"],
    "Neomicina": ["N", "O"],
    "Gentamicina": ["N", "O"],
    "Formaldehído": ["C", "H", "O"],
    "Ácido cítrico": ["C", "H", "O"],
    "Citrato trisódico": ["Na", "C", "H", "O"],
    "Etanol": ["C", "H", "O"],
    "Polisorbato 80": ["C", "H", "O"],
    "2-hidroxipropil-β-ciclodextrina": ["C", "H", "O"],
    "Cloruro de sodio": ["Na", "Cl"],
    "Ácido clorhídrico": ["H", "Cl"],
    "Hidróxido de sodio": ["Na", "O", "H"]
}

covid19_janssen_diccionario = {
   "Ácido cítrico": ["C", "H", "O"],
    "Citrato trisódico": ["Na", "C", "H", "O"],
    "Etanol": ["C", "H", "O"],
    "Polisorbato 80": ["C", "H", "O"],
    "2-hidroxipropil-β-ciclodextrina": ["C", "H", "O"],
    "Cloruro de sodio": ["Na", "Cl"],
    "Ácido clorhídrico": ["H", "Cl"],
    "Hidróxido de sodio": ["Na", "O", "H"]
}

def elementos_comunes(junte):
    coincidencias = {}
    for comunes in junte:
        if comunes in gripe_aviar_diccionario and comunes in gripe_porcina_diccionario and comunes in covid19_janssen_diccionario:
            coincidencias[comunes] = (gripe_porcina_diccionario[comunes], gripe_aviar_diccionario[comunes],covid19_janssen_diccionario[comunes])
    return coincidencias

if __name__ == "__main__":
    junte = set(gripe_porcina_diccionario.keys()).union(gripe_aviar_diccionario.keys()).union(covid19_janssen_diccionario.keys())
    resultado = elementos_comunes(junte)

    with open('dictmatchvacuna.txt', 'w') as f:
        f.write(str(resultado))

    print("El archivo dictmatchvacuna.txt ha sido creado con el diccionario de datos resultante. ")
    print(resultado)
