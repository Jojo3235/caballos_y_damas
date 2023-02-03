def pedir_numero(cond):
    while True:
        try:
            numero = int(input(cond))
            break
        except ValueError:
            print("No es un numero")
    return numero

def posición_damas(n):
    lista_pares = []
    lista_impares = []
    if n == 2 or n == 3:
        return []
    else:
        for i in range(n):
            if (i+1)%2 == 0:
                lista_pares.append((i))
            else:
                lista_impares.append((i)) 
        lista_final = lista_pares + lista_impares
    return lista_final
        

def main():
    n = pedir_numero("Introduce el numero de casillas(<1000000): ")
    try:
        if n <= 1000000:
            print(posición_damas(n))
        else:
            raise OverflowError("El número excede el límite permitido")
    except OverflowError as e:
        print(type(e).__name__ + ": " + str(e))

if __name__ == "__main__":
    main()