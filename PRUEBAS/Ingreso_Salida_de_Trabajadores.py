Base_de_Trabajadores = {"Juan", "Valeria", "Sebastian", "Julian", "Pablo", "juan", "valeria", "sebastian", "julian", "pablo"}
x = input("Bienvenido, qué registra? ")
if x == "Entrada" or x == "entrada":
    ingreso = input("Ingrese su nombre ")
    if ingreso in Base_de_Trabajadores:
        print("Registro de entrada exitoso!!")
        print("Hora de entrada 9:00 am")
        print("Bienvenido", ingreso,", qué tenga un buen día")
        print("Recuerde que le pagamos, portese bien")
    else:
        print("Entrada rechzada, largo pejelagarto")
elif x == "Salida" or x == "salida" :
    salida = input("Ingrese su nombre ")
    if salida in Base_de_Trabajadores:
        print("Hora de salida 5:00 pm")
        print("Hasta mañana, tenga un buen descanso exclavo del sistema")
    else:
        print("Salida rechazada, no se encuentra en la base de datos de trabajadores")
        print("¿Y a este random quién lo dejó entrar?")
else:
    print("Opción no válida, por favor ingrese 'Entrada' o 'Salida'")
    print("Aprende a leer ome")