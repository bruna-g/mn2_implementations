import numpy as np

def diferencasFinitasPVC1(N):
    
    deltaX = 1.0/N
    lateral = 1/deltaX**2
    centro = - (2/(deltaX**2) + 1)
    A = np.zeros((N-1, N-1))

    for i in range(N-1):
        if i > 0:
            A[i, i-1] = lateral

        A[i, i] = centro

        if i < N-2:
            A[i, i+1] = lateral

    b = np.zeros(N-1)
    b[N-2] = - lateral
    
    solucao = np.linalg.solve(A, b)
    return solucao

N = 8
pontos = np.linspace(0, 1, N+1)
solucao = diferencasFinitasPVC1(N)
print(f"Pontos: {pontos[1:N]}")
print(f"Solucao: ", solucao)
