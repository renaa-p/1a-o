#Autores : Felipe Jara - Renato Ortiz (sec.2)
# Cada línea contiene la  siguiente  información:  fecha  del  informe,  nombre  de  la  estación,  región,  comuna, 
#lugar, sitio, especie y total de muertes.

def lectura_datos(nombre):
    lista = []
    x = open(nombre)
    for linea in x:
        linea = linea.rstrip('\n').split(',')
        lista.append(linea)
    x.close
    return lista

def muerte_region_ave(datos_ave):
    Antofagasta = 0
    Aysen = 0
    Arica_y_Parinacota = 0
    Atacama = 0
    Bio_bio = 0
    Coquimbo = 0
    La_Araucania = 0
    OHiggins = 0
    Los_Lagos = 0
    Los_Ríos = 0
    Magallanes = 0
    Maule = 0
    nuble = 0
    Tarapaca = 0
    Valparaiso = 0
    for linea_2 in datos_ave:
        if linea_2[2] == 'Arica y Parinacota':
            Arica_y_Parinacota = Arica_y_Parinacota + int(linea_2[-1])
        if linea_2[2] == 'Antofagasta':
            Antofagasta = Antofagasta + int(linea_2[-1])
        if linea_2[2] == 'Tarapaca':
            Tarapaca = Tarapaca + int(linea_2[-1])
        if linea_2[2] == 'Coquimbo':
            Coquimbo = Coquimbo + int(linea_2[-1])
        if linea_2[2] == 'Maule':
            Maule = Maule + int(linea_2[-1])
        if linea_2[2] == 'Valparaiso':
            Valparaiso = Valparaiso + int(linea_2[-1])
        if linea_2[2] == 'Atacama':
            Atacama = Atacama + int(linea_2[-1])  
        if linea_2[2] == 'OÂ´Higgins':
            OHiggins = OHiggins + int(linea_2[-1])
        if linea_2[2] == 'nuble':
            nuble = nuble + int(linea_2[-1])
        if linea_2[2] == 'Biobio':
            Bio_bio = Bio_bio + int(linea_2[-1])
        if linea_2[2] == 'Los Rios':
            Los_Ríos = Los_Ríos + int(linea_2[-1])
        if linea_2[2] == 'Los Lagos':
            Los_Lagos = Los_Lagos + int(linea_2[-1])
        if linea_2[2] == 'Magallanes':
            Magallanes = Magallanes + int(linea_2[-1])
        if linea_2[2] == 'Aysen':
            Aysen = Aysen + int(linea_2[-1])
        if linea_2[2] == 'Araucania':
            La_Araucania = La_Araucania + int(linea_2[-1])
    return

def muertes_enero_2023(datos_ave):
    contador = 0
    for m_enero in datos_ave:
        if m_enero[0][3:5] < '02':
            contador = contador + int(m_enero[-1])
    print(contador)
   


if __name__ == "__main__":
    datos_ave = lectura_datos('mortalidad_aves.txt')
    muerte_region_ave(datos_ave)
    muertes_enero_2023(datos_ave)
    