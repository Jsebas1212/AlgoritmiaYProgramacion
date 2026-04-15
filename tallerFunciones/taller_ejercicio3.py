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
        cantidad = diccionario[nombre]["cantidad"]
        precio = diccionario[nombre]["precio"]
        print(f"{nombre} : {cantidad} : por unidad ${precio}")



print("\nBienvenido al sistema de inventario")
print("¿Desea empezar con un inventario ya definido o desea crear uno desde cero? (D/C)")

while True:
    while True:
        pregunta0 = input("")
        if pregunta0.lower() == "d":
            inventario = {
                            "Manzana": {"cantidad": 50, "precio": 1200},
                            "Leche": {"cantidad": 20, "precio": 4500},
                            "Pan": {"cantidad": 15, "precio": 2500},
                            "Cafe": {"cantidad": 10, "precio": 15000},
                            "Huevos": {"cantidad": 30, "precio": 600}
                            }
            print("Su inventario de prueba es el siguiente: ")
            print(f"\n{mostrar_inventario(inventario)}")
            break
        elif pregunta0.lower() == "c" :
            inventario = {}
            break
        else:
            print("Por favor ingrese una opción válida")

    while True:
        print("\n¿Qué desea hacer? ")
        print("""
            Para agregar un producto nuevo al inventario escriba...."agregar"  o "A"
            Para eliminar un producto del inventario escriba........"eliminar" o "E"
            Para Calcular el valor total del inventario escriba....."calcular" o "C"
            Para ver el inventario escriba.........................."mostrar"  o "M"
            Para salir del programa escriba........................."salir"    o "S"
                    """)
        actionsinv = input("")
        if actionsinv.lower() in ["agregar","a"]:
            print("Escriba lo siguiente en ese orden separado por espacios")
            print("\nNombre del producto - cantidad de unidades del producto - precio del producto")
            agrlista = input("\n")
            datos = agrlista.split()
            nombre = datos[0]
            cantidad = int(datos[1])
            precio = float(datos[2])
            agregar_producto(inventario, nombre, cantidad, precio)

        #elif actionsinv.lower in ["eliminar","e"]:


        # elif actionsinv.lower in ["calcular","c"]:

        # elif actionsinv.lower in ["mostrar","m"]:
        
        # elif actionsinv.lower in ["salir","s"]: