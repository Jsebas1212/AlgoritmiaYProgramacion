#No se si interpreté el inciso "a" mal, pues por un lado pensé que se refería a 2 elevado a sus potencias desde 20 hasta 220,
#Tipo 2^20 2^21 2^22 ... 2^219 2^220, pero despúes leí y supuse que más bien podría ser el que dejé sin numerales en el código,
#Igualmente el primero que hice lo dejé de todas maneras pero sin formar parte del código a ejecutar, por si acaso (aunque no creo) ese sea el correcto.

# potencia = 20
# resultado = 0
# while potencia <= 220:
#     resultado = 2**potencia
#     potencia = potencia + 1 
#     print(resultado) #Un poco caótico este print ¯\_(ツ)_/¯


pot = 0
x = 0
while x < 220:
    x = 2**pot
    if x >= 20 and x <= 220:
        print(x, end=" ")
    pot = pot +1

