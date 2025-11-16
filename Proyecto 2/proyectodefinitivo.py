#Autores : Felipe Jara - Renato Ortiz (sec.2)
# Cada línea contiene la  siguiente  información:  fecha  del  informe,  nombre  de  la  estación,  región,  comuna, 
#lugar, sitio, especie y total de muertes.

import matplotlib.pyplot as plt

#lee el archivo
def lectura_datos(nombre):
    lista = []
    x = open(nombre)
    for linea in x:
        linea = linea.rstrip('\n').split(',')
        lista.append(linea)
    x.close()
    return lista

#contador de las regiones con las aves muertas
def funcion_a(datos_ave):
    arica = 0
    tarapaca = 0
    antofagasta = 0
    atacama = 0
    coquimbo = 0
    valparaiso = 0
    ohiggins = 0
    maule = 0
    nuble = 0
    biobio = 0
    araucania = 0
    losrios = 0
    loslagos = 0
    aysen = 0
    magallanes = 0
    for linea_2 in datos_ave:
        if linea_2[2] in ['Arica y Parinacota', 'AricaParinacota']:
            arica = arica + int(linea_2[-1])
        if linea_2[2] in ['Tarapaca', 'Iquique']:
            tarapaca = tarapaca + int(linea_2[-1])
        if linea_2[2] in ['Antofagasta', 'Taltal', 'Tocopilla']:
            antofagasta = antofagasta + int(linea_2[-1])
        if linea_2[2] == 'Atacama':
            atacama = atacama + int(linea_2[-1])  
        if linea_2[2] == 'Coquimbo':
            coquimbo = coquimbo + int(linea_2[-1])
        if linea_2[2] == 'Valparaiso':
            valparaiso = valparaiso + int(linea_2[-1])
        if linea_2[2] == 'OÂ´Higgins':
            ohiggins = ohiggins + int(linea_2[-1])
        if linea_2[2] == 'Maule':
            maule = maule + int(linea_2[-1])
        if linea_2[2] == 'nuble':
            nuble = nuble + int(linea_2[-1])
        if linea_2[2] == 'Biobio':
            biobio = biobio + int(linea_2[-1])
        if linea_2[2] == 'Araucania':
            araucania = araucania + int(linea_2[-1])
        if linea_2[2] == 'Los Rios':
            losrios = losrios + int(linea_2[-1])
        if linea_2[2] == 'Los Lagos':
            loslagos = loslagos + int(linea_2[-1])
        if linea_2[2] == 'Aysen':
            aysen = aysen + int(linea_2[-1])
        if linea_2[2] == 'Magallanes':
            magallanes = magallanes + int(linea_2[-1])
    return arica, tarapaca, antofagasta, atacama, coquimbo, valparaiso, ohiggins, maule, nuble, biobio, araucania, losrios, loslagos, aysen, magallanes

#muertes en el mes de enero
def funcion_b(datos_ave):
    muertes_enero = 0
    for m_enero in datos_ave:
        if m_enero[0][3:5] == '01':
            muertes_enero = muertes_enero + int(m_enero[-1])
    return muertes_enero

#muertes de la especie Tagua en Cartagena
def funcion_c(datos_ave):
    muertes_tagua = 0
    for linea in datos_ave:
        if linea[3] == "Cartagena" and "Tagua" in linea[6]:
            muertes_tagua += int(linea[-1])
    return muertes_tagua

#muertes el 12 de febrero de 2023 de la especie piquero
def funcion_d(datos_ave):
    muertes_piquero = 0
    for linea in datos_ave:
        if linea[0] == "12-02-2023" and "Piquero" in linea[6]:
            muertes_piquero += int(linea[-1])
    return muertes_piquero

#gráfica de la función
def funcion_e(datos_ave, especies):
    muertes = [0] * len(especies)
    for linea in datos_ave:
        for i in range(len(especies)):
            if especies[i] in linea[6]:
                muertes[i] += int(linea[7])
    return muertes

#muestra gráfica y crea archivo
def mostrar_datos(ave_muertas_region, muertes_en_enero2023, muertes_tagua_cartagena, muertes_piquero_12f, muertes_especies):
    regiones = ['Arica y Parinacota', 'Tarapaca', 'Antofagasta', 'Atacama', 'Coquimbo', 'Valparaiso', 
        'O’Higgins', 'Maule', 'Ñuble', 'Biobio', 'Araucania', 'Los Rios', 'Los Lagos', 'Aysen', 'Magallanes']

    datos = []
    datos.append("Autor(es): Felipe Jara - Renato Ortiz")
    datos.append(   "Cantidad de aves muertas por región:")

    for region, muertes in zip(regiones, ave_muertas_region):
        datos.append(f"Nombre de la región: {region}, {muertes}")

    datos.append(f"\nCasos aves muertas mes enero del año 2023: {muertes_en_enero2023}")
    datos.append(f"\nEn la comuna de Cartagena se detectaron {muertes_tagua_cartagena} Taguas muertas.")
    datos.append(f"\nLas muertes detectadas para el 12 de febrero del 2023 de la especie Piquero son: {muertes_piquero_12f}")

    lista1 = []
    sal = open('resultadoS2.txt', 'w')
    for dato in datos:
        sal.write(dato+'\n')
    lista1.append(sal)
    sal.close()

    plt.bar(especies, muertes_especies, color=['blue', 'green', 'red', 'purple', 'black'],)
    plt.xlabel('Especies')
    plt.ylabel('Número de Muertes')
    plt.title('Muertes de Especies de Aves')
    plt.xticks(rotation = 12) #rota las etiquetas en x
    plt.subplots_adjust(bottom = 0.19) #ajusta el espacio entre las etiquetas(label)
    plt.margins(0.01) #crea margenes entre las barras del info.
    plt.show()

if __name__ == "__main__":
    datos_ave = lectura_datos('mortalidad_aves.txt')
    ave_muertas_region = funcion_a(datos_ave)
    muertes_en_enero2023 = funcion_b(datos_ave)
    muertes_tagua_cartagena = funcion_c(datos_ave)
    muertes_piquero_12f = funcion_d(datos_ave)
    especies = ["Gaviota garuma", "Piquero", "Gaviota de Franklin", "Pelicano", "Guanay"]
    muertes_especies_cantidad = funcion_e(datos_ave, especies)
    mostrar_datos(ave_muertas_region, muertes_en_enero2023, muertes_tagua_cartagena, muertes_piquero_12f, muertes_especies_cantidad)