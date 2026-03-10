print("Detectando nivel de tanque")
x = input("¿Nivel del tanque lleno? ")
if x == "si":
    y =input("¿Está la válvula cerrada? ")
    if y == "si":
        print("Mantener la válvula cerrada")
    elif y == "no":
        print("Cerrando válvula")
elif x == "no":
    z =input("¿Nivel del tanque vacío? ")
    if z == "si":
        print("Abrir válvula de entrada")
print("Volver a detectar")