print("---Suma de números pares desde 2 a 100---")
num1 = 0
suma1 = 0
while num1 <= 100:
    suma1 = suma1 + num1
    num1 = num1 + 2
print(f"la suma de todos los números impares desde 2 hasta 100 es: {suma1}")

print("\n---Suma de todos los cuadrados de 1 a 100---")
num2 = 0
suma2 = 0
while num2 <= 100:
    suma2 = suma2 + (num2**2)  
    num2 = num2 + 1
print(f"La suma de todos los cuadrados de 1 hasta 100 es: {suma2}")

print("\n---Suma de números impares en entre un rango---")
rangeA = int(input("Escriba el valor del inicio del rango: "))
rangeB = int(input("Escriba el valor del final del rango: "))
if rangeA < rangeB:
    sumimp = 0
    for numero in range(rangeA, rangeB +1):
        if numero %2 !=0:
            sumimp += numero
    print(f"la suma de los números impares entre {rangeA} y {rangeB} es: {sumimp}")
else:
    print("El valor del inicio debe ser menor que el valor del final")

print("\n---Suma de dígitos impares---")
n = int(input("Digite un número: "))
sums = 0
tex = str(n)
for xxy in tex:
    number = int(xxy)
    if number %2 != 0:
        sums = sums + number
print(f"\nLa suma de los números impares del número {n} es: {sums}")