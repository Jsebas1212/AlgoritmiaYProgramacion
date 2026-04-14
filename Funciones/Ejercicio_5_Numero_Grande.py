"""
El código recibe una lista con diferentes números,
la revisa y define cual es el número más grande de
esa lista

prompt: Generame una función para python a la cual
yo le entrego una lista con varios números y me arroje
el número más grande.

Johan Sebastian Echeverry Vega
c.c. 111372839
Universidad Tecnológica de Pereira
Fecha: 2026/04/13
"""
def encontrar_num_grande(lista):
    """
    Esta función encuentra y devuelve el número de mayor
    valor dentro de una lista.

    Parámetros:
    lista (list): Una lista que contiene números (enteros o reales).

    Retorna:
    int o float: El número más grande encontrado en la lista.
    list: Una lista vacía [] si la lista ingresada original estaba vacía.
    """
    if lista == []:
        return []
    else:
        numero_grande = lista[0]
        for numero in lista:
            if numero > numero_grande:
                numero_grande = numero
        return numero_grande
    
print("""
        ---Bienvenido usuario promedio---

          ~~~Notas de actualización~~~
  ---El programa corre una sexta parte más rápido
  ---Se solucionó el bug que borraba la carpeta de system32
  ---Removed Herobrine
""")                       #Aprendí a hacer esto con triple comilla desdeel código pasado, solo que olvidé comentarlo
while True:
    option = input("\nPresiona enter para continuar o escribe 's' para salir del programa: ")
    if option == "":
        while True:
            lis_user = input("\nIntroduce una lista de números separados por espacios para encontrar el más grande: ")
            if lis_user.lower() == "salir" or lis_user.lower() == "s":
                print("\nSaliendo del programa...")
                exit()
            elif lis_user.lower() == "eléctrica":
                print("\n¡Has encontrado un easter egg!")
                print("¡¡Viva la ingeniería electrica carajo!!")
            else:
                elementos_lis = lis_user.split() 
                numeros_validos = [] 
                for item in elementos_lis:
                    try:
                        numero_convertido = float(item)
                        numeros_validos.append(numero_convertido) #".append" se utiliza para agregar un único elemento al final de una lista. El ".append()"" está actuando como un "recolector de números buenos". Está construyendo una lista nueva y limpia, agregando uno por uno los elementos que sí pasaron la prueba de ser números.
                    except ValueError:
                        print(f"\nSe ignoró el elemento '{item}' porque no es un número válido.")
                if numeros_validos:                               #La forma en la que este "if" está funcionando es muy buen truco, basicamente está verificando si hay al menos un elemento dentro de esa lista, el caso de que si pasa a imprimir el resultado del numero más grande, si no hay nada entonces pasa al else e imprime un mensaje.
                    print(f"\nEl número más grande de los valores válidos en la lista ingresada:")
                    print(f"[{" ".join(elementos_lis)}]")
                    print(f"\nes: {encontrar_num_grande(numeros_validos)}")
                else:
                    print("\nNo se encontró ningún número válido en tu lista para comparar.")
    elif option.lower() == "s" or option.lower() == "salir":
        print("""
            Saliendo del programa...
            Entonces pa qué lo abrió jum
            """)                      #Ando probando formas de organizar el texto
        break
    else:
        print("\nA veces como que los chamos no entienden las instrucciones, por favor ingresa una opción válida.")