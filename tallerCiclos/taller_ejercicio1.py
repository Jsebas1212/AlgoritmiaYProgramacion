n = int(input("Ingrese valor: "))
i = 0
print(f"\nCuadrados menores que {n}:") #Las llaves junto con la f antes de las comillas me permiten meter la variable dentro del texto sin cerrar las comillas. En esencia la pongo por estética y controlar de mejor manera los espacios.
while i * i < n:                        #el \n lo uso básicamente para dejar renglones entre los mensajes que imprime el print. Es tambien pura estética, lo sé, soy algo quisquilloso con eso ¯\_(ツ)_/¯
    print(i * i, end=" ")               #para dejar los espacios tambien pude haber usado varios print uno abajo de otro pero usar el \n es más cómodo y más límpio (ദ്ദി˙ᗜ˙)
    i = i + 1
diez = 10
print(f"\n\nNumeros positivos divisibles por 10 y menores que {n}:")
while diez < n:
    print(diez, end=" ")
    diez = diez +10
contador = 0
valor = 2**contador
print(f"\n\nPotencias de 2 menores que {n}:")
while valor < n:
    print(valor, end=" ")
    contador = contador + 1
    valor = 2**contador