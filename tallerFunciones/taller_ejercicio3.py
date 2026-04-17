def agregar_producto(diccionario, nombre, cantidad, precio):
    """
    Agrega un nuevo producto al inventario o actualiza uno existente
    tomando en cuenta que las cantidades y el precio no puede ser negativo.
    
    Parámetros:
    diccionario (dict): El diccionario que almacena el inventario
    nombre (str): El nombre del producto
    cantidad (int): La cantidad de unidades disponibles
    precio (float o int): El valor monetario por unidad del producto
    
    Retorna:
    Ninguno. Modifica el diccionario original y muestra un mensaje de confirmación
    """
    if cantidad < 0 or precio < 0:
        print("\nError, la cantidad y el precio no pueden ser negativos")
        print(f"\nEl producto '{nombre}' no fué agregado correctamente.")
    else:
        diccionario[nombre] = {"cantidad" : cantidad,
                            "precio" : precio}
        print(f"Se ha agregado '{nombre}' al inventario ✅")

def eliminar_producto(diccionario, nombre):
    """
    Elimina un producto específico del inventario, verificando primero si existe.
    
    Parámetros:
    diccionario (dict): El diccionario que almacena el inventario
    nombre (str): El nombre del producto a eliminar
    
    Retorna:
    Ninguno. Modifica el diccionario original y muestra un mensaje de éxito o de advertencia
    """
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"\nEl producto '{nombre}' ha sido eliminado 🗑️")
    else:
        print(f"\n⚠️  Error: El producto '{nombre}' no se encuentra en el inventario.")

def calcular_valor_total(diccionario):
    """
    Calcula el valor monetario total del inventario. 
    Multiplica la cantidad de cada producto por su precio y suma todos los resultados.
    
    Parámetros:
    diccionario (dict): El diccionario que almacena el inventario
    
    Retorna:
    float o int: El valor total acumulado de todos los productos
    """
    total = 0
    for nombre in diccionario:
        cantidad = diccionario[nombre]["cantidad"]
        precio = diccionario[nombre]["precio"]
        total = total + (cantidad * precio)
    return total

def mostrar_inventario(diccionario):
    """
    Recorre el inventario actual y muestra en pantalla cada producto 
    con su respectiva cantidad y precio por unidad de forma ordenada.
    
    Parámetros:
    diccionario (dict): El diccionario que almacena el inventario
    
    Retorna:
    Ninguno. Imprime la información clara y ordenada en la consola.
    """
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
