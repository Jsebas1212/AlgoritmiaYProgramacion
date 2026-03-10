x = float(input("Ingresa el primer número: "))
O = input("Seleccione la operación a realizar: ")
y = float(input("Ingresa el segundo número: "))
if O == "+":
    print("El resultado de la suma es: ", x + y)
elif O == "-":
    print("El resultado de la resta es: ", x - y)
elif O == "*":
    print("El resultado de la multiplicación es: ", x * y)
elif O == "/":
    if y != 0: #el != lo que hace es excluir el valor, es decir, si "y" es diferente de 0, entonces se realiza la división
        print("El resultado de la división es: ", x / y)
    else:
        print("Error: No se puede dividir por cero")