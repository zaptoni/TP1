def crear_grilla(desc):
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
    dm=(len(grilla[0]),len(grilla))
    return dm
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''

def hay_pared(grilla, c, f):
    if '#'==grilla[f][c]:
        return True
    else:
        return False
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''

def hay_objetivo(grilla, c, f):
    if '.'==grilla[f][c]:
        return True
    elif '+'==grilla[f][c]:
        return True
    elif '*'==grilla[f][c]:
        return True
    else:
        return False
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''

def hay_caja(grilla, c, f):
    if '$'==grilla[f][c]:
        return True
    elif '*'==grilla[f][c]:
        return True
    else:
        return False
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''

def hay_jugador(grilla, c, f):
    if '@' in grilla[f][c]:
        return True
    elif '+' in grilla[f][c]:
        return True
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''

def juego_ganado(grilla):
    objetivos=0
    objetivos_con_caja=0
    objetivos_con_jugador=0
    dimen=dimensiones(grilla)
    for y in range(dimen[1]):
        for x in range(dimen[0]):
            if "."==(grilla[y][x]):
                objetivos+=1
            elif "+"==(grilla[y][x]):
                objetivos_con_jugador+=1
            elif "*"==(grilla[y][x]):
                objetivos_con_caja+=1
    if objetivos==objetivos_con_jugador==0 and objetivos_con_caja>0:
        return True
    else:
        return False
    '''Devuelve True si el juego está ganado.'''
def mover(grilla,direccion):
    place=direccionar(grilla,direccion)
    if (grilla[place[0]][place[1]])!="#":
        caracter=(grilla[place[0]][place[1]])
        if (grilla[place[2]][place[3]])!=("#" and "$" and "*"):
            if (grilla[place[2]][place[3]])=="$" and (grilla[place[0]][place[1]])=="$":
                return crear_grilla(grilla)
            elif (grilla[place[2]][place[3]])=="#" and (grilla[place[0]][place[1]])=="*":
                return crear_grilla(grilla)
            elif(grilla[place[2]][place[3]])=="." and (grilla[place[0]][place[1]])=="*":
                new=crear_grilla(grilla)
                (new[place[0]][place[1]])="+"
                (new[place[2]][place[3]])="*"
                return new
            elif (grilla[place[2]][place[3]])=="#" and (grilla[place[0]][place[1]])=="$":
                return crear_grilla(grilla)
            elif (grilla[place[2]][place[3]])=="$" and (grilla[place[0]][place[1]])=="*":
                return crear_grilla(grilla)
            elif (grilla[place[0]][place[1]])==" " and (grilla[place[4]][place[5]])=="+":
                new=crear_grilla(grilla)
                (new[place[4]][place[5]])="."
                (new[place[0]][place[1]])="@"
                return new
            elif caracter=="$" and (grilla[place[2]][place[3]])==".":
                new=crear_grilla(grilla)
                (new[place[2]][place[3]])="*"
                (new[place[0]][place[1]])="@"
                (new[place[4]][place[5]])=" "
                return new
            elif caracter=="$" and (grilla[place[2]][place[3]])==" ":
                new=crear_grilla(grilla)
                (new[place[2]][place[3]])="$"
                (new[place[0]][place[1]])="@"
                (new[place[4]][place[5]])=" "
                return new
            elif caracter==".":
                new=crear_grilla(grilla)
                (new[place[0]][place[1]])="+"
                (new[place[4]][place[5]])=" "
                return new
            else:
                new=crear_grilla(grilla)
                (new[place[0]][place[1]])="@"
                (new[place[4]][place[5]])=" "
                return new
        else:
            return crear_grilla(grilla)
    else:
        return crear_grilla(grilla)

def posicion_jugador(grilla):
    """Determinar columna y fila en donde esta el jugador"""
    dimen=dimensiones(grilla)
    for valor_x in range(dimen[1]):
        for valor_y in range(dimen[0]):
            if "@"==grilla[valor_x][valor_y] or "+"==grilla[valor_x][valor_y]:
                return (valor_y,valor_x)
def direccionar(grilla,direccion):
    x=direccion[0]
    y=direccion[1]
    pla=posicion_jugador(grilla)
    x1=pla[1]+y
    y1=pla[0]+x
    x2=pla[1]+y*2
    y2=pla[0]+x*2
    z2=pla[0]
    z1=pla[1]
    return x1,y1,x2,y2,z1,z2
