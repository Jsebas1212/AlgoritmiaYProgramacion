while True:
    print("\nRegistrando hora...")
    t = (input("\n¿Son las 6 A.M.? "))
    if t == "no" :
        print("\nAun no suena la alarma")
    elif t == "si" :
        print("\n¡Sonando alarma!")
        b = 0
        while b < 3:
            Apag = input("\n¿Se ha apagado la alarma? ")
            if Apag == "no" :
                b = b + 1
                if b != 3:
                    print("\n¡Sigue sonando la alarma!")
                elif b == 3:
                    print("\nApagando despertador")
            elif Apag == "si" :
                print("\nApagando despertador")
                b = 3