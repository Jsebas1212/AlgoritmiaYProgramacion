#Este código es para calcular números perfectos

# def buscar_perfectos(limite): 
#     print(f"Buscando números perfectos hasta el {limite}...")
#     for num in range(2, limite + 1):
#         suma_divisores = 0
#         # Optimizamos: solo buscamos divisores hasta la mitad del número
#         for i in range(1, (num // 2) + 1):
#             if num % i == 0:
#                 suma_divisores += i
        
#         if suma_divisores == num:
#             print(f"-> {num} es un número perfecto")

# # El programa correrá solo hasta el número que tú decidas
# buscar_perfectos(10000)


#Este es para comprobar si un número es perfecto

def comprobar_numero_perfecto(n):
    divisores = []
    # 1. Sacar los divisores del número
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    
    # 2. Resultado de la suma de todos los divisores por aparte
    suma_total = sum(divisores)
    
    # 3. Resultado de los divisores menos el mismo número (divisores propios)
    suma_propios = suma_total - n
    
    # Mostrar resultados
    print(f"Número evaluado: {n}")
    print(f"1. Lista de todos los divisores: {divisores}")
    print(f"2. Suma de todos los divisores: {suma_total}")
    print(f"3. Suma de divisores menos el {n}: {suma_propios}")
    
    # Comprobación final
    if suma_propios == n:
        print(f"\n¡Resultado! {n} ES un número perfecto.")
    else:
        print(f"\nResultado: {n} NO es un número perfecto.")

# Prueba el código con el número que quieras
numero_usuario = int(input("Introduce un número para comprobar: "))
comprobar_numero_perfecto(numero_usuario)

33550336
#Calcular el 5to número perfecto tomarría de 4 a 10 horas dependiendo del procesador