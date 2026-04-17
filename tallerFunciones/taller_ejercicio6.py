productos = {
    "Doritos": 4000,
    "Monster": 7000,
    "Agua": 2000,
    "Cheetos": 3500,
    "Oreo": 3000
            }

def mostrar_productos(diccionario):
    for nombre, precio in diccionario.items():
        print(f"|{nombre}| : Precio del producto ${precio}")

def verificar_dinero(precio, pago):
    if pago < precio:
        faltante = precio - pago
        print(f"El dinero no es suficiente. Te faltan ${faltante}.")
        return False
    else:
        return True 


print("\n¡Bienvenido a la máquina dispensadora!\n")
print("Seleccione el producto que desee:")
mostrar_productos(productos)

producto_elegido = input("\n¿Qué producto elige? ").capitalize()

if producto_elegido in productos:
    precio_producto = productos[producto_elegido]
    print(f"\nProducto elegido : {producto_elegido}")
    print(f"Total a pagar:     ${precio_producto}")
    
    pago_usuario = int(input("\nIngrese la cantidad de dinero con la que va a pagar: $"))
    
    if verificar_dinero(precio_producto, pago_usuario):
        
        devuelta = pago_usuario - precio_producto
        
        if devuelta > 0:
            print(f"\n¡Compra exitosa! Entregando {producto_elegido}...")
            print(f"Tu devuelta es: ${devuelta}")
        else:
            print(f"\n¡Compra exitosa! Entregando {producto_elegido}...")
            print("Pagaste exacto, no hay devuelta.")

else:
    print("\nProducto no válido. Por favor reinicie la máquina.")