lista = ["client1","client2","client3","client4","client5"]

valu = 0.15

nomclient = input("Ingrese matrícula del cliente: ")
if nomclient in lista:
    consuclient = float(input("Ingrese consumo en kwh: "))
    if consuclient < 0 :
        print("Error, ingrese un valor positivo")
    elif consuclient >= 0 :
        print("El valor del consumo de", nomclient, "es de $",consuclient * valu)
else:    
    print("Cliente no encontrado, por favor ingrese un cliente válido")