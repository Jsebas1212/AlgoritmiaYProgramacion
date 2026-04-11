#En un inicio no comprendí si el ejercicio se refería a invertir el orden de las palabras o a invertir el orden de los caracteres, así que decidí hacer ambas cosas por si acaso
def invertir_cadena(texto):
    if texto == "":
        return "" 
    else:
        return invertir_cadena(texto[1:]) + texto[0]

def invertir_palabras(texto):
    if texto == []:
        return []
    else:
        return invertir_palabras(texto[1:]) + [texto[0]]
        
print("---Bienvenido al Invierte texto 5000!!!---")
print("---(Pucha que nombre más genérico, no se me ocurrió nada mejor)---")
while True:
    options = input("\nPresiona enter para continuar o escribe 's' para salir del programa: ")
    if options.lower() == "":
        while True:
            texto = input("\nIngrese un texto: ")
            while True:
                pregunta = input("\nDesea invertir el orden de las palabras o de los caracteres?: (P/C) ")
                if pregunta.lower() == 'p':
                    lista_texto = texto.split()
                    resultado = invertir_palabras(lista_texto)
                    print("\nTexto con palabras invertidas:")
                    print(" ".join(resultado))
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
        print("\nSi que sos terco no? Te estoy dando las opciones claras y no captas la idea. O presionas 'enter' o escribes 's' para salir")
        print("O te vas a chingar a tu madre baboso")