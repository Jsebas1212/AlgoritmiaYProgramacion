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
        return "⚠️  La división entre cero no está definida⚠️"

def raiz_cuadrada(a):
    if a < 0:
        return "⚠️  ERROR, Las raíces negativas no están definidas en el conjunto de los reales⚠️"
    else:
        raiz = producto(a, 1)**0.5
        return raiz

def exponente(a, b):
    if a < 0 and 0 < b < 1:
        return "⚠️  Las raíces de un número negativo no están definida en el conjunto de los reales⚠️"
    elif a == 0 and b < 0:
        return "⚠️  La división por cero no está definida⚠️"
    else:
        exponente = producto(a, 1) ** b
        return exponente

def factorial(a):
    if a % 1 != 0:
        return "⚠️  El factorial solo está definido para números enteros⚠️"
    elif a == 0: 
        return 1
    elif a < 0:
        return "⚠️  El factorial no está definido para números negativos⚠️"
    else:
        return a*factorial(a-1)

def inversa(a):
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