def promedio(lista):
    if lista == []:
        return 0
    else:
        sumlista = sum(lista)
        return float(sumlista) / len(lista)

def encontrar_num_grande(lista):
    if lista == []:
        return []
    else:
        numero_grande = lista[0]
        for numero in lista:
            if numero > numero_grande:
                numero_grande = numero
        return numero_grande
    
def encontrar_num_pequeño(lista):
    if lista == []:
        return []
    else:
        numero_pequeño = lista[0]
        for numero in lista:
            if numero < numero_pequeño:
                numero_pequeño = numero
        return numero_pequeño
    
def dias_sobre_promedio(lista):
    promlist = prom(lista)
    count = 0
    for i in lista:
        if i > promlist:
            count = count + 1
    return count

