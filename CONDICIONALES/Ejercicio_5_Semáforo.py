print("Luz roja encendida")
x = input("¿Han pasado 20 segundos? ")
if x == "si":
    print("Apgando luz roja")
    print("Encendiendo luz verde")
    y = input("¿Han pasado 40 segundos? ")
    if y == "si":
        print("Encendiendo luz amarilla")
        z = input("¿Han pasado 5 segundos? ")
        if z == "si":
            print("Apagando luz amarilla")
            print("Apagando luz verde")
            print("sumando 1 al ciclo")
            print("Encendiendo luz roja")
        elif z == "no":
            print("Esperar a que pasen 5 segundos")
            print("sumando 1s al tiempo")
    elif y == "no":
        print("Esperando a que pasen 40 segundos")
        print("sumando 1s al tiempo")
elif x == "no":
    print("Esperando a que pasen 20 segundos")
    print("sumando 1s al tiempo")