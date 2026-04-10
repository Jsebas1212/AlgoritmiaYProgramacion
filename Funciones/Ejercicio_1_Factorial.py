def factorial(n):
    """
    Define la función factorial que recibe un número entero n y devuelve su factorial.
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

while True:
        numfact = input("Ingrese un número para calcular su factorial: ")
        if numfact.lower() == "apagar":
            print("Cerrando programa...")
            break
        elif numfact.isdigit():
            numfact_int = int(numfact)
            print(factorial(numfact_int))
        else:
            print("Ingrese un número válido o 'apagar' para salir.")