S =input("¿Se ha lanzado el dado? ")
if  S == "si" or S == "Si" or S == "SI" or S == "sI" :
    N = int(input("¿Qué número ha salido? "))
    if N == 1:
        print("Posición en x = x + 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif N == 2:
        print("Posición en y = y - 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif N == 3:
        print("Posición en x = x - 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif N == 4:
        print("Posición en y = y + 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif N < 1 or N > 4:
        print("Número inválido, repetir lanzamiento")
elif S == "no" or S == "No" or S == "NO" or S == "nO" :
    print("Esperando lanzamiento del dado...")