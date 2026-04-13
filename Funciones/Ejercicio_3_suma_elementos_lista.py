def suma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

print("---Hey muy buenas a todos, wapisimos!!!---")
print("---Aquí Vegetta 777 en un nuevo directo de Planeta Vegetta!!!---")
print("---Ok no---")
while True:
    option = input("\nPresiona enter para continuar o escribe 'salir' para cerrar el progranma: ")
    if option == "":
        while True:
            numlist = input("\nEscribe una lista de números, ¡OJO! separados por espacios: ")
            if numlist == "salir":
                print("Saliendo...")
                exit()
            else:
                List1 = numlist.split()
                try: 
                    for o in range(len(List1)):
                        List1[o] = float(List1[o])
                    print("\nLa suma de los elementos de la lista ingresada es: ", suma_recursiva(List1))
                except ValueError:
                    print("\nPinche bruto, ¿no ves que solo puedes ingresar números? Intenta de nuevo ingeniero industrial.")
    elif option.lower() == "salir" or option.lower()== "s":
        print("Saliendo del programa...")
        break
    else:
        print("\nNo te quieras pasar de listo conmigo muchacho")
        print("Ingresa una opción válida por favor, ois?")