def generar_numero(minimo, maximo):
    """
    Genera un número pseudoaleatorio dentro de un rango específico.
    Utiliza la ubicación en memoria de un objeto nuevo (id(object())) 
    como base matemática para generar el número, evitando usar librerías externas.
    
    Parámetros:
    minimo (int): El límite inferior del rango numérico
    maximo (int): El límite superior del rango numérico
    
    Retorna:
    int: Un número entero aleatorio comprendido entre el mínimo y el máximo
    """
    numero_base = id(object())
    rango = maximo - minimo + 1
    numero_final = (numero_base % rango) + minimo
    return numero_final

def elegir_dificultad():
    """
    Despliega un menú interactivo para que el usuario seleccione la dificultad.
    Valida las diferentes formas en las que el usuario puede escribir su opción.
    
    Parámetros:
    Ninguno
    
    Retorna:
    int: La cantidad de intentos permitidos según la dificultad elegida 
         (10 para Fácil, 7 para Media, 5 para Difícil)
    """
    while True:
        print("""
Escoje el nivel de dificultad
1. Fácil   (10 intentos)
2. Media   (7 intentos)
3. Difícil (5 intentos)
              """)
        opcDificultad = input("")
        if opcDificultad.lower() in ["1","fácil","facil","10"]:
            return 10
        elif opcDificultad.lower() in ["2","media","7"]:
            return 7
        elif opcDificultad.lower() in ["3","difícil","dificil","5"]:
            return 5
        else:
            print("\nOpción no válida, vuelva a intentar")

def jugar(intentos):
    """
    Controla el ciclo principal del juego de adivinar el número.
    Maneja los intentos, proporciona pistas si el número es mayor o menor,
    valida errores de texto y guarda el historial de la partida en un archivo de texto.
    
    Parámetros:
    intentos (int): La cantidad de intentos disponibles para adivinar el número
    
    Retorna:
    Ninguno. Imprime toda la interacción en consola y escribe en historial_partidas.txt.
    """
    numero_secreto = generar_numero(1, 100)
    intentos_restantes = intentos
    victoria = False
    
    print("\n¡Que comience el juego! He pensado un número entre 1 y 100.")
    
    while intentos_restantes > 0:
        print(f"\n--- Intentos restantes: {intentos_restantes} ---")
        
        try:
            intento_usuario = int(input("¿Puedes adivinar qué número es?: "))
        except ValueError:
            print("Por favor, introduce solo números.")
            continue

        if intento_usuario == numero_secreto:
            print(f"\n¡INCREÍBLE! Adivinaste el número correctamente.")
            print(f"El número efectivamente era '{numero_secreto}.'")
            print("¡FELICIDADES! ¡USTED GANÓ!")
            victoria = True
            resultado_log = f"GANÓ: El jugador adivinó el {numero_secreto} usando {intentos - intentos_restantes + 1} intentos."
            break
        elif intento_usuario < numero_secreto:
            print("\nNúmero incorrecto, intenta de nuevo")
            print("\nPista: El número secreto es |MAYOR| ⬆️.")
        else:
            print("\nNúmero incorrecto, intenta de nuevo")
            print("\nPista: El número secreto es |MENOR| ⬇️.")
        
        intentos_restantes = intentos_restantes - 1

    if not victoria:
        print(f"\nSe agotaron los intentos. El número secreto era {numero_secreto}.")
        print("\nBuen intento jugador, suerte para la proxima ✌️")
        resultado_log = f"PERDIÓ: El jugador no adivinó el {numero_secreto} en {intentos} intentos."

    with open("historial_partidas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(resultado_log + "\n")
    
    print("\n-> Partida guardada en el historial 'historial_partidas.txt'.")

intentos_seleccionados = elegir_dificultad()
jugar(intentos_seleccionados) 

