def suma(a, b):
    adición = a + b
    return adición

def resta(a, b):
    sustración = a - b
    return sustración

def producto(a, b):
    multiplicación = a * b
    return multiplicación

def división(a, b):
    try:
        division = a / b
        return division
    except:
        return "La división entre cero no está definida"

def raiz_cuadrada(a):
    if a < 0:
        return "ERROR, Las raíces negativas no están definidas en el conjunto de los reales."
    else:
        raiz = producto(a, 1)**0.5
        return raiz

def exponente(a, b):
    exponente = producto(a, 1) ** b
    return exponente

def factorial(a):
    if a == 0: 
        return 1
    elif a < 0:
        return "⚠️  El factorial no está definido para números negativos⚠️"
    else:
        return a*factorial(a-1)

def inversa(a):
    if a == 0:
        return "La división entre cero no está definida."
    else:
        inverso = producto(a, 1) ** -1
        return f"1/{a} lo que equivale a {inverso}"


a = float(input("Numero: "))
#b = float(input("Potencia: "))
print(f"El inverso de {a} es: {inversa(a)}")

