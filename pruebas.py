import numpy as np

A = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
A = np.array(A)

def multiplicar_matrices(A,B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0]*p for i in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k]*B[k][j]
    return C

def separar_matrices(A):
    n = len(A)
    return A[:n//2,:n//2], A[:n//2,n//2:], A[n//2:,:n//2], A[n//2:,n//2:]

def metodo_strassen(A,B):
    if len(A) <= 2:
        return multiplicar_matrices(A,B)
    else:
        a, b, c, d = separar_matrices(A)
        e, f, g, h = separar_matrices(B)
        p1 = metodo_strassen(a+d, e+h)
        p2 = metodo_strassen(d, g-e)
        p3 = metodo_strassen(a+b, h)
        p4 = metodo_strassen(b-d, g+h)
        p5 = metodo_strassen(a, f-h)
        p6 = metodo_strassen(c+d, e)
        p7 = metodo_strassen(a-c, e+f)
        c11 = p1 + p2 - p3 + p4
        c12 = p5 + p3
        c21 = p6 + p2
        c22 = p5 + p1 - p6 - p7
        C = np.vstack((np.hstack((c11,c12)), np.hstack((c21,c22))))
        return C

# print(A)

# # A*A
# A2 = metodo_strassen(A,A)
# A3 = metodo_strassen(A2,A)
# A4 = metodo_strassen(A3,A)
# A5 = metodo_strassen(A4,A)
# A6 = metodo_strassen(A5,A)
# A7 = metodo_strassen(A6,A)
# A8 = metodo_strassen(A7,A)
# A9 = metodo_strassen(A8,A)
# A10 = metodo_strassen(A9,A)
# A11 = metodo_strassen(A10,A)
# A12 = metodo_strassen(A11,A)
# A13 = metodo_strassen(A12,A)
# A14 = metodo_strassen(A13,A)
# A15 = metodo_strassen(A14,A)
# A16 = metodo_strassen(A15,A)
# A17 = metodo_strassen(A16,A)
# A18 = metodo_strassen(A17,A)
# A19 = metodo_strassen(A18,A)
# A20 = metodo_strassen(A19,A)
# A21 = metodo_strassen(A20,A)
# A22 = metodo_strassen(A21,A)
# A23 = metodo_strassen(A22,A)
# A24 = metodo_strassen(A23,A)
# A25 = metodo_strassen(A24,A)
# A26 = metodo_strassen(A25,A)
# A27 = metodo_strassen(A26,A)
# A28 = metodo_strassen(A27,A)
# A29 = metodo_strassen(A28,A)
# A30 = metodo_strassen(A29,A)
# A31 = metodo_strassen(A30,A)
# A32 = metodo_strassen(A31,A)

def n_potencia(A,n):
    i = 0
    A2 = A
    if n == 0:
        return np.identity(len(A))
    while i < n-1:
        A2 = metodo_strassen(A2,A)
        i += 1
    return A2

def pedir_numero(cond):
    while True:
        try:
            numero = int(input(cond))
            break
        except ValueError:
            print("No es un numero")
    return numero

def main():
    numero = pedir_numero("¿Cuántos movimientos quieres que haga caballo?: ")
    A2 = n_potencia(A,numero-1)
    A3 = metodo_strassen(A2, A)
    print("El caballo tiene", np.sum(A3), "movimientos distintos con", numero, "movimientos")

if __name__ == "__main__":
    main()