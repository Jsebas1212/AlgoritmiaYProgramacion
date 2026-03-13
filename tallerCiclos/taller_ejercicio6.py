print("Escriba 'cerrar' si quiere apagar el programa")
while True:
    valor = input("\nEscriba un número para descomponerlo en sus factores primnos: ")
    if valor == "cerrar":
        print("\n---Apagando código---\n")
        break
#Como quería que mi código funcionara teniendo en cuenta todas las posibiliades tuve que aprender a utilizar el "try", el cual significa "intenta" y el "except".
#Osea que básicamente lo que hace try es decirle a el if "intenta hacer esto" y juton al except "y si no funciona no saltes error y en vez de eso has esto (y de ahí salta al mensaje del print)",
#entonces fue una adición que le quise poner y a su vez aprender para evitar qué hayan errores en el programa y a su vez que lo que se realice se siga ejecutando de forma lineal sin desvios
    try:
        numero = int(valor)
        div = 2
        if numero <= 1:
            print("\n===Por favor ingrese un número mayor a 1===")
            continue 
#Lo que hace el "continue" es decirle al ciclo "while" que se detenga, como decir "vea, el número que pusieron es menor o igual que 1, paila no siga hacia abajo, devuelvase más bien" (que ejemplo tan malo sinceramente)
#entonces se va a devolver hacia el inicio (while true), es basicamente una condición de parada pero que en vez de detener el programa, lo devuelve y ya, estoy sonando algo ambiguo lo se kkkk.
        print(f"\nLos factores primos del número {numero} son: ")
        while numero > 1:
            if numero % div == 0:
                print(div)
                numero = numero // div
            else:
                div = div + 1
    except ValueError:
        print("\n===No se permite texto, ingrese un número entero mayor a 1 por favor===")
#Vuelvo y aclaro que la mayoria de implementaciones extra son solo caprichos mios para hacer el código más chevere y completo por así decirlo 
#Cumplo con lo que el ejercicio pide, y además lo hace mas preciso, correcto, y con funciones u opciones extra que ayudan a que no ocurran o hayan tantos errores.