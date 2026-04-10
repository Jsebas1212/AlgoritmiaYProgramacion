def pro_lista(lista):
    if lista == []:
        return []
    else:
        numero = lista[0]
        if numero % 2 == 0:
            return [numero**2] + pro_lista(lista[1:])
        else:
            return pro_lista(lista[1:])
        
print("---Hola bienvenido---")
print("---Este programa te permite ingresar una lista de números enteros y te devolverá---")
print("---una lista con los números pares elevados al cuadrado---")
while True:
    opt=input("\nEscoja entre: Lista ya definida, lista personnalizada o salir? (D/P/S): ")
    
    if opt == "D" or opt == "d":
        ListDef = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        print("\nLista de números del 1 al 20: ")
        print(pro_lista(ListDef))

    elif opt == "P" or opt == "p":
        numtex = input("\nIngrese la lista de números separados por espacios: ")
        List1 = numtex.split()
        for o in range(len(List1)):
            List1[o] = int(List1[o])
        print("\nLos pares elevados al cuadrado de la lista ingresada son: ")
        print(sorted(pro_lista(List1)))

    elif opt == "S" or opt == "s"  :
        print("Saliendo...")
        break
    else:
        print("\nOpción no válida, por favor ingrese una opción válida.")