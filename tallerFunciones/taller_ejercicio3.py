def agregar_producto(diccionario, nombre, cantidad, precio):
    diccionario[nombre] = {"cantidad" : cantidad,
                           "precio" : precio}
    print(f"Se ha agregado {nombre} al inventario ✅")

def eliminar_producto(diccionario, nombre):
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"El producto '{nombre}' ha sido eliminado 🗑️")
    else:
        print(f"⚠️  Error: El producto '{nombre}' no se encuentra en el inventario.")

def calcular_valor_total(diccionario):
    total = 0
    for nombre in diccionario:
        cantidad = diccionario[nombre]["cantidad"]
        precio = diccionario[nombre]["precio"]
        total = total + (cantidad * precio)
    return total

def mostrar_inventario(diccionario):
    print("---Inventario actual---")
    for nombre in diccionario:
        cantidad = diccionario[nombre][cantidad]
        precio = diccionario[nombre][precio]
        print(f"{nombre} : {cantidad} : por unidad ${precio}")

