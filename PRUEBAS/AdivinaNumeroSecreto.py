import random

def generar_numero(minimo, maximo):
    return random.randint(minimo, maximo)

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
\33[1;32m1. Fácil   (10 intentos)\033[0m
\33[1;33m2. Media   (7 intentos)\033[0m
\33[1;31m3. Difícil (5 intentos)\033[0m
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
    print(numero_secreto)
    intentos_restantes = intentos
    victoria = False
    
    print("\n\033[38;5;208m¡Que comience el juego! He pensado un número entre 1 y 100.\033[0m")
    
    while intentos_restantes > 0:
        print(f"\n\033[94m--- Intentos restantes: {intentos_restantes} ---\033[0m")
        
        try:
            intento_usuario = int(input("¿Cuál crees que es el número?: "))
        except ValueError:
            print("\n\033[31mPor favor, introduce solo números.\033[0m")
            continue

        if intento_usuario == numero_secreto:
            print("\n\033[32m¡INCREÍBLE! Adivinaste el número correctamente.\033[0m")
            print(f"\033[93mEl número efectivamente era {numero_secreto}\033[0m")
            print("\033[32m¡FELICIDADES! ¡USTED GANÓ!\033[0m")
            victoria = True
            resultado_log = f"GANÓ: El jugador adivinó el {numero_secreto}"
            break

        print("\033[31mNúmero incorrecto, intenta de nuevo\033[0m")

        intentos_restantes -= 1  

        if intentos_restantes > 0:
            if intento_usuario < numero_secreto:
                print(f"\nPista: El número secreto es |MAYOR| que {intento_usuario} ⬆️.")
            else:
                print(f"\nPista: El número secreto es |MENOR| que {intento_usuario} ⬇️.")

    if not victoria:
        print(f"\nSe agotaron los intentos. El número secreto era {numero_secreto}.")
        print("\n\033[35mBuen intento jugador, suerte para la proxima ✌️\033[0m")
        resultado_log = f"PERDIÓ: El jugador no adivinó el {numero_secreto} en {intentos} intentos."

    with open("historial_partidas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(resultado_log + "\n")
    
    print("\n-> Partida guardada en el historial 'historial_partidas.txt'.")

while True:
    intentos_seleccionados = elegir_dificultad()
    jugar(intentos_seleccionados) 
    print("\n¿Desea volver a jugar? (S/N)")
    volver = input("")
    if volver.lower() in ["s","si"]:
        print("\nCargando nueva partida...")
    elif volver.lower() in ["n","no"]:
        print("\nNos vemos la proxima vez, adios...")
        break
