print("Registrando hora")
t = (input("¿Son las 6 A.M.? "))
if t == "si" :
    print("Sonando alarma")
elif t == "no" :
    print("Aun no suena la alarma")
if t == "si" :
    b = input("¿Se ha apagado la alarma? ")
    if b == "si" :
        print("Apagando despertador")
    elif b == "no" :
        print("Sigue sonando la alarma")
print("se repite ciclo")