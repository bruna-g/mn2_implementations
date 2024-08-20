# aula 19
# POTENCIA COM DESLOCAMENTO

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *
from tarefa_11_1 import potenciaInversa

'''matrizA = float(input("Insira a matriz A: "))
vetorInicial = float(input("Insira o vetor inicial: "))
tol = float(input("Insira a tolerância desejada: "))
desloc = float(input("Insira a tolerância desejada: "))'''

def potenciaComDeslocamento(matrizA, vetorInicial, e, desloc):
    n = len(matrizA)
    I = matIdentidade(n)
    IdDesloc = multEscalarMatriz(desloc, I)
    matANew = subtracaoMatrizMatriz(matrizA, IdDesloc)
    lambdaOld, xOld = potenciaInversa(matANew, vetorInicial, e)
    lambdaNew = lambdaOld + desloc
    xNew = xOld
    return lambdaNew, xNew


matrizA1 = [[5.0, 2.0, 1.0], 
           [2.0, 3.0, 1.0], 
           [1.0, 1.0, 2.0]]
print("Matriz A1: ")
for i in range(len(matrizA1)):
    print(matrizA1[i])
vetorInicial1 = [1.0, 1.0, 1.0]
tol1 = 0.000006
deslocamento1 = 1

lambdaNew1, xNew1 = potenciaComDeslocamento(matrizA1, vetorInicial1, tol1, deslocamento1)
print("autovalor da matriz 1 =", lambdaNew1, "\nautovetor da matriz 1 =", xNew1)
print("\n")


matrizA2 = [[-14.0, 1.0, -2.0], 
           [1.0, -1.0, 1.0], 
           [-2.0, 1.0, -11.0]]
print("Matriz A2: ")
for i in range(len(matrizA2)):
    print(matrizA2[i])
vetorInicial2 = [1.0, 1.0, 1.0]
tol2 = 0.000006
deslocamento2 = 1

lambdaNew2, xNew2 = potenciaComDeslocamento(matrizA2, vetorInicial2, tol2, deslocamento2)
print("autovalor da matriz 2 =", lambdaNew2, "\nautovetor da matriz 2 =", xNew2)
print("\n")


matrizA3 = [[40.0, 8.0, 4.0, 2.0, 1.0], 
           [8.0, 30.0, 12.0, 6.0, 2.0], 
           [4.0, 12.0, 20.0, 1.0, 2.0],
           [2.0, 6.0, 1.0, 25.0, 4.0],
           [1.0, 2.0, 2.0, 4.0, 5.0]]
print("Matriz A3: ")
for i in range(len(matrizA3)):
    print(matrizA3[i])
vetorInicial3 = [1.0, 1.0, 1.0]
tol3 = 0.000006
deslocamento3 = 1

lambdaNew3, xNew3 = potenciaComDeslocamento(matrizA3, vetorInicial3, tol3, deslocamento3)
print("autovalor da matriz 3 =", lambdaNew3, "\nautovetor da matriz 3 =", xNew3)
print("\n")