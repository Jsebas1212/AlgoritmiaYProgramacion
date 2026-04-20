def mostrar_productos(diccionario):
    """
    Recorre el diccionario de productos y los muestra en la consola 
    de forma ordenada, indicando el nombre y su respectivo precio.
    
    Parámetros:
    diccionario (dict): Un diccionario que contiene los productos disponibles 
                        como llaves y sus precios como valores.
    
    Retorna:
    Ninguno. Imprime la lista de productos formateada en pantalla
    """
    for nombre, precio in diccionario.items(): #.items() lo que hace es como decirle a python que saque las llaves (nombre) y los valores (precio) juntos y que los guarde en cada una de las variables que se definen en for.
        print(f"|{nombre}| : Precio del producto ${precio}")

def verificar_dinero(precio, saldo_total):
    """
    Evalúa si el dinero ingresado por el usuario es suficiente para pagar el producto.
    Si el dinero no alcanza, calcula la diferencia y le informa al usuario cuánto falta.
    
    Parámetros:
    precio (float o int): El costo total del producto a comprar
    saldo_total (float o int): La cantidad de dinero que el usuario ha ingresado
    
    Retorna:
    bool: True si el saldo es igual o mayor al precio (la compra se puede realizar)
          False si el saldo es menor al precio (falta dinero)
    """
    if saldo_total < precio:
        faltante = precio - saldo_total
        print(f"\nEl dinero no es suficiente. Te faltan ${faltante}\n")
        return False
    else:
        return True 
    
productos = {
    "Doritos": 4000,
    "Monster": 7000,
    "Agua": 2000,
    "Cheetos": 3500,
    "Oreo": 3000
            }

print("\n¡HOLA¡ Bienvenido a la máquina dispensadora!\n")

while True:
    print("\nSeleccione el producto que desee:")
    mostrar_productos(productos)
    
    producto_elegido = input("\n¿Qué producto elige? ").capitalize() #.capitalice() sirve como para mantener un estandar en la forma en la que python recibe el texto ingresado. Sin importar que el usurio escriba "monster","MONSTER" o "MoNsTer" el .capitalice siempre lo va a tranformar en "Monster", es decir, la primera letra mayuscula y la segunda minuscula, siempre así.

    if producto_elegido in productos:
        precio_producto = productos[producto_elegido]
        print(f"\nProducto elegido : {producto_elegido}")
        print(f"Total a pagar:     ${precio_producto}")
        
        saldo = 0
        
        while saldo < precio_producto:
            try:
                pago_usuario = float(input("\nIngrese la cantidad de dinero con la que va a pagar: $"))
                if pago_usuario >= 0:
                    saldo = pago_usuario + saldo
                else:
                    print("\nNo se aceptan valores negativos, ingrese solo valores positivos.")
                    continue
            except ValueError:
                print("\nPor favor ingrese el valor numérico de la cantidad de dinero con la que va a pagar.")
                continue

            if verificar_dinero(precio_producto, saldo) == True:

                devuelta = saldo - precio_producto
            
                if devuelta > 0:
                    print(f"\n¡Compra exitosa! Entregando {producto_elegido}...")
                    print(f"\nTu devuelta es: ${devuelta} \nPor favor retírela")
                    print("\nQue tenga un buen día usuario")
                    input("\n\nPresiona 'enter' para volver al menú de opciones")


                else:
                    print(f"\n¡Compra exitosa! Entregando {producto_elegido}...")
                    print("\nPagaste exacto, no hay devuelta.\n")
                    print("\nQue tenga un buen día usuario")
                    input("\n\nPresiona 'enter' para volver al menú de opciones")
                    
    elif producto_elegido in ["Apagar","Salir","S","A"]:
        print("\nApagando máquina dispensadora...")
        break
    else:
        print("\nProducto no válido. Por favor digite correctamente el nombre del producto que desea.\n")