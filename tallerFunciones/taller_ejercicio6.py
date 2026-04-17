def mostrar_productos(diccionario):
    for nombre, precio in diccionario.items():
        print(f"|{nombre}| : Precio del producto ${precio}")

def verificar_dinero(precio, saldo_total):
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
    
    producto_elegido = input("\n¿Qué producto elige? ").capitalize()

    if producto_elegido in productos:
        precio_producto = productos[producto_elegido]
        print(f"\nProducto elegido : {producto_elegido}")
        print(f"Total a pagar:     ${precio_producto}")
        
        saldo = 0
        
        while saldo < precio_producto:
            try:
                pago_usuario = float(input("\nIngrese la cantidad de dinero con la que va a pagar: $"))
                saldo = pago_usuario + saldo
            except ValueError:
                print("\nPor favor ingrese el valor numérico de la cantidad de dinero con la que va a pagar.")
                continue

            if verificar_dinero(precio_producto, saldo) == True:

                devuelta = saldo - precio_producto
            
                if devuelta > 0:
                    print(f"\n¡Compra exitosa! Entregando {producto_elegido}...")
                    print(f"\nTu devuelta es: ${devuelta} \nPor favor retírela")
                    print("\nQue tenga un buen día usuario")
                    input("\n\nVolviendo al menú de opciones")


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