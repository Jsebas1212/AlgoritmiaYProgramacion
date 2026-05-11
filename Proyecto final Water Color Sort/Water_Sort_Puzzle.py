import tkinter as tk
from tkinter import messagebox
import random

# --- CONFIGURACIÓN DE DIFICULTADES ---
DIFICULTADES = {
    "Fácil": {"colores": 3, "vacios": 2},
    "Básico": {"colores": 5, "vacios": 2},
    "Normal": {"colores": 7, "vacios": 2},
    "Difícil": {"colores": 9, "vacios": 3},
    "Extremo": {"colores": 11, "vacios": 3},
    "Pesadilla": {"colores": 13, "vacios": 4},
    "Prueba": {"colores": 16, "vacios": 40}
}

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
        
        # --- CONFIGURACIÓN DE GAMEPLAY ---
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
        # Panel superior (Header)
        self.header = tk.Frame(self.root, bg="#161625", pady=10)
        self.header.pack(fill="x", side="top")
        
        tk.Label(self.header, text="NÚCLEO:", fg="#00FFFF", bg="#161625", font=("Courier", 12, "bold")).pack(side="left", padx=10)
        
        self.var_dif = tk.StringVar(value=self.dificultad_actual)
        menu_dif = tk.OptionMenu(self.header, self.var_dif, *DIFICULTADES.keys(), command=self.cambiar_dificultad)
        menu_dif.config(bg="#00FFFF", fg="black", font=("Courier", 10, "bold"), width=12)
        menu_dif.pack(side="left", padx=10)

        # Botón Reiniciar
        btn_reset = tk.Button(self.header, text="REINICIAR", command=self.iniciar_nivel, bg="#FF00FF", fg="white", font=("Courier", 10, "bold"), width=12)
        btn_reset.pack(side="right", padx=10)

        # Botón Deshacer
        self.btn_undo = tk.Button(self.header, text=f"DESHACER ({self.intentos_deshacer})", command=self.deshacer_movimiento, 
                                  bg="#FFD700", fg="black", font=("Courier", 10, "bold"), width=15)
        self.btn_undo.pack(side="right", padx=10)

        # Contenedor para Canvas y Scrollbar
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

    def cambiar_dificultad(self, seleccion):
        self.dificultad_actual = seleccion
        self.iniciar_nivel()

    def iniciar_nivel(self):
        conf = DIFICULTADES[self.dificultad_actual]
        colores_usar = PALETA_NEON[:conf["colores"]]
        
        pool = colores_usar * self.capacidad
        random.shuffle(pool)
        
        self.tubos_data = [pool[i:i + self.capacidad] for i in range(0, len(pool), self.capacidad)]
        for _ in range(conf["vacios"]):
            self.tubos_data.append([])
            
        self.historial = []
        self.intentos_deshacer = self.max_deshacer
        self.seleccionado = None
        self.actualizar_boton_undo()
        self.dibujar_escena()

    def registrar_estado(self):
        estado_copia = [list(tubo) for tubo in self.tubos_data]
        self.historial.append(estado_copia)
        if len(self.historial) > 50: self.historial.pop(0)

    def deshacer_movimiento(self):
        if self.historial and self.intentos_deshacer > 0:
            self.tubos_data = self.historial.pop()
            self.intentos_deshacer -= 1
            self.seleccionado = None
            self.actualizar_boton_undo()
            self.dibujar_escena()
        elif self.intentos_deshacer <= 0:
            messagebox.showwarning("ERROR DE SISTEMA", "No quedan cargas de retroceso temporal.")

    def actualizar_boton_undo(self):
        self.btn_undo.config(text=f"DESHACER ({self.intentos_deshacer})")
        if self.intentos_deshacer <= 0:
            self.btn_undo.config(state="disabled", bg="#333333", fg="#777777")
        else:
            self.btn_undo.config(state="normal", bg="#FFD700", fg="black")

    def dibujar_botella(self, x, y, ancho, alto, contenido, seleccionado):
        cuello_w, cuello_h = ancho * 0.4, alto * 0.2
        puntos = [
            x + (ancho-cuello_w)/2, y, x + (ancho+cuello_w)/2, y,
            x + (ancho+cuello_w)/2, y + cuello_h, x + ancho, y + cuello_h + 20,
            x + ancho, y + alto, x, y + alto, x, y + cuello_h + 20,
            x + (ancho-cuello_w)/2, y + cuello_h
        ]
        color_borde = "#FF00FF" if seleccionado else "#00FFFF"
        ancho_borde = 3 if seleccionado else 1

        cuerpo_alto = alto - cuello_h - 10
        for i, color in enumerate(contenido):
            bh = cuerpo_alto / self.capacidad
            by1 = (y + alto) - (i * bh)
            by0 = by1 - bh
            self.canvas.create_rectangle(x+4, by0, x+ancho-4, by1, fill=color, outline=color)

        self.canvas.create_polygon(puntos, outline=color_borde, fill="", width=ancho_borde)
        self.canvas.create_line(x+10, y+cuello_h+30, x+10, y+alto-20, fill="white", stipple="gray50")

    def dibujar_escena(self):
        self.canvas.delete("all")
        
        total_tubos = len(self.tubos_data)
        columnas = 8 if total_tubos > 15 else 7
        ancho_b, alto_b = 60, 180
        gap_x, gap_y = 50, 80
        margen_x, margen_y = 100, 50

        # 1. Dibujamos las botellas
        for i, contenido in enumerate(self.tubos_data):
            fila, col = i // columnas, i % columnas
            x = margen_x + col * (ancho_b + gap_x)
            y = margen_y + fila * (alto_b + gap_y)
            
            self.dibujar_botella(x, y, ancho_b, alto_b, contenido, self.seleccionado == i)
            
            tag = f"b_{i}"
            self.canvas.create_rectangle(x, y, x+ancho_b, y+alto_b, fill="", outline="", tags=tag)
            self.canvas.tag_bind(tag, "<Button-1>", lambda e, idx=i: self.clic_botella(idx))

        # 2. Ajuste inteligente del ScrollRegion
        self.canvas.update_idletasks()
        bbox = self.canvas.bbox("all")
        
        # Obtenemos el alto actual de la ventana (mínimo 850 si aún no carga)
        win_height = self.canvas.winfo_height()
        if win_height < 100: win_height = 850 

        if bbox:
            # El límite será el máximo entre el fondo de las botellas (+ margen) o el alto de la ventana
            limite_y = max(bbox[3] + 100, win_height)
            # El ancho será el máximo entre el ancho de las botellas o el ancho de la ventana
            limite_x = max(bbox[2] + 100, self.canvas.winfo_width())
            
            self.canvas.config(scrollregion=(0, 0, limite_x, limite_y))
        else:
            limite_y = win_height

        # 3. Dibujamos la rejilla de fondo ocupando todo el espacio calculado
        for i in range(0, 2000, 50): # Un poco más ancho por seguridad
            self.canvas.create_line(i, 0, i, limite_y, fill="#0f0f1a", tags="fondo")
        for i in range(0, limite_y + 50, 50):
            self.canvas.create_line(0, i, 2000, i, fill="#0f0f1a", tags="fondo")
        
        self.canvas.tag_lower("fondo")

    def clic_botella(self, idx):
        if self.seleccionado is None:
            if self.tubos_data[idx]:
                self.seleccionado = idx
        else:
            if self.seleccionado != idx:
                if self.puede_transferir(self.seleccionado, idx):
                    self.registrar_estado()
                    self.transferir(self.seleccionado, idx)
            self.seleccionado = None
        
        self.dibujar_escena()
        self.check_win()

    def puede_transferir(self, origen, destino):
        t_org, t_des = self.tubos_data[origen], self.tubos_data[destino]
        if not t_org or len(t_des) >= self.capacidad: return False
        if not t_des or t_des[-1] == t_org[-1]: return True
        return False

    def transferir(self, origen, destino):
        t_org, t_des = self.tubos_data[origen], self.tubos_data[destino]
        color = t_org[-1]
        while t_org and t_org[-1] == color and len(t_des) < self.capacidad:
            t_des.append(t_org.pop())

    def check_win(self):
        for t in self.tubos_data:
            if t and (len(t) != self.capacidad or len(set(t)) > 1):
                return
        messagebox.showinfo("MISIÓN CUMPLIDA", "¡Has estabilizado todos los núcleos de energía!")
        self.iniciar_nivel()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterSortFuturista(root)
    root.mainloop()