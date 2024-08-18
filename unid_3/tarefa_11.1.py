import sys
import os
from tarefa_11 import potenciaInversa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *

'''matrizA = float(input("Insira a matriz A: "))
vetorInicial = float(input("Insira o vetor inicial: "))
tol = float(input("Insira a tolerância desejada: "))
desloc = float(input("Insira a tolerância desejada: "))'''

matrizA = [[5.0, 2.0, 1.0], 
           [2.0, 3.0, 1.0], 
           [1.0, 1.0, 2.0]]
print("Matriz A:\n", matrizA[0], "\n", matrizA[1], "\n", matrizA[2], "\n")
vetorInicial = [1.0, 1.0, 1.0]
tol = 0.000006
deslocamento = 1

def potenciaComDeslocamento(matrizA, vetorInicial, e, desloc):
    n = len(matrizA)
    I = matIdentidade(n)
    IdDesloc = multEscalarMatriz(desloc, I)
    matANew = subtracaoMatrizMatriz(matrizA, IdDesloc)
    lambdaOld, xOld = potenciaInversa(matANew, vetorInicial, e)
    lambdaNew = lambdaOld + desloc
    xNew = xOld
    return lambdaNew, xNew

lambdaNew, xNew = potenciaComDeslocamento(matrizA, vetorInicial, tol, deslocamento)
print("lambdaN =", lambdaNew, "\nxn =", xNew)