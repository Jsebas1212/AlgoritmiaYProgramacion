def promedio(lista):
    if lista == []:
        return 0
    else:
        sumlista = sum(lista)
        return float(sumlista) / len(lista)

def promediosim_por_estudiante(diccionario):
    for nombre in diccionario:
        notas = diccionario[nombre]
        promnotas =promedio(notas)
        print(f"El promedio simple del estudiante '{nombre}' es: {promnotas} / 5,0")

def promedio_ponderado_estudiante(diccionario):
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
        totalnota = (notas[0] * 0.30) + (notas[1] * 0.30) + (notas[2] * 0.40)
        if totalnota > nota_mayor:
            nota_mayor = totalnota
            mejor_estudiante = nombre
    print(f"El estudiante '{mejor_estudiante}' fué quién obtuvo la mayor nota final, obteniendo {nota_mayor} / 5.0")

def estudiantes_qpasan(diccionario):
    for nombre in diccionario:
        notas = diccionario[nombre]
        nota_total = (notas[0] * 0.30) + (notas[1] * 0.30) + (notas[2] * 0.40)
        if nota_total >= 3.0:
            print(f"¡'{nombre}' APROBÓ la clase de la profesora Mcgonagall con nota de {nota_total} / 5.0 !")

def estudiantes_qnopasan(diccionario):
    for nombre in diccionario:
        notas = diccionario[nombre]
        nota_total = (notas[0] * 0.30) + (notas[1] * 0.30) + (notas[2] * 0.40)
        if nota_total < 3.0:
            print(f"¡'{nombre}' NO APROBÓ la clase de la profesora Mcgonagall con nota destroza de {nota_total} / 5.0 !")

notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Daco": [4.5, 4.2, 5.0],
    "Nevil": [2.5, 3.0, 3.2]
    }

while True:
    print("""
Seleccione acción que desea realizar:
    
1. Promedio simple de cada estudiante
2. Promedio ponderado de cada estudiante
3. Estudiante con mayor promedio final
4. Mostrar estudiantes aprobados
5. Mostrar todas a la vez
        """)
    seleccion = input("")
    if seleccion == "1":
        print("")
        promediosim_por_estudiante(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion == "2":
        print("")
        promedio_ponderado_estudiante(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion == "3":
        print("")
        mayor_promedio(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion == "4":
        print("")
        estudiantes_qpasan(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion == "5":
        print("")
        print("Promedio simple de cada estudiante:")
        promediosim_por_estudiante(notas)
        print("")
        print("Promedio ponderado de cada estudiante:")
        promedio_ponderado_estudiante(notas)
        print("")
        print("Estudiante con mayor promedio final:")
        mayor_promedio(notas)
        print("")
        print("Mostrar estudiantes aprobados:")
        estudiantes_qpasan(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion == "6":
        print("")
        estudiantes_qnopasan(notas)
        print("")
        input("Presione 'enter' para volver a las opciones")
    elif seleccion.lower() in ["salir","s"]:
        break
    else:
        print("Opción inválida, vuelva e ingrese una opción válida")