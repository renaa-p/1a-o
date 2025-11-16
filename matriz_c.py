def f_abrir():

    try:
        f = open('matriz.txt', 'r', encoding='UTF-8')
        
        contenido = f.read().rstrip()
        
        a = list(contenido[2:4]+contenido[5:7])
        b = list(contenido[10:12]+ contenido[13:15])
        print("A:",a , "B:",b)
        i = 0
        while i < 4:
            c = (int(a[i])+ int(b[i]))
            print("C",[i + 1],":",c)
            i = i + 1 

        f.close()

    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return contenido


if __name__ == '__main__':
    lista = f_abrir()
    

