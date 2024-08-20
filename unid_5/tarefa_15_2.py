import numpy as np

def pvc2(N, valor):
    dx = 1.0/N
    dy = 1.0/N
    coef_y = 1/(dy**2)
    coef_x = 1/(dx**2)
    centro = - (2/(dx**2) + 2/(dy**2))
    tam = (N-1) * (N-1)
    A = np.zeros((tam, tam))
    k = 0
    y = 0

    for i in range(tam):
        if i > 0:
            k = k + 1
            if k%(N-1) != 0: 
                A[i][i-1] = coef_y
            else:
                A[i][i-1] = 0
        if i > (N-2):
            A[i][i-(N-1)] = coef_x
        A[i][i] = centro
        if i < tam-(N-1):
            A[i][i+(N-1)] = coef_x
        if i < tam-1:
            y = y + 1
            if y%(N-1) !=0: 
                A[i][i+1] = coef_y
            else:
                A[i][i+1] = 0
    

    b = np.array([valor for i in range(tam)])

    solucao = np.linalg.solve(A, b)

    return solucao

N = 4
valor = 4
solucao = pvc2(N, valor)
print(f"{solucao}")