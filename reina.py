import os.path

#Funciones

def validate_file_existence(file_path):
    v = False
    if os.path.isfile(file_path):
        v = True
    return v

def crearLista(N):
    tamaño = N*N
    tablero = []
    for i in range(tamaño):
        tablero.append(0)
    return tablero

def posicionesOcupadas(lista_tablero, lista_posiciones):
    for i in lista_posiciones:
        lista_tablero[i] = 1
    return lista_tablero


def mostrarLista(lista):
    print(lista)

def getFile(file, r):
    try:
        data = open(file, r)
        data = data.readlines()
        data1 = []
        for i in data:
            data1.append(i.split())
        return data1
    except Exception as e:
        print(e)


def interprete(fila, columna, N):
    posicion = fila * N + columna
    return posicion

def lista_ocupados(lista, N):
    c = 0
    ocupados = []
    for i in lista:
        fila = int(i[c]) - 1
        columna = int(i[c+1]) - 1
        posicion = interprete(fila,columna,N)
        ocupados.append(posicion)
        c += 1
        if c > 0:
            c = 0
    return ocupados

def arrivaMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while fila != 0:
        fila = fila - 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def abajoMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while fila != N-1:
        fila = fila + 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def izquierdaMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != 0:
        columna = columna - 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def derechaMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != N-1:
        columna = columna + 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def diagonalNorOesteMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != 0 and fila != 0:
        columna = columna - 1
        fila = fila - 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def diagonalSurEsteMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != N-1 and fila != N-1:
        columna = columna + 1
        fila = fila + 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def diagonalNorEsteMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != N-1 and fila != 0:
        columna = columna + 1
        fila = fila - 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def diagonalSurOesteMov(fila, columna, lista, N):
    contador = 0
    posicion = fila * N + columna
    while columna != 0 and fila != N-1:
        columna = columna - 1
        fila = fila + 1
        posicion = fila * N + columna
        if lista[posicion] == 1:
            break
        else:
            contador += 1
            lista[posicion] = 3
    return [lista, contador]

def sumaPosicionesReina(fila, columna, lista, N):
    acumulador = 0
    norte = arrivaMov(fila, columna, lista, N)
    acumulador += norte[1]
    lista = norte[0]
    sur = abajoMov(fila, columna, lista, N)
    acumulador += sur[1]
    lista = sur[0]
    oeste = izquierdaMov(fila, columna, lista, N)
    acumulador += oeste[1]
    lista = oeste[0]
    este = derechaMov(fila, columna, lista, N)
    acumulador += este[1]
    lista = este[0]
    noroeste = diagonalNorOesteMov(fila, columna, lista, N)
    acumulador += noroeste[1]
    lista = noroeste[0]
    sureste = diagonalSurEsteMov(fila, columna, lista, N)
    acumulador += sureste[1]
    lista = sureste[0]
    noreste = diagonalNorEsteMov(fila, columna, lista, N)
    acumulador += noreste[1]
    lista = noroeste[0]
    suroeste = diagonalSurOesteMov(fila, columna, lista, N)
    acumulador += suroeste[1]
    lista = suroeste[0]
    return [acumulador,lista]

def valido_tamano(tamano):
    v = False
    if tamano > 1:
        v = True
    return v

def valido_reina_limites(fila, columna, N):
    v = False
    if fila >= 0 and fila <= N-1 and columna >= 0 and columna <= N-1:
        v = True
    return v

def valido_obstaculo_cantidad(cantidad_obstaculos, lista_obstaculos):
    v = False
    if cantidad_obstaculos == len(lista_obstaculos):
        v = True
    return v

def valido_obstaculos_reina(posicion_reina, lista_obstaculos):
    v = True
    for i in lista_obstaculos:
        if i == posicion_reina:
            v = False
            break
    return v

def valido_obstaculos_limites1(lista_obstaculos, N):
    v = False
    n = (N*N)-1
    for i in lista_obstaculos:
        if i >= 0 and i <= n:
            v = True
    return v

def valido_obstaculos_limites2(subLista, N):
    v = True
    c = 0
    for i in subLista:
        a = int(i[c])
        b = int(i[c+1])
        if (a <= 0 or b <= 0) or (a > N or b > N):
            v = False
            break
        c += 1
        if c > 0:
            c = 0
    return v

def imprimir(lista, N):
    c = 0
    print(" ")
    for i in lista:
        print(i, end=' |  ')
        c += 1
        if c >= N:
            print(" ")
            c = 0


#------------ MAIN     --------------------------------

# ----------- ENTRADA  --------------------------------

if validate_file_existence('subir.txt'):
    data = getFile("subir.txt", 'r')  # CARGA DE ARCHIVO TXT

    N = int(data[0][0])  # DEFINO MATRIZ CUADRADA

    # PROCESO
    if valido_tamano(N):
        obstaculos = int(data[0][1])  # CANTIDAD DE OBSTÁCULOS
        fila = int(data[1][0]) - 1  # POSICIÓN DE LA REINA
        columna = int(data[1][1]) - 1
        posicion_reina = interprete(fila, columna, N)
        if valido_reina_limites(fila, columna, N):
            data1 = data[2:]  # SUB LISTA DE data CON SOLO LISTAS DE OBSTÁCULO
            table = crearLista(N)  # CREACIÓN DE TABLERO MATRIZ, EN REALIDAD UNA LISTA EN PYTHON
            table[posicion_reina] = 'X'
            ocupado = lista_ocupados(data1,
                                     N)  # LISTA CON LA POSICIÓN DE LOS OBSTÁCULOS EN LA LISTA DE PYTHON QUE REPRESENTA AL TABLERO MATRIZ
            if valido_obstaculo_cantidad(obstaculos, ocupado):
                if valido_obstaculos_reina(posicion_reina, ocupado):
                    if valido_obstaculos_limites2(data1, N):
                        tablero1 = posicionesOcupadas(crearLista(N), ocupado)  # LISTA DE TABLERO CON OBSTÁCULOS
                        total = sumaPosicionesReina(fila, columna, tablero1,
                                                    N)  # CANTIDAD TOTAL DE MOVIMIENTOS POSIBLES DE LA REINA
                        total[1][posicion_reina] = 'X'
                        # SALIDA
                        print("\n TABLERO INICIAL : ")
                        imprimir(table, N)
                        print("\n TABLERO CON OBSTÁCULOS : ")
                        imprimir(posicionesOcupadas(table, ocupado), N)
                        print("\n TABLERO FINAL : ")
                        imprimir(total[1], N)
                        print("\n TOTAL DE POSIBLES POSICIONES: ", total[0])  # IMPRIMO RESPUESTA
                    else:
                        print("\n LA POSICIÓN DE LOS OBSTÁCULOS DEBE ESTAR DENTRO DE LOS LÍMITES DE LA MATRIZ")
                else:
                    print("\n LA POSICIÓN DE LOS OBSTÁCULOS NO DEBE COICIDIR CON LA UBICACIÓN DE LA REINA")
            else:
                print("\n LA CANTIDAD DE OBSTÁCULOS DESCRITA NO COINCIDE CON EL NÚMERO DE LOS MISMOS")
        else:
            print("\n LA UBICACIÓN DE LA REINA NO ESTÁ DENTRO DE LOS LÍMITES DEL TABLERO DE MATRIZ ", N, "X", N)
    else:
        print("\n EL TAMAÑO DE LA MATRIZ NO ES VÁLIDO, DEBE SER MAYOR QUE 1. MATRICES CUADRADAS DE 2X2 EN ADELANTE")
else:
    print("NO EXISTE EL ARCHIVO")




