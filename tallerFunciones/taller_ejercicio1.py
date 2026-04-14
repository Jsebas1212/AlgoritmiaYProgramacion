def promedio(lista):
    if lista == []:
        return 0
    else:
        sumlista = sum(lista)
        return float(sumlista) / len(lista)

def encontrar_max(lista):
    if lista == []:
        return []
    else:
        numero_grande = lista[0]
        for numero in lista:
            if numero > numero_grande:
                numero_grande = numero
        return numero_grande
    
def encontrar_min(lista):
    if lista == []:
        return []
    else:
        numero_pequeño = lista[0]
        for numero in lista:
            if numero < numero_pequeño:
                numero_pequeño = numero
        return numero_pequeño
    
def dias_sobre_promedio(lista):
    promlist = promedio(lista)
    count = 0
    for i in lista:
        if i > promlist:
            count = count + 1
    return count

temperaturas = [21,23,27,29,30,32,34,35,35,34,33,32,31,29,28,25,23,22,18,15,16,17,19,20]

print("El promedio de las temperaturas es:")
print(f"{promedio(temperaturas)}°c")

print("\nLa temperatura más grande es:")
print(f"{encontrar_max(temperaturas)}°c")

print("\nLa temperatrura más baja es:")
print(f"{encontrar_min(temperaturas)}°c")

print(f"\nLa temperatura estuvo por encima del promedio {dias_sobre_promedio(temperaturas)} veces")