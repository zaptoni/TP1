def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador

    Ejemplo:

    >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
    ])
    '''
    grilla=[]
    y=len(desc)
    x=len(desc[0])
    for pos in range(y):
        caracteres=[]
        for posicion_carac in range(x):
            caracteres.append(desc[pos][posicion_carac])
        grilla.append(caracteres)
    return grilla

def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    dm=(len(grilla[0]),len(grilla))
    return dm

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return "#"==grilla[f][c]
def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return '.'==grilla[f][c] or '+'==grilla[f][c] or '*'==grilla[f][c]
def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return '$'==grilla[f][c] or '*'==grilla[f][c]
def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return'@'==grilla[f][c] or '+'==grilla[f][c]

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    objetivos=0
    dimen=dimensiones(grilla)
    for y in range(dimen[1]):
        for x in range(dimen[0]):
            if grilla[y][x]=="." or grilla[y][x]=="+":
                objetivos+=1
    return objetivos==0
def mover(grilla,direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.

    Nota aparte: Hay una variable llamada posicionamiento la cual es una tupla
    de forma (0,1,2,3,4,5); cada una de estos valores representa:
       °0-1:La posicion en la que se desea mover el jugador
       °2-3:La posicion que le sigue, se usara en la funcion "mover_con_caja"
        para saber si se la puede mover
       °4-5:La posicion en la que se encuentra el jugador
    '''
    copia_grilla=crear_grilla(grilla)
    posicionamiento=direccionar(grilla,direccion)

    if hay_pared(grilla,posicionamiento[1],posicionamiento[0])==False:
        caracter=(grilla[posicionamiento[0]][posicionamiento[1]])

        if hay_caja(grilla,posicionamiento[1],posicionamiento[0])==True:
            return mover_con_caja(copia_grilla,grilla,caracter,direccion)

        if grilla[posicionamiento[4]][posicionamiento[5]]=="+" or hay_objetivo(grilla,posicionamiento[1],posicionamiento[0])==True:
            return mover_con_objetivo(copia_grilla,grilla,caracter,direccion)
            
        copia_grilla[posicionamiento[0]][posicionamiento[1]]="@"
        copia_grilla[posicionamiento[4]][posicionamiento[5]]=" "

    return copia_grilla

def posicion_jugador(grilla):
    """Determinar columna y fila en donde esta el jugador"""
    dimen=dimensiones(grilla)
    for valor_x in range(dimen[1]):
        for valor_y in range(dimen[0]):
            if hay_jugador(grilla,valor_y,valor_x)==True:
                return (valor_y,valor_x)

def direccionar(grilla,direccion):
    """Saber posicion del jugador, casilla donde vas a moverte
    y la casilla siguiente (para saber si podes mover la caja)"""

    x_posicion=direccion[0]
    y_posicion=direccion[1]
    pla=posicion_jugador(grilla)

    x_movimiento=pla[1]+y_posicion
    y_movimiento=pla[0]+x_posicion
    x_movimiento_doble=pla[1]+y_posicion*2
    y_movimiento_doble=pla[0]+x_posicion*2
    x_jugador=pla[1]
    y_jugador=pla[0]

    return x_movimiento,y_movimiento,x_movimiento_doble,y_movimiento_doble,x_jugador,y_jugador

def mover_con_caja(copia_grilla,grilla,caracter,direccion):
    """Mover cuando en la direccion hay una caja o caja con objetivo"""
    posicionamiento=direccionar(grilla,direccion)

    if grilla[posicionamiento[2]][posicionamiento[3]]==" ":

        if grilla[posicionamiento[4]][posicionamiento[5]]=="+": 
            copia_grilla[posicionamiento[4]][posicionamiento[5]]="."
        else:
            copia_grilla[posicionamiento[4]][posicionamiento[5]]=" "

        if caracter=="*":                   
            copia_grilla[posicionamiento[0]][posicionamiento[1]]="+"
        else:
            copia_grilla[posicionamiento[0]][posicionamiento[1]]="@"

        copia_grilla[posicionamiento[2]][posicionamiento[3]]="$"


    elif grilla[posicionamiento[2]][posicionamiento[3]]==".":

        if grilla[posicionamiento[4]][posicionamiento[5]]=="@":
            copia_grilla[posicionamiento[4]][posicionamiento[5]]=""
        else:
            copia_grilla[posicionamiento[4]][posicionamiento[5]]="."

        if caracter=="$":
            copia_grilla[posicionamiento[0]][posicionamiento[1]]="@"
        else:
            copia_grilla[posicionamiento[0]][posicionamiento[1]]="+"

        copia_grilla[posicionamiento[2]][posicionamiento[3]]="*"
    return copia_grilla

def mover_con_objetivo(copia_grilla,grilla,caracter,direccion):
    """Mover cuando hay un objetivo en la direccion o el jugador esta en uno"""
    posicionamiento=direccionar(grilla,direccion)

    if grilla[posicionamiento[4]][posicionamiento[5]]=="+":
        copia_grilla[posicionamiento[4]][posicionamiento[5]]="."
    else:
        copia_grilla[posicionamiento[4]][posicionamiento[5]]=" "

    if caracter==".":
        copia_grilla[posicionamiento[0]][posicionamiento[1]]="+"
    else:
        copia_grilla[posicionamiento[0]][posicionamiento[1]]="@"

    return copia_grilla
