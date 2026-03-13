#No se si interpreté el inciso "a" mal, pues por un lado pensé que se refería a 2 elevado a sus potencias desde 20 hasta 220,
#Tipo 2^20 2^21 2^22 ... 2^219 2^220, pero despúes leí y supuse que más bien podría ser el que dejé sin numerales en el código,
#Igualmente el primero que hice lo dejé de todas maneras pero sin formar parte del código a ejecutar, por si acaso (aunque no creo) de que ese sea el correcto.

# potencia = 20
# resultado = 0
# while potencia <= 220:
#     resultado = 2**potencia
#     potencia = potencia + 1 
#     print(resultado) #Un poco caótico este print ¯\_(ツ)_/¯

print("---Todas las potencias de 2 entre el rango de 20 a 220---")
pot = 0
x = 0
while x < 220:
    x = 2**pot
    if x >= 20 and x <= 220:
        print(x, end=" ")
    pot = pot +1

print("\n\n---Suma de números impares en entre un rango---")
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
count = int(input("Digite un número: "))
sums = 0
tex = str(count)
for xxy in tex:
    number = int(xxy)
    if number %2 != 0:
        sums = sums + number
print(f"\nLa suma de los números impares del número {count} es: {sums}")

#Para aclarar, si, hice practicamente un copy-paste de los incisos "3" y "4" del ejercicio 2 para hacer el inciso "2" y "3" de este ejercicio
#Es que praticamente son los mismos así que no tuve necesidad de hacerlos desde ceroS