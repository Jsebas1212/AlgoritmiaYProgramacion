def encontrar_num_grande(lista):
    if lista == []:
        return []
    else:
        numero_grande = lista[0]
        for numero in lista:
            if numero > numero_grande:
                numero_grande = numero
        return numero_grande
    
print("---Bienvenido usuario promedio---")
print("\n~~~Notas de actualización~~~")
print("---El programa corre una sexta parte más rápido---")
print("---Se solucionó el bug que borraba la carpeta de system32---")
print("---Removed Herobrine---")
option = input("\nPresiona enter para continuar o escribe 's' para salir del programa: ")
if option.lower() == "":
    while True:
        lis_user = input("\nIntroduce una lista de números separados por espacios para encontrar el más grande: ")
        if lis_user.lower() == "salir" or lis_user.lower() == "s":
            print("Saliendo del programa...")
            break
        elif lis_user.strip() == "Eléctrica":
            print("\n¡Has encontrado el easter egg!")
            print("¡¡Viva la ingeniería electrica carajo!!")
        else:
            num_list = lis_user.split()
            for i in range(len(num_list)):
                try:
                    num_list[i] = float(num_list[i])
                except ValueError:
                    print(f"Error: '{num_list[i]}' no es un número válido.")
                    break
            else:
                print("\nEl número más grande de la lista ingresada es: ")
                print(encontrar_num_grande(num_list))
elif option.lower() == "s" or option.lower() == "salir":
    print("Saliendo del programa...")
    print("Entonces pa qué lo abrió jum")
else:
    print("A veces como que los chamos no entienden las instrucciones, por favor ingresa una opción válida.")