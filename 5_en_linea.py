import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300

def juego_crear():
    """Inicializar el estado del juego"""
    juego_5_linea=[]
    for x in range(10):
        valor=[]
        for y in range(10):
            valor.append(" ")
        juego_5_linea.append(valor)
    return juego_5_linea

def juego_actualizar(juego, x, y,caracter):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if (x<=295 and x>=5) and (y>=40 and y<=250):
        for i in range(10):
            cal=30*(i+1)
            if x<=cal:
                valor_x=i
                break
        for j in range(10):
            cal2=40+21*(j+1)
            if y<=cal2:
                valor_y=j
                break
        if juego[valor_x][valor_y]!=" ":
            return juego
        if caracter/2==caracter//2:
            juego[valor_x][valor_y]="O"
        else:
            juego[valor_x][valor_y]="X"
    return juego

def juego_mostrar(juego,caracter):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    gamelib.draw_rectangle(110, 10, 190, 30, outline='white',fill="")
    for x in range(len(juego)):
        for y in range(len(juego[0])):
            gamelib.draw_text(juego[x][y],18+x*29,50+y*21)
    gamelib.draw_rectangle(5, 40, 295, 250, outline='white',fill="")
    for i in range(10):
        for j in range(10):
            if i==9:
                continue
            gamelib.draw_line(30*(i+1), 40, 30*(i+1), 250, fill='white', width=0)
            if j==0:
                continue
            gamelib.draw_line(5, 21*(j+2), 295, 21*(j+2), fill='white', width=0)
    if caracter/2==caracter//2:
        gamelib.draw_text('Turno de: X', 150, 270)
    else:
        gamelib.draw_text('Turno de: O', 150, 270)

def main():
    juego = juego_crear()
    caracter=0
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego,caracter)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            caracter+=1
            juego = juego_actualizar(juego, x, y,caracter)
gamelib.init(main)
