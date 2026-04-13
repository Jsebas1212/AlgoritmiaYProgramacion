import tkinter as tk

# --- LÓGICA DEL JUEGUITO ---
# Usamos una variable global para guardar los puntos
puntos = 0

def incrementar_puntos():
    global puntos
    puntos += 1
    # Actualizamos el texto de la etiqueta en la pantalla
    etiqueta_puntos.config(text=f"¡Puntos: {puntos}!")
    
    # Un pequeño easter egg para cuando llegues a 10 ;)
    if puntos == 10:
        etiqueta_titulo.config(text="¡NIVEL 2 DESBLOQUEADO!", fg="purple")

# --- INTERFAZ GRÁFICA (GUI) ---
# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Super Clicker 3000 :3")
ventana.geometry("300x250")  # Ancho x Alto

# Colores y fuentes bonitas
color_fondo = "#f0f0f0"  # Un gris clarito
fuente_grande = ("Arial", 16, "bold")
fuente_puntos = ("Courier New", 24, "bold")

# Configuramos el color de fondo de la ventana
ventana.config(bg=color_fondo)

# 2. Crear los elementos (Widgets)
etiqueta_titulo = tk.Label(ventana, text="Haz clic para ganar:", font=fuente_grande, bg=color_fondo, fg="#333")
etiqueta_titulo.pack(pady=20) # 'pady' es espacio arriba y abajo

etiqueta_puntos = tk.Label(ventana, text="¡Puntos: 0!", font=fuente_puntos, bg=color_fondo, fg="blue")
etiqueta_puntos.pack()

# Crear el botón y conectarlo a nuestra función con 'command='
boton_clic = tk.Button(ventana, text="¡CLIC AQUÍ!", font=("Arial", 12), command=incrementar_puntos, bg="green", fg="white", padx=10, pady=5)
boton_clic.pack(pady=30)

# 3. El ciclo principal: Mantiene la ventana abierta y escuchando clics
ventana.mainloop()