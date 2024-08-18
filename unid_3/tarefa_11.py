import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *

'''matrizA = float(input("Insira a matriz A: "))
vetorInicial = float(input("Insira o vetor inicial: "))
tol = float(input("Insira a tolerância desejada: "))'''

matrizA = [[5.0, 2.0, 1.0], 
           [2.0, 3.0, 1.0], 
           [1.0, 1.0, 2.0]]
print("Matriz A:\n", matrizA[0], "\n", matrizA[1], "\n", matrizA[2])
vetorInicial = [1.0, 1.0, 1.0]
tol = 0.000006

def potenciaRegular(matrizA, vetorInicial, E):
    L, U = decompLU(matrizA)
    lambdaNovo = 0.0
    vetorNovo = vetorInicial

    while True:
        lambdaVelho = lambdaNovo
        vetorVelho = vetorNovo
        x1_velho = Normalizar(vetorVelho)
        vetorNovo = solverLU(matrizA, x1_velho)
        lambdaNovo = np.transpose(x1_velho).dot(vetorNovo)
        if convergencia(lambdaVelho ,lambdaNovo) <= tol:
            break
    lambdaN = 1/lambdaNovo
    xn = x1_velho
    print("\nlambdaN = ", lambdaN, "\nXn = ", xn)

potenciaRegular()




