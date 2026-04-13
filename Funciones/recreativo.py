import tkinter as tk

# Configuración
TAM = 40
FILAS = 10
COLUMNAS = 15

# Laberinto (1 = pared, 0 = camino)
laberinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [0,1,1,1,0,1,0,0,1,1,1,0,1,0,1],
    [0,1,0,1,0,1,0,0,0,0,1,0,0,0,1],
    [0,1,1,1,0,1,0,0,0,0,1,1,1,0,1],
    [0,1,0,0,0,1,0,0,0,0,0,0,1,0,1],
    [0,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Posición inicial
jugador = [13, 8]

# Salida
salida = [2, 8]

# Ventana
ventana = tk.Tk()
ventana.title("Laberinto")

canvas = tk.Canvas(ventana, width=COLUMNAS*TAM, height=FILAS*TAM)
canvas.pack()

def dibujar():
    canvas.delete("all")
    
    for f in range(FILAS):
        for c in range(COLUMNAS):
            x1 = c * TAM
            y1 = f * TAM
            x2 = x1 + TAM
            y2 = y1 + TAM

            if laberinto[f][c] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    # Dibujar salida
    canvas.create_rectangle(
        salida[0]*TAM, salida[1]*TAM,
        salida[0]*TAM + TAM, salida[1]*TAM + TAM,
        fill="green"
    )

    # Dibujar jugador
    canvas.create_rectangle(
        jugador[0]*TAM, jugador[1]*TAM,
        jugador[0]*TAM + TAM, jugador[1]*TAM + TAM,
        fill="blue"
    )

def mover(evento):
    x, y = jugador

    if evento.keysym == "w":
        ny = y - 1
        nx = x
    elif evento.keysym == "s":
        ny = y + 1
        nx = x
    elif evento.keysym == "a":
        nx = x - 1
        ny = y
    elif evento.keysym == "d":
        nx = x + 1
        ny = y
    else:
        return

    # Verificar si es camino
    if laberinto[ny][nx] == 0:
        jugador[0], jugador[1] = nx, ny

    # Verificar victoria
    if jugador == salida:
        print("¡Ganaste!")
        ventana.destroy()

    dibujar()

ventana.bind("<Key>", mover)

dibujar()
ventana.mainloop()