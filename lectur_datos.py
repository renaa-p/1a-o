def abrir_fichero(nombre_archivo):
    f = open(nombre_archivo, 'r', encoding='UTF-8')

    for linea in f:
        linea = linea.rstrip('\n').split(',')
        x = linea[2]
        i = x[6:7].split()
        z = linea[2][:4]
        if z == ['2022'] or ['2023']: 
            if i == ['7']:
                print(x)
        

if __name__=='__main__':
    lista = abrir_fichero('guias.dat')