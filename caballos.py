def suma_rara(lista):
    suma = 0
    for arg in lista:
        if arg == 1:
            suma += 2
        elif arg == 2:
            suma += 2
        elif arg == 3:
            suma += 2
        elif arg == 4:
            suma += 3
        elif arg == 6:
            suma += 3
        elif arg == 7:
            suma += 2
        elif arg == 8:
            suma += 2
        elif arg == 9:
            suma += 2
        elif arg == 0:
            suma += 2
        else:
            print("none")
    return suma

def suma_rara2(lista):
    suma = 0
    for arg in lista:
        if arg == 1:
            suma += 5
        elif arg == 2:
            suma += 4
        elif arg == 3:
            suma += 5
        elif arg == 4:
            suma += 6
        elif arg == 6:
            suma += 6
        elif arg == 7:
            suma += 5
        elif arg == 8:
            suma += 4
        elif arg == 9:
            suma += 5
        elif arg == 0:
            suma += 6
    return suma

lista = [0,1,7,3,1,6,2,4,2,3,9,0,3,1,4,8,4,2,4,6,6,8,6,2,6,4,1,7,0,7,9,9,3,0,9,7,0,1,7,0,3,9,4,8,6,8]

def morfosear_lista(lista):
    nueva_lista = []
    for arg in lista:
        if arg == 1:
            nueva_lista.append(6)
            nueva_lista.append(8)
        elif arg == 2:
            nueva_lista.append(7)
            nueva_lista.append(9)
        elif arg == 3:
            nueva_lista.append(4)
            nueva_lista.append(8)
        elif arg == 4:
            nueva_lista.append(3)
            nueva_lista.append(0)
            nueva_lista.append(9)
        elif arg == 6:
            nueva_lista.append(0)
            nueva_lista.append(1)
            nueva_lista.append(7)
        elif arg == 7:
            nueva_lista.append(6)
            nueva_lista.append(2)
        elif arg == 8:
            nueva_lista.append(3)
            nueva_lista.append(1)
        elif arg == 9:
            nueva_lista.append(4)
            nueva_lista.append(2)
        elif arg == 0:
            nueva_lista.append(6)
            nueva_lista.append(4)
    return nueva_lista

lista_original = [1,2,3,4,6,7,8,9,0]

def suma_enesima(n, lista):
    i = 0
    lista_de_paso_2 = lista
    while i < n:
        i += 1
        lista_de_paso = morfosear_lista(lista_de_paso_2)
        lista_de_paso_2 = lista_de_paso
    return suma_rara(lista_de_paso_2)

print(suma_enesima(1,lista_original))