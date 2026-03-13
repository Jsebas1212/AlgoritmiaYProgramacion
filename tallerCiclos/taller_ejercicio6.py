while True:
    valor = input("Escriba algún número: ")
    if valor == "cerrar":
        print("\n---Apagando código---\n")
        break
    else:
        print("Error, no se permite texto")
        numero = int(valor)
        div = 2
        while numero > 1:
            if numero % div == 0:
                print(div)
                numero = numero // div
            else:
                div = div + 1