def agregar_producto(diccionario, nombre, cantidad, precio):
    diccionario[nombre] = {"cantidad" : cantidad,
                           "precio" : precio}
    print(f"Se ha agregado '{nombre}' al inventario ✅")

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
    pregunta0 = input("")
    if pregunta0.lower() == "d":
        inventario = {
                        "Manzana": {"cantidad": 50, "precio": 1200},
                        "Leche": {"cantidad": 20, "precio": 4500},
                        "Pan": {"cantidad": 15, "precio": 2500},
                        "Cafe": {"cantidad": 10, "precio": 15000},
                        "Huevos": {"cantidad": 30, "precio": 600}
                        }
        print("\nSu inventario de prueba es el siguiente: ")
        print("")
        mostrar_inventario(inventario)
        input("\nPresiona 'enter' para continuar")
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
        while True:
            print("\nIngrese los siguientes datos del nuevo producto:")
            try:
                nombrenpro = input("\nNombre del producto: ").capitalize()
                cantidadnpro = int(input("Cantidad del producto: "))
                precionpro = float(input("Precio del producto: "))
                agregar_producto(inventario, nombrenpro, cantidadnpro, precionpro)
                break
            except:
                print("\n⚠️  Error, la cantidad y el precio deben ser números, vuelva a intentarlo")

    elif actionsinv.lower() in ["eliminar","e"]:
        print("\nIngrese el nombre del producto que quiere eliminar del inventario")
        elimpro = input("").capitalize()
        print("")
        eliminar_producto(inventario, elimpro)

    elif actionsinv.lower() in ["calcular","c"]:
        print(f"\nEl valor total de su inventario es de: ${calcular_valor_total(inventario)}")
        input("\nPresiona 'enter' para volver atrás")

    elif actionsinv.lower() in ["mostrar","m"]:
        print("")
        mostrar_inventario(inventario)
        input("\nPresiona 'enter' para volver atrás")
    
    elif actionsinv.lower() in ["salir","s"]:
        print("\n¿Seguro que desea salir?")
        print("¡La base de datos de su inventario se borrará!")
        advertencia = input("(s/n) ")
        if advertencia.lower() in ["si","s"]:
            break
        elif advertencia.lower() in ["no","n"]:
            print("Acción cancelada")
    else:
            print("\nOpción inválida, por favor ingrese una opción válida")