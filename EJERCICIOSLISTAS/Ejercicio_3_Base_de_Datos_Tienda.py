inventario = {"Manzanas" : 2.5 ,
              "Banana" : 1.8 ,
             "Naranja" : 3.0 ,
             "Pera" : 2.0 ,
             "Monster" : 5.0 ,
             "Agua" : 1.0 ,
             "CocaCola" : 3.5}
print("Para ver las opciones escribir 'ayuda'")
opciones = input("Bienvenido usuario, qué desea hacer? ") 
if opciones == "consultar producto" or opciones == "1" :
    selección = input("Ingrese nombre de producto: ")
    precio = inventario.get(selección)
    if selección in inventario :
        print("El producto '"+selección+"' se encuentra en existencia, precio del producto: $",precio)
    else:
        print("Producto no encontrado")
elif opciones == "agregar producto" or opciones == "2":
    producto_nuevo = input("Escriba el nombre del producto nuevo: ")
    precio_nuevo = float(input("Escriba su precio: "))
    inventario.update({producto_nuevo : precio_nuevo})
    print("Producto agregado con éxito!!!")
    preguntainv = input("¿Desea ver todo el inventario actualizado? (1), o ¿Desea ver solo el producto nuevo? (2): ")
    if preguntainv == "1" :
        print(inventario)
    elif preguntainv == "2" :
        print(producto_nuevo ,"$",precio_nuevo)
    else:
        print("Opción inválida")
elif opciones == "eliminar producto" or opciones == "3" :
    producto_elim = input("Escriba el nombre del producto a eliminar: ")
    if producto_elim in inventario :
        preguntainv2 = input("Está seguro de que quiere eliminar el producto '"+producto_elim+"'? Recierde que esta acción no se puede revertir ")
        if preguntainv2 == "continuar" or preguntainv2 == "si":
            precio_elim = inventario.pop(producto_elim)
            print("El producto '"+producto_elim+ "' ha sido eliminado correctamente del inventario")
            preguntainv1 = input("¿Desea ver todo el inventario actualizado? (1), o ¿Desea ver solo el producto eliminado? (2): ")
            if preguntainv1 == "1" :
                print(inventario)
            elif preguntainv1 == "2" :
                print("Producto eliminado:",producto_elim, "$", precio_elim)
        elif preguntainv2 == "cancelar" or preguntainv2 == "no":
            print("Acción cancelada")
    else:
        print("El producto indicado no se encuentra en el inventario")
elif opciones == "actualizar precio" or opciones == "4":
    mod_price = input("¿A qué producto le va a modificar su precio? ")
    if mod_price in inventario:
        new_price = float(input("Ingrese nuevo valor para el producto '"+mod_price+"': "))
        inventario.update({mod_price: new_price})
        print("Precio actualizado con éxito!!!")
        preguntainv3 = input("¿Desea ver todo el inventario actualizado? (1), o ¿Desea ver solo el producto con su precio actualizado? (2): ")
        if preguntainv3 == "1" :
            print(inventario)
        elif preguntainv3 == "2" :
            print(mod_price, "$", new_price)
    else:
        print("El producto indicado no se encuentra en el inventario")
elif opciones == "ayuda":
    print("Las opciones disponibles son las siguientes:")
    print("Para consultar precio de algún producto escribir 'consultar producto' o '1'")
    print("Para agregar algún producto nuevo escribir 'agregar producto' o '2'")
    print("Para eliminar algún producto del inventario escribir 'eliminar producto' o '3'")
    print("Para actualizar el precio de algún producto del inventario escribir 'actualizar precio' o '4'")
elif opciones == "nada" or opciones == "20":
    print("Ah bueno, chingue sumadre entonces")
elif opciones == "que le importa sapo" or opciones == "07" or opciones == "sapo":
    print("Su madre bobo")
elif opciones == "no se" or opciones == "no estoy seguro" or opciones == "que puedo hacer":
    print("Recuerde que puede obtener más información acerca de las opciones de este código escribiendo 'ayuda' al ejecutarlo")
else:
    print("Opción inválida, por favor escriba una opción válida")

#perdón si le metí muchas vainas, es que me emocioné y quise hacerlo bastante completo
#y con unos pequeños easter eggs de paso :3