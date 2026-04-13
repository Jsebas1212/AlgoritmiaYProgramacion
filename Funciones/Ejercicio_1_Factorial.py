def factorial(n):
    """
    Define la función factorial que recibe un número entero n y devuelve su factorial.
    """
    if n == 0:
        return 1
    elif n < 0:
        return "El factorial no está definido para números negativos."
    else:
        return n*factorial(n-1)


print("ESPERA, MINIATURA MINIATURA")
print("PERO QUE MINIATURA DICES TIO")

while True:
    calcfact = input("Ingrese un número entero para calcular su factorial: ")
    if calcfact.isdigit() >= 0:
        try:
            calcfactint = int(calcfact)
            print(factorial(calcfactint))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
        try:
            if calcfact.lower() == "salir" or calcfact.lower() == "s":
                print("Saliendo del programa.")
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

