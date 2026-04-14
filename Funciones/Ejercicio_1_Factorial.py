"""
Este código se creó con la finalidad de calcular el factorial
de un número entero no negativo

Pompt: Puedes generarme un código para una funcuón en Python que
calcule el factorial de un número entero no negativo

Johan Sebastian Echeverry Vega
c.c. 1113782839
Universidad Tecnológica de Pereira
Fecha: 2026-04-13
"""
def factorial(n):
    """
    Define la función factorial que recibe un número entero n y
    devuelve su factorial.

    Parámetros:
    n (int): Número entero al cuál se le calculará el factorial.

    Retorna:
    int o str: El factorial de n si es válido, o si es negativo
    un mensaje.
    """
    if n == 0: 
        return 1 #Por definición el factorial de 0 es igual a 1
    elif n < 0:
        return "⚠️  El factorial no está definido para números negativos⚠️"
    else:
        return n*factorial(n-1)

print("---Bienvenido al programa que te solucionará la vida si no sabes calcular un factorial---")
print("---Se que esas 10 lukas que pagaste por esto valdrán completamente la pena!!!---")
print("---Y si no pagaste, pues deja de ser tan degenerado, me costó mucho hacerlo hdtpm---") #Es solo humor!!! 

while True:
    calcfact = input("\nIngrese un número entero para calcular su factorial: ")
    if calcfact.lower() == "salir" or calcfact.lower() == "s":
        print("\nSaliendo del programa....")
        break
    try:
        numintfact = int(calcfact)
        if numintfact < 0:
            print(factorial(numintfact))
        elif numintfact >= 0:
            print(f"\nEl factorial de {calcfact} es: {factorial(numintfact)}")
    except ValueError:
        print("\nPor favor, ingrese un número entero válido o 'salir' para cerrar el programa.")