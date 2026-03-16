while True:
    print("\nRegistrando hora...")
    t = (input("¿Son las 6 A.M.? "))
    if t == "no" :
        print("\nAun no suena la alarma")
    elif t == "si" :
        print("\n¡Sonando alarma!")
        b = 0
        while b < 60:
            Apag = input("¿Se ha apagado la alarma? ")
            if Apag == "no" :
                b = b + 1
                if b != 60:
                    print("\n¡Sigue sonando la alarma!")
                elif b == 60:
                    print("\nApagando despertador")
            elif Apag == "si" :
                print("\n--Apagando despertador--")
                b = 60
    elif t == "desactivar":
        print("\n---Alarma desactivada---\n")
        break #La opción de apagado fué una idea de ultimo momento para el código