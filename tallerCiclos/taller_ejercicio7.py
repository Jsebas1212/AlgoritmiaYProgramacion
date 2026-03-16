print("---¡¡¡Simluador de borracho!!!---") #El título me recuerda a un tamagotchi
print("\nPara moverlo seguir el sentido de las flechas del teclado numérico")
print("o tambien puede utilizar las techas w, a, s, d")
print("\n8 = w = arriba   4 = a = izquierda   6 = d = derecha   2 = = s = abajo")
x = 0
y = 0
while True: #la mayoria de estos añadidos son por capricho y personalización, sorry
    starexit = input("Escribe 'e' para empezar o 's' para salir ")
    if starexit == "e":
        for posición in range (100):
            print(f"\n--- Paso {posición + 1} de 100 ---")
            posición = input("Hacia donde se ha movido? ")
            if posición == "6" or posición == "d":
                print("Se ha movido una cuadra hacia la derecha")
                x = x + 1
            elif posición == "2" or posición == "s":
                print("Se ha movido una cuadra hacia ababjo")
                y = y - 1
            elif posición == "4" or posición == "a":
                print("Se ha movido una cuadra hacia la izquierda")
                x = x - 1
            elif posición == "8" or posición == "w":
                print("Se ha movido una cuadra hacia arriba")
                y = y + 1
            else:
                print("Opción inválida, el borracho no se ha movido en este paso")
        print(f"\nDespués de 100 pasos el borracho se ha detenido en la posición ({x},{y})")
    elif starexit == "s":
        print("---Cerrando simulador---")
        break
    else:
        print("Por escriba una opción válida")
    #Hago una aclaración y es que en el diagrama de flujo puse las opciones 1, 2, 3, 4, pero mientras constuia el código
    #me di cuenta que podría ser mejor para el usuario usar 8 o w, 2 o s, 4 o a y 6 o d, ya que si nos fijamos en el teclado
    #numérico de nuestros teclados podremos ver esos mismos números señalados con flechas las cuales podemos tomar de referencia
    #para la dirección a donde se mueve el borracho, lo mismo para las teclas w, a, s y d, estas siendo la dirección típica en
    #los videojuegos.