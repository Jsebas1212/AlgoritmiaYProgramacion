"""
Este código se creó para escoger de una lista, ya sea
definida o creada por el usuario, los números enteros
pares de la misma y mostrar el resultado de esos 
números pares elevados al cuadrado.

prompt: Puedes explicarme y generarme como crear una
función en python para que, de una lista solo tome los
números pares y los eleve al cuadrado.

Johan Sebastian Echeverry Vega
c.c. 1113782839
Universidad Tecnológica de Pereira
Fecha: 2026/04/13
"""
def pro_lista(lista):
    """
    Esta función lo que haces es recorrer una lista y
    cada vez que encuentre un número par lo eleva al
    cuadrado y lo guarda.

    Parámetros:
    lista (list): Lista de números enteros.

    Retorna:
    list: una nueva lista que contiene a los números pares de
    la original pero elevados al cuadrado.
    """
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
print("---una lista con los números pares elevados al cuadrado---") #Hasta ahora mi mensaje de bienvenida más normal
while True:
    opt = input("\nEscoja entre: Lista ya definida, lista personnalizada o salir? (D/P/S): ")
    if opt.lower() == "d" :
        ListDef = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        print("\nLista de números del 1 al 20: ")
        print("\nLista original:")
        print(ListDef)
        print("\nLista solo con pares elevados al cuadrado:")
        print(pro_lista(ListDef))
    elif opt.lower() == "p" :
        numtex = input("\nIngrese la lista de números separados por espacios: ")
        try:
            List1 = numtex.split() #".split" sirve para dividir un string (texto) en una lista separada por espacios, pero siendo aún texto.
            for o in range(len(List1)): #"len" sirve para saber cuantos elementos tiene algo, en este caso la lista. Sirve para que el código cuente la cantidad de elementos que ingresó el usuario en su lista personalizada y defina el rango en "for" de forma automática.
                List1[o] = int(List1[o])
            list10 = pro_lista(List1)
            print("\nLos pares elevados al cuadrado de la lista ingresada son: ")
            print(list10)
            if len(list10) >= 2 and list10 != sorted(list10): #Tambien es un capricho para que no salga la opción si no es necesario. Lo que hace el "!= sorted(list10)" Es básicamente revisar si es diferente a la lista organizada, osea, primero la organiza con el "sorted" y después la compara.
                ordenlist = input("\n¿Desea ordenar los elementos de su lista de menor a mayor?: (S/N) ").lower() #A ultimo momento aprendí que podía poner ".lower" al final del input para ahorrarme trabajo (Tambien es mas práctico).
                if ordenlist == "s" :
                    print(sorted(list10)) #"sorted" sirve para organizar los elementos de la lista de menor a mayor (tambien funciona con texto de a-z). Toda esta parte de organizar la lista de menor a mayor fue solo capricho mío jajaja.
                elif ordenlist == "n" :
                    print("Ok...")
        except:
            print("Algún dato de la lista no es un número entero, por favor verifique su error")
    elif opt.lower() == "s" :
        print("Saliendo...")
        break
    else:
        print("\nOpción no válida, por favor ingrese una opción válida.")