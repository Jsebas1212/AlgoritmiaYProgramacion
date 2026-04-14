#En un inicio no comprendí si el ejercicio se refería a invertir el orden de las palabras o a invertir el orden de los caracteres, así que decidí hacer ambas cosas por si acaso
"""
El código recibe un texto del usuario y,
según lo que este elija, le da la vuelta
devolviéndolo al revés, ya sea invirtiendo
el orden de las palabras o invirtiéndolo
letra por letra.

prompt: Generame una función en python la cual me
invierta el orden de las palabras de una cadena de
texto y otro que me invierta el el orden pero letra
por letra tambien de una cadena de texto.

Johan Sebastian Echeverry Vega
c.c. 111372839
Universidad Tecnológica de Pereira
Fecha: 2026/04/13
"""
def invertir_cadena(texto):
    """
    Invierte el orden de los caracteres de una cadena
    de texto mediante recursividad.

    Parámetros:
    texto (str): La cadena de texto original que se desea
    invertir.

    Retorna:
    str: Una nueva cadena con los caracteres en orden
    inverso.
    """
    if texto == "":
        return "" 
    else:
        return invertir_cadena(texto[1:]) + texto[0]

def invertir_lista(texto):
    """
    Invierte el orden de los elementos (palabras) de una lista mediante recursividad.

    Parámetros:
    texto (list): Una lista que contiene las palabras del texto separadas.

    Retorna:
    list: Una nueva lista con las palabras en orden inverso.
    """
    if texto == []:
        return []
    else:
        return invertir_lista(texto[1:]) + [texto[0]]
        
print("""
---Bienvenido al Invierte texto 5000!!!---
---(Pucha que nombre más genérico, no se me ocurrió nada mejor)---""")
while True:
    options = input("\nPresiona enter para continuar o escribe 's' para salir del programa: ")
    if options == "":
        while True:
            texto = input("\nIngrese un texto: ")
            while True:
                pregunta = input("\nDesea invertir el orden de las palabras o de los caracteres?: (P/C) ")
                if pregunta.lower() == 'p':
                    lista_texto = texto.split()
                    resultado = invertir_lista(lista_texto)
                    print("\nTexto con palabras invertidas:")
                    print(" ".join(resultado)) #El ".join" toma los elementos sueltos de una lista y los une para formar un solo texto normal (un string). Lo que ponga dentro de las comillas será con lo que voy a separar el texto, en este caso es por espacio pero podría ser un guión o lo que sea
                    break
                elif pregunta.lower() == 'c':
                    resultado = invertir_cadena(texto)
                    print("\nTexto con caracteres invertidos:")
                    print(resultado)
                    break
                elif pregunta.lower() == 'salir' or pregunta.lower() == 's':
                    print("Saliendo del programa...")
                    exit()
                else:
                    print("\n~~~Opción no válida, pongase serio ciervo, escriba una opción válida ome~~~")
    elif options.lower() == "s":
        print("Saliendo del programa...")
        break
    else:
        print("""
Si que sos terco no? Te estoy dando las opciones claras y no captas la idea. O presionas 'enter', o escribes 's' para salir,
o te vas a chingar a tu madre baboso""") #Creo que me pasé