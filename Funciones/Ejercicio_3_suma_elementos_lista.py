def suma_recursiva(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])

print("---Hey muy buenas a todos, wapisimos!!!---")
input("")