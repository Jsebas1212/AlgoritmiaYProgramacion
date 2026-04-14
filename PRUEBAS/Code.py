opt = input("\nEscoja entre: Lista ya definida, lista personnalizada o salir? (D/P/S): ")
if opt.lower() == "p" :
        numtex = input("\nIngrese la lista de números separados por espacios: ")
        List1 = numtex.split() #.split sirve para dividir un string (texto) en una lista separada por espacios, pero siendo aún texto.
        print(List1)