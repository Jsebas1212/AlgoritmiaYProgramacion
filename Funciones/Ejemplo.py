# # text = input("INGRESE UNA LISTA DE NUMEROS")
# # Lista = text.split(",")
# # print("La lista es: ", Lista)
# # numero = %2 == 0:
# # numero ** 2

# listapru = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def procesar_pares(lista):
#     # 1. CASO BASE (El freno): Si la lista está vacía
#     if lista == []:
#         return []
        
#     # 2. PASO RECURSIVO (El motor):
#     # Si el primer número es par...
#     if lista[0] % 2 == 0:
#         # Lo elevamos al cuadrado y lo unimos al resto
#         return [lista[0] ** 2] + procesar_pares(lista[1:])
        
#     # Si no es par (es impar)...
#     else:
#         # Lo ignoramos y pasamos directo al resto de la lista
#         return procesar_pares(lista[1:])

ID_aleatorio = id(object())
print("")
print(ID_aleatorio)
maximo = 15 
mínimo = 10
rango = maximo - mínimo + 1
numero_aleatorio = (ID_aleatorio % rango) + mínimo

print("")
print(maximo)
print("")
print(mínimo)
print("")
print(rango)
print("")
print(numero_aleatorio)