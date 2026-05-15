import tkinter as tk
from tkinter import messagebox
import random
# Importamos la librería Pillow para poder leer el archivo .jpg
from PIL import Image, ImageTk 

# Diccionario con las reglas de cada nivel
DIFICULTADES = {
    "Fácil": {"colores": 3, "vacios": 2},
    "Básico": {"colores": 5, "vacios": 2},
    "Normal": {"colores": 7, "vacios": 2},
    "Difícil": {"colores": 9, "vacios": 3},
    "Extremo": {"colores": 11, "vacios": 3},
    "Pesadilla": {"colores": 13, "vacios": 4},
    "Prueba": {"colores": 16, "vacios": 40}
}

# Lista de colores en formato Hexadecimal
PALETA_NEON = [
    "#FF00FF", "#00FFFF", "#FFD700", "#FF4500", "#7FFF00", 
    "#1E90FF", "#FF1493", "#ADFF2F", "#FF8C00", "#00FA9A",
    "#8A2BE2", "#F0E68C", "#FF6347", "#E0E0E0", "#4B0082",
    "#000000"
]

class WaterSortFuturista:
    
    def __init__(self, root):
        self.root = root
        self.root.title("NÚCLEO DE ENERGÍA")
        self.root.geometry("1200x850")
        self.root.configure(bg="#0a0a12") 
        
        # --- CARGAR LA IMAGEN DE FONDO ---
        self.fondo_img = None
        try:
            ruta_imagen = r"C:\Users\che1u\Documents\Algoritmia y Programación\Proyecto final Water Color Sort\vangoh.jpg"
            imagen_original = Image.open(ruta_imagen)
            imagen_redimensionada = imagen_original.resize((1200, 850))
            self.fondo_img = ImageTk.PhotoImage(imagen_redimensionada)
        except Exception as e:
            print(f"Nota: No se pudo cargar la imagen. Error: {e}")
        
        self.max_deshacer = 9999
        self.intentos_deshacer = self.max_deshacer
        self.dificultad_actual = "Normal"
        self.tubos_data = [] 
        self.historial = []  
        self.seleccionado = None 
        self.capacidad = 4 
        
        self.setup_ui()
        self.iniciar_nivel()

    def setup_ui(self):
        self.header = tk.Frame(self.root, bg="#161625", pady=10)
        self.header.pack(fill="x", side="top")
        
        tk.Label(self.header, text="NÚCLEO:", fg="#00FFFF", bg="#161625", font=("Courier", 12, "bold")).pack(side="left", padx=10)
        
        self.var_dif = tk.StringVar(value=self.dificultad_actual)
        menu_dif = tk.OptionMenu(self.header, self.var_dif, *DIFICULTADES.keys(), command=self.cambiar_dificultad)
        menu_dif.config(bg="#00FFFF", fg="black", font=("Courier", 10, "bold"), width=12)
        menu_dif.pack(side="left", padx=10)

        btn_reset = tk.Button(self.header, text="REINICIAR", command=self.iniciar_nivel, bg="#FF00FF", fg="white")
        btn_reset.pack(side="right", padx=10)

        self.btn_undo = tk.Button(self.header, text=f"DESHACER ({self.intentos_deshacer})", command=self.deshacer_movimiento, bg="#FFD700", fg="black")
        self.btn_undo.pack(side="right", padx=10)

        container = tk.Frame(self.root, bg="#0a0a12")
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg="#0a0a12", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def iniciar_nivel(self):
        conf = DIFICULTADES[self.dificultad_actual]
        cantidad_colores = conf["colores"]
        cantidad_vacios = conf["vacios"]
        
        colores_usar = PALETA_NEON[0:cantidad_colores]
        
        pool_colores = colores_usar * self.capacidad
        random.shuffle(pool_colores) 
        
        self.tubos_data = []
        
        posicion = 0
        while posicion < len(pool_colores):
            un_tubo = pool_colores[posicion : posicion + self.capacidad]
            self.tubos_data.append(un_tubo)
            posicion = posicion + self.capacidad
            
        for _ in range(cantidad_vacios):
            tubo_vacio = []
            self.tubos_data.append(tubo_vacio)
            
        self.historial = []
        self.intentos_deshacer = self.max_deshacer
        self.seleccionado = None
        self.actualizar_boton_undo()
        self.dibujar_escena()

    def registrar_estado(self):
        estado_copia = []
        for tubo in self.tubos_data:
            estado_copia.append(list(tubo)) 
        self.historial.append(estado_copia)

    def cambiar_dificultad(self, seleccion):
        self.dificultad_actual = seleccion
        self.iniciar_nivel()

    def deshacer_movimiento(self):
        if len(self.historial) > 0 and self.intentos_deshacer > 0:
            self.tubos_data = self.historial.pop()
            self.intentos_deshacer -= 1
            self.seleccionado = None
            self.actualizar_boton_undo()
            self.dibujar_escena()
        else:
            messagebox.showwarning("ERROR", "No puedes deshacer más.")

    def actualizar_boton_undo(self):
        self.btn_undo.config(text=f"DESHACER ({self.intentos_deshacer})")

    # --- FUNCIÓN DE DIBUJO LIMPIA Y EXACTA A LA IMAGEN ---
    def dibujar_tubo(self, x, y, ancho, alto, contenido, seleccionado):
        radio = ancho / 2
        
        # Grosor y color dependiendo de si está seleccionado
        if seleccionado:
            color_borde = "#FF00FF"
            ancho_borde = 4
        else:
            color_borde = "#000000"
            ancho_borde = 2

        alto_liquido = alto / self.capacidad

        # 1. Dibujar los líquidos primero para que queden por debajo del borde
        for i in range(len(contenido)):
            color = contenido[i]
            y_abajo = (y + alto) - (i * alto_liquido)
            y_arriba = y_abajo - alto_liquido

            if i == 0:
                # Líquido del fondo: Parte curva (Arco)
                self.canvas.create_arc(
                    x, y + alto - ancho, 
                    x + ancho, y + alto, 
                    start=180, extent=180, style=tk.CHORD, 
                    fill=color, outline=color
                )
                # Líquido del fondo: Parte recta arriba de la curva
                if alto_liquido > radio:
                    self.canvas.create_rectangle(
                        x, y_arriba, 
                        x + ancho, y + alto - radio, 
                        fill=color, outline=color
                    )
            else:
                # Líquidos de más arriba (Rectángulos simples)
                self.canvas.create_rectangle(
                    x, y_arriba, 
                    x + ancho, y_abajo, 
                    fill=color, outline=color
                )

        # 2. Dibujar el contorno limpio del tubo de ensayo
        # Pared izquierda
        self.canvas.create_line(x, y, x, y + alto - radio, fill=color_borde, width=ancho_borde)
        # Pared derecha
        self.canvas.create_line(x + ancho, y, x + ancho, y + alto - radio, fill=color_borde, width=ancho_borde)
        # Curva inferior (U)
        self.canvas.create_arc(
            x, y + alto - ancho, 
            x + ancho, y + alto, 
            start=180, extent=180, style=tk.ARC, 
            outline=color_borde, width=ancho_borde
        )
        
        # 3. Dibujar el labio superior (simple y limpio)
        sobresale = 5
        self.canvas.create_line(x - sobresale, y, x + ancho + sobresale, y, fill=color_borde, width=ancho_borde)

    def dibujar_escena(self):
        self.canvas.delete("all") 
        
        if self.fondo_img is not None:
            self.canvas.create_image(0, 0, image=self.fondo_img, anchor="nw", tags="fondo")
        
        total_tubos = len(self.tubos_data)
        columnas = 7
        if total_tubos > 15:
            columnas = 8
            
        ancho_b = 60
        alto_b = 200 # Un poco más altos para que parezcan tubos
        
        margen_x = 120 
        margen_y = 100 
        gap_x = 60      
        gap_y = 100     

        for i in range(len(self.tubos_data)):
            contenido = self.tubos_data[i]
            fila = i // columnas
            columna = i % columnas
            
            x = margen_x + columna * (ancho_b + gap_x)
            y = margen_y + fila * (alto_b + gap_y)
            
            es_seleccionado = False
            if self.seleccionado == i:
                es_seleccionado = True
                
            self.dibujar_tubo(x, y, ancho_b, alto_b, contenido, es_seleccionado)
            
            tag_tubo = f"t_{i}"
            self.canvas.create_rectangle(x, y, x+ancho_b, y+alto_b, fill="", outline="", tags=tag_tubo)
            self.canvas.tag_bind(tag_tubo, "<Button-1>", lambda event, numero=i: self.clic_tubo(numero))

        self.canvas.update_idletasks()
        limites_dibujo = self.canvas.bbox("all") 
        
        if limites_dibujo is not None:
            alto_total_necesario = limites_dibujo[3] + 100 
            self.canvas.config(scrollregion=(0, 0, 1200, alto_total_necesario))

    def clic_tubo(self, indice_clic):
        if self.seleccionado is None:
            if len(self.tubos_data[indice_clic]) > 0:
                self.seleccionado = indice_clic
        else:
            if self.seleccionado != indice_clic:
                if self.puede_transferir(self.seleccionado, indice_clic):
                    self.registrar_estado()
                    self.transferir(self.seleccionado, indice_clic)
            self.seleccionado = None
        
        self.dibujar_escena()
        self.check_win()

    def puede_transferir(self, origen, destino):
        tubo_origen = self.tubos_data[origen]
        tubo_destino = self.tubos_data[destino]
        
        if len(tubo_origen) == 0:
            return False
        if len(tubo_destino) >= self.capacidad:
            return False
            
        if len(tubo_destino) == 0:
            return True
            
        color_arriba_origen = tubo_origen[-1]
        color_arriba_destino = tubo_destino[-1]
        
        if color_arriba_destino == color_arriba_origen:
            return True
            
        return False

    def transferir(self, origen, destino):
        tubo_origen = self.tubos_data[origen]
        tubo_destino = self.tubos_data[destino]
        color_a_mover = tubo_origen[-1]
        
        while len(tubo_origen) > 0:
            if tubo_origen[-1] == color_a_mover and len(tubo_destino) < self.capacidad:
                color_sacado = tubo_origen.pop() 
                tubo_destino.append(color_sacado) 
            else:
                break 

    def check_win(self):
        for tubo in self.tubos_data:
            if len(tubo) > 0: 
                if len(tubo) != self.capacidad: 
                    return 
                
                primer_color = tubo[0]
                for color in tubo:
                    if color != primer_color:
                        return 
                        
        messagebox.showinfo("¡GANASTE!", "Todos los colores están ordenados.")
        self.iniciar_nivel()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterSortFuturista(root)
    root.mainloop()