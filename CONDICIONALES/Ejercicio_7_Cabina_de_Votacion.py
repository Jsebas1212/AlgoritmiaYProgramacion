x = input("Seleccione candidato a votar: ")
if x == "A" or x == "a" :
    A = input("¿Confirmar voto por el partido \033[33mAmarillo\033[0m? ")
    if A == "si" :
        print("Usted ha votado por el partido \033[33mAmarillo\033[0m")
        print("\033[32mVoto registrado correctamente, gracias por votar!!\033[0m")
    elif A == "no" :
        print("\033[31mVoto cancelado\033[0m")
        print("\033[34mVolviendo a la selección de candidatos... \033[0m")
elif x == "M" or x == "m" :
    M = input("¿Confirmar voto por el partido \033[35mMorado\033[0m? ")
    if M == "si" :
        print("Usted ha votado por el partido \033[35mMorado\033[0m")
        print("\033[32mVoto registrado correctamente, gracias por votar!!\033[0m")
    elif M == "no" :
        print("\033[31mVoto cancelado\033[0m")
        print("\033[34mVolviendo a la selección de candidatos... \033[0m")
elif x == "N" or x == "n" :
    N = input("¿Confirmar voto por el partido \033[38;2;255;165;0mNaranja\033[0m? ")
    if N == "si" :
        print("Usted ha votado por el partido \033[38;2;255;165;0mNaranja\033[0m")
        print("\033[32mVoto registrado correctamente, gracias por votar!!\033[0m")
    elif N == "no" :
        print("\033[31mVoto cancelado\033[0m")
        print("\033[34mVolviendo a la selección de candidatos... \033[0m")
else :
    print("\033[31mOpción inválida. Por favor, seleccione un candidato válido.\033[0m")