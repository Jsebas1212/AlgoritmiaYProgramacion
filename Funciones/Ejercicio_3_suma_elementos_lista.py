"""
Este código lo que hace es tomar cada uno de los elementos de
una lista ingresada por el usuario e imprimir el resultado de
esos elementos.

prompt: Generame una función en python donde yo le de una lista
de números y me devuelva la suma de todos sus elementos y explicame
como funciona esa función valga la redundancia.

Johan Sebastian Echeverry Vega
c.c. 1113782839
Universidad Tecnológica de Pereira
Fecha: 2026/04/13
"""
def sumalist(lista):
    """ 
    Devuelve los elementos de una lista y los va sumando

    Parámetros:
    lista (list): Lista de números reales

    Retorna:
    float: La suma de los elementos de la lista ingresada
    """
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumalist(lista[1:])

print("---Hey muy buenas a todos, wapisimos!!!---")
print("---Aquí Vegetta 777 en un nuevo directo de Planeta Vegetta!!!---")
print("---Ok no---")
while True:
    option = input("\nPresiona enter para continuar o escribe 'salir' para cerrar el progranma: ")
    if option == "":
        while True:
            numlist = input("\nEscribe una lista de números, ¡OJO! separados por espacios: ").lower()
            if numlist == "salir" or numlist == "s":
                print("Saliendo...")
                exit()
            else:
                List1 = numlist.split()
                try: 
                    for o in range(len(List1)):
                        List1[o] = float(List1[o])
                    print("\nLa suma de los elementos de la lista ingresada es: ", sumalist(List1))
                except ValueError:
                    print("\nPinche bruto, ¿no ves que solo puedes ingresar números? Intenta de nuevo ingeniero industrial.")
    elif option.lower() == "salir" or option.lower()== "s":
        print("Saliendo del programa...")
        break
    else:
        print("\nNo te quieras pasar de listo conmigo muchacho")
        print("Ingresa una opción válida por favor, ois?")