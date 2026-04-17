def suma(a, b):
    """
    Calcula la suma de dos números.
    
    Parámetros:
    a (float o int): El primer número
    b (float o int): El segundo número a sumar
    
    Retorna:
    float o int: El resultado de la adición
    """
    adición = a + b
    return adición

def resta(a, b):
    """
    Calcula la diferencia (resta) entre dos números.
    
    Parámetros:
    a (float o int): El número base (minuendo)
    b (float o int): El número a restar (sustraendo)
    
    Retorna:
    float o int: El resultado de la sustracción
    """
    sustración = a - b
    return sustración

def producto(a, b):
    """
    Calcula la multiplicación de dos números.
    
    Parámetros:
    a (float o int): El primer factor
    b (float o int): El segundo factor
    
    Retorna:
    float o int: El producto de la multiplicación
    """
    multiplicación = a * b
    return multiplicación

def división(a, b):
    """
    Calcula la división exacta entre dos números
    y maneja el error de división por cero.
    
    Parámetros:
    a (float o int): El dividendo (número a dividir)
    b (float o int): El divisor
    
    Retorna:
    float: El resultado de la división
    str: Un mensaje de advertencia si se intenta dividir entre cero
    """
    try:
        division = a / b
        return division
    except:
        return "⚠️  La división entre cero no está definida⚠️"

def raiz_cuadrada(a):
    """
    Calcula la raíz cuadrada de un número
    Para cumplir con los requisitos, utiliza la función
    producto() internamente.
    
    Parámetros:
    a (float o int): El número del cual se extraerá la raíz
    
    Retorna:
    float: La raíz cuadrada del número
    str: Un mensaje de advertencia si el número es negativo
    """
    if a < 0:
        return "⚠️  ERROR, Las raíces negativas no están definidas en el conjunto de los reales⚠️"
    else:
        raiz = producto(a, 1)**0.5
        return raiz

def exponente(a, b):
    """
    Calcula la potencia de un número elevado a otro.
    Para cumplir con los requisitos, utiliza la función
    producto() internamente.
    Maneja excepciones matemáticas como raíces negativas
    o divisiones por cero implícitas.
    
    Parámetros:
    a (float o int): La base
    b (float o int): El exponente
    
    Retorna:
    float o int: El resultado de elevar la base al exponente
    str: Un mensaje de advertencia si la operación matemática no está definida
    """
    if a < 0 and 0 < b < 1:
        return "⚠️  Las raíces de un número negativo no están definida en el conjunto de los reales⚠️"
    elif a == 0 and b < 0:
        return "⚠️  La división por cero no está definida⚠️"
    else:
        exponente = producto(a, 1) ** b
        return exponente

def factorial(a):
    """
    Calcula el factorial de un número utilizando recursividad.
    Asegura que el cálculo solo se realice en números enteros
    positivos o cero.
    
    Parámetros:
    a (int o float): El número del cual se calculará el factorial
    
    Retorna:
    int: El factorial del número
    str: Un mensaje de advertencia si el número es decimal o negativo
    """
    if a % 1 != 0:
        return "⚠️  El factorial solo está definido para números enteros⚠️"
    elif a == 0: 
        return 1
    elif a < 0:
        return "⚠️  El factorial no está definido para números negativos⚠️"
    else:
        return a*factorial(a-1)

def inversa(a):
    """
    Calcula el inverso multiplicativo de un número (1/a).
    Maneja el error matemático cuando el número es cero.
    
    Parámetros:
    a (float o int): El número al cual se le calculará la inversa
    
    Retorna:
    float: El resultado de 1 dividido por el número
    str: Un mensaje de advertencia si se intenta calcular la inversa de cero
    """
    if a == 0:
        return "⚠️  La división entre cero no está definida⚠️"
    else:
        inverso = producto(a, 1) ** -1
        return f"1/{a} lo que equivale a {inverso}"

print("\n___Calculadora___")
while True:
    primterm = input("\nIngrese valor a operar: ")
    if primterm.lower() in ["salir","s"]:
        print("Cerrando calculadora")
        break
    else:
        floprimterm = float(primterm)
        operación = input(
        f"""Escriba la operación a realizar:
        1. Suma           (+)
        2. Resta          (-)
        3. Multiplicacion (*)
        4. Division       (/)
        5. Raiz cuadrada  (√)
        6. Potencia      (^^)
        7. Factorial      (!)
        8. Inverso       (-1)
            {floprimterm} """)

        if operación.lower() in ["1","suma","+"]:

            sumaval2 = float(input(f"""\nEscriba valor del sumando
            {floprimterm} {operación} """))

            print(f"""\nEl resultado de la suma es:
            {floprimterm} {operación} {sumaval2} = {suma(floprimterm, sumaval2)}""")

        elif operación.lower() in ["2","resta","-"]:

            restaval2 = float(input(f"""\nEscriba valor del sustraendo
            {floprimterm} {operación} """))

            print(f"""\nEl resultado de la resta es:
            {floprimterm} {operación} {restaval2} = {resta(floprimterm, restaval2)}""")

        elif operación.lower() in ["3","multiplicacion","*"]:

            multival2 = float(input(f"""\nEscriba valor del multiplicador
            {floprimterm} {operación} """))

            print(f"""\nEl producto de la multiplicación es:
            {floprimterm} {operación} {multival2} = {producto(floprimterm, multival2)}""")

        elif operación.lower() in ["4","division","/"]:

            divisionval2 = float(input(f"""\nEscriba valor del divisor
            {floprimterm} {operación} """))

            print(f"""\nEl resultado de la división es:
            {floprimterm} {operación} {divisionval2} = {división(floprimterm, divisionval2)}""")

        elif operación.lower() in ["5","raiz cuadrada","√"]:

            print(f"""\nEl resultado de la raíz cuadrada de {floprimterm} es:
            √{floprimterm} = {raiz_cuadrada(floprimterm)}""")

        elif operación.lower() in ["6","potencia","^^"]:

            potenciaval2 = float(input(f"""\nEscriba valor del exponente
            {floprimterm} {operación} """))

            print(f"""\nEl resultado de {floprimterm} elevado a {potenciaval2} es:
            {floprimterm} ^ {potenciaval2} = {exponente(floprimterm, potenciaval2)}""")

        elif operación.lower() in ["7","factorial","!"]:

            print(f"""\nEl factorial de {floprimterm} es:
            {floprimterm}! = {factorial(floprimterm)}""")

        elif operación.lower() in ["8","inverso","-1"]:

            print(f"""\nEl inverso de {floprimterm} es:
            {floprimterm}⁻¹ = {inversa(floprimterm)}""")
        else:
            print("Por favor ingrese una opción válida")