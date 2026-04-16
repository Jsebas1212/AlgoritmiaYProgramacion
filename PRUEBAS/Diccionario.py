import json

# =====================
# CLASE INVENTARIO
# =====================
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad, precio):
        nombre = nombre.lower()
        if cantidad < 0 or precio < 0:
            print("⚠️ Valores inválidos")
            return

        if nombre in self.productos:
            print("⚠️ Producto ya existe, se actualizará")

        self.productos[nombre] = {
            "cantidad": cantidad,
            "precio": precio
        }
        print(f"✅ Producto '{nombre}' guardado")

    def eliminar(self, nombre):
        nombre = nombre.lower()
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"🗑️ '{nombre}' eliminado")
        else:
            print("⚠️ Producto no encontrado")

    def mostrar(self):
        if not self.productos:
            print("📦 Inventario vacío")
            return

        print("\n--- INVENTARIO ---")
        for nombre, datos in self.productos.items():
            print(f"{nombre} | Cantidad: {datos['cantidad']} | Precio: ${datos['precio']}")

    def total(self):
        total = sum(d["cantidad"] * d["precio"] for d in self.productos.values())
        print(f"💰 Total inventario: ${total}")

    def guardar(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump(self.productos, f)
        print("💾 Inventario guardado")

    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                self.productos = json.load(f)
            print("📂 Inventario cargado")
        except FileNotFoundError:
            print("⚠️ No existe archivo guardado")


# =====================
# FUNCIONES AUXILIARES
# =====================

def pedir_numero(tipo):
    while True:
        try:
            return float(input(f"Ingrese {tipo}: "))
        except ValueError:
            print("⚠️ Debe ingresar un número válido")


# =====================
# PROGRAMA PRINCIPAL
# =====================
inv = Inventario()

while True:
    print("""
    ===== MENÚ =====
    1. Agregar producto
    2. Eliminar producto
    3. Mostrar inventario
    4. Calcular total
    5. Guardar inventario
    6. Cargar inventario
    7. Salir
    """)

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        cantidad = pedir_numero("cantidad")
        precio = pedir_numero("precio")
        inv.agregar(nombre, cantidad, precio)

    elif opcion == "2":
        nombre = input("Nombre a eliminar: ")
        inv.eliminar(nombre)

    elif opcion == "3":
        inv.mostrar()

    elif opcion == "4":
        inv.total()

    elif opcion == "5":
        inv.guardar()

    elif opcion == "6":
        inv.cargar()

    elif opcion == "7":
        print("👋 Saliendo...")
        break

    else:
        print("⚠️ Opción inválida")
