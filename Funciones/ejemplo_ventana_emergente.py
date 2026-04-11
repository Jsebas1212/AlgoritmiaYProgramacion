import tkinter
from tkinter import messagebox

# Esto es necesario para "esconder" una ventana principal vacía que tkinter crea por defecto.
tkinter.Tk().withdraw()

# Esta es la línea mágica que crea la ventana emergente de información.
messagebox.showinfo("Aviso de homosexualidad", "Hola, usted es 100% homosexual ¡Felicidades!")