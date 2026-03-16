while True:
    print("\nDetectando nivel de tanque...")
    x = input("\n¿Nivel del tanque lleno? ")
    if x == "si":
        y = input("\n¿Está la válvula cerrada? ")
        if y == "si":
            print("\nManteniendo la válvula cerrada")
        elif y == "no":
            print("\nCerrando válvula")
    elif x == "no":
        z =input("\n¿Nivel del tanque vacío? ")
        if z == "si":
            print("\nAbrir válvula de entrada")
    elif x == "apagar":
        print("\n---Apagando sistema---\n")
        break 
#A este solo tuve que copiar y pegar y añadirle el while y el break como extra tambien
#Ah y los \n por mero capricho jeje