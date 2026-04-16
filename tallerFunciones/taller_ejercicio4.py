def promedio(lista):
    if lista == []:
        return 0
    else:
        sumlista = sum(lista)
        return float(sumlista) / len(lista)

def promedio_por_estudiante(diccionario):
    for nombre in diccionario:
        notas = diccionario[nombre]
        promnotas =promedio(notas)
        print(f"El promedio del estudiante '{nombre}' es: {promnotas} / 5,0")

def promedio_ponderado(diccionario):
    for nombre in diccionario:
        notas = diccionario[nombre]
        nota1 = notas[0]*0.30
        nota2 = notas[1]*0.30
        nota3 = notas[2]*0.40
        totalnota = nota1 + nota2 + nota3
        print(f"El promedio ponderado del estudiante '{nombre}' es: {totalnota} / 5,0")

def mayor_promedio(diccionario):
    nota_mayor = 0.0
    mejor_estudiante = ""
    for nombre in diccionario:
        notas = diccionario[nombre]
        nota1 = notas[0]*0.30
        nota2 = notas[1]*0.30
        nota3 = notas[2]*0.40
        totalnota = nota1 + nota2 + nota3
        if totalnota > nota_mayor:
            nota_mayor = totalnota
            mejor_estudiante = nombre
    print(f"El estudiante {nombre} fué quién obtuvo la mayor nota fina, obteniendo {nota_mayor} / 5.0")

def estudiantes_qpasan(diccionario):
    
notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Daco": [4.5, 4.2, 5.0],
    "Nevil": [2.5, 3.0, 3.2]
    }

#promedio_por_estudiante(notas)
#promedio_ponderado(notas)
#mayor_promedio(notas)












# def buscar_perfectos(limite):
#     print(f"Buscando números perfectos hasta el {limite}...")
#     for num in range(2, limite + 1):
#         suma_divisores = 0
#         # Optimizamos: solo buscamos divisores hasta la mitad del número
#         for i in range(1, (num // 2) + 1):
#             if num % i == 0:
#                 suma_divisores += i
        
#         if suma_divisores == num:
#             print(f"-> {num} es un número perfecto")

# # El programa correrá solo hasta el número que tú decidas
# buscar_perfectos(10000)

