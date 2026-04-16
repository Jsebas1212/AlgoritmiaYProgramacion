def generar_numero(minimo, maximo):
    numero_base = id(object())
    rango = maximo - minimo + 1
    numero_final = (numero_base % rango) + minimo
    return numero_final

def elegir_dificultad():
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

# def jugar(intentos):
#     numero_secreto = generar_numero(1, 100)
#     intentos_restantes = intentos
#     victoria = False
    
#     print("\n¡Que comience el juego! He pensado un número entre 1 y 100.")
    
#     while intentos_restantes > 0:
#         print(f"\n--- Intentos restantes: {intentos_restantes} ---")
        
#         try:
#             intento_usuario = int(input("¿Cuál crees que es el número?: "))
#         except ValueError:
#             print("Por favor, introduce solo números.")
#             continue

#         if intento_usuario == numero_secreto:
#             print(f"¡INCREÍBLE! Adivinaste el número {numero_secreto}.")
#             victoria = True
#             resultado_log = f"GANÓ: Adivinó el {numero_secreto} usando {intentos - intentos_restantes + 1} intentos."
#             break
#         elif intento_usuario < numero_secreto:
#             print("Pista: El número secreto es MAYOR.")
#         else:
#             print("Pista: El número secreto es MENOR.")
        
#         intentos_restantes = intentos_restantes - 1

#     if not victoria:
#         print(f"\nSe agotaron los intentos. El número secreto era {numero_secreto}.")
#         resultado_log = f"PERDIÓ: No adivinó el {numero_secreto} en {intentos} intentos."

#     with open("historial_partidas.txt", "a", encoding="utf-8") as archivo:
#         archivo.write(resultado_log + "\n")
    
#     print("\n-> Partida guardada en el historial 'historial_partidas.txt'.")

# --- BLOQUE DE EJECUCIÓN ---
intentos_seleccionados = elegir_dificultad()
jugar(intentos_seleccionados) #No tomar en cuenta hasta no entender como funciona comoletamente