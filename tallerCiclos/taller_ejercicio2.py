num1 = 0
suma1 = 0
while num1 <= 100:
    suma1 = suma1 + num1
    num1 = num1 + 2
print(suma1)

num2 = 0
suma2 = 0
while num2 <= 100:
    suma2 = suma2 + (num2**2)  
    num2 = num2 + 1
print(suma2)

rangeA = int(input("Escriba el valor del inicio del rango: "))
rangeB = int(input("Escriba el valor del final del rango: "))
if rangeA < rangeB:
    sumimp = 0
    for numero in range(rangeA, rangeB +1):
        if numero %2 !=0:
            sumimp += numero
    print(sumimp, end=" ")
else:
    print("El valor del inicio debe ser menor que el valor del final")
    