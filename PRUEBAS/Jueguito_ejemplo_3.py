import tkinter as tk
import random
from tkinter import messagebox

FILAS = 8
COLUMNAS = 8
CANTIDAD_MINAS = 10

ventana = tk.Tk()
ventana.title("Buscaminas 💣")

# Diccionario para guardar nuestros botones y lista para las minas
botones = {}
minas = []
juego_terminado = False

def preparar_minas():
    # Creamos una lista con todas las coordenadas posibles (0,0 hasta 7,7)
    posiciones = [(f, c) for f in range(FILAS) for c in range(COLUMNAS)]
    # Elegimos 10 al azar
    return random.sample(posiciones, CANTIDAD_MINAS)

def contar_minas_cerca(f, c):
    contador = 0
    # Revisamos la cuadrícula de 3x3 alrededor de la casilla
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (f + i, c + j) in minas:
                contador += 1
    return contador

def clic_izquierdo(f, c):
    global juego_terminado
    # Si el juego acabó o la casilla ya se presionó, no hacemos nada
    if juego_terminado or botones[(f,c)]["state"] == "disabled": 
        return
    
    # 1. ¿Pisamos una mina?
    if (f, c) in minas:
        botones[(f,c)].config(text="💥", bg="red")
        juego_terminado = True
        messagebox.showinfo("Boom", "¡Pisaste una mina! Fin del juego.")
        return
    
    # 2. Si no es mina, contamos las cercanas y hundimos el botón
    minas_cerca = contar_minas_cerca(f, c)
    botones[(f,c)].config(state="disabled", relief=tk.SUNKEN, bg="lightgrey")
    
    # 3. Si hay minas cerca, mostramos el número
    if minas_cerca > 0:
        botones[(f,c)].config(text=str(minas_cerca))
    # 4. ¡RECURSIVIDAD! Si es 0, abrimos las vecinas automáticamente
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= f+i < FILAS and 0 <= c+j < COLUMNAS:
                    clic_izquierdo(f+i, c+j) # La función se llama a sí misma

def clic_derecho(event, f, c):
    if juego_terminado or botones[(f,c)]["state"] == "disabled": 
        return
    
    # Poner o quitar bandera roja
    texto_actual = botones[(f,c)].cget("text")
    if texto_actual == "🚩":
        botones[(f,c)].config(text="", fg="black")
    else:
        botones[(f,c)].config(text="🚩", fg="red")

# --- CONSTRUCCIÓN DE LA INTERFAZ ---
minas = preparar_minas()

for f in range(FILAS):
    for c in range(COLUMNAS):
        # Creamos el botón
        btn = tk.Button(ventana, width=3, height=1, font=("Arial", 12, "bold"),
                        command=lambda fila=f, col=c: clic_izquierdo(fila, col))
        btn.grid(row=f, column=c)
        
        # Le atamos el clic derecho (Button-3 o Button-2 dependiendo del mouse)
        btn.bind("<Button-3>", lambda event, fila=f, col=c: clic_derecho(event, fila, col))
        
        # Lo guardamos en el diccionario usando su coordenada (f, c) como llave
        botones[(f, c)] = btn

ventana.mainloop()