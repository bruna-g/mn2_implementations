# aula 22
# METODO QR
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *
import math

def metodoQR(matA, n, e):
  matP = []
  matQ = []
  matR = []
  matAnew = []
  matAold = []
  matAbarra = []
  lamb = [0.0 for _ in range(n)]
  val = 100

  matP = matIdentidade(n)
  matAold = matA

  max_iter = 5
  iter_count = 0

  while val > e:
    (matQ, matR) = decomposicaoQR(matAold)
    matAnew = multMatrizMatriz(matR, matQ)
    matAold = matAnew.copy()
    matP = multMatrizMatriz(matP, matQ)
    val = somaDosQuadradosDosTermosAbaixoDaDiagonal(matAnew, n)
    iter_count += 1

    if iter_count == max_iter:
      print("Alcançou o número máximo de iterações sem convergência.")
      break
  
  for k in range(len(lamb)):
    lamb[k] = matAnew[k][k]
  
  return (matP, lamb, matAnew)

#------------------------------------------------------------

def decomposicaoQR(matA):
  matQT = []
  matJij = []
  matRnew = []
  matRold = []
  matR = []
  n = len(matA)

  matQT = matIdentidade(n)
  matRold = matA.copy()

  for j in range(n-1):
    for i in range(j+1, n):
      matJij = matrizJacobiBaseadaNoElemento_ij_DeRVelha(matRold, i, j) 
      matRnew = multMatrizMatriz(matJij, matRold)
      matRold = matRnew.copy()
      matQT = multMatrizMatriz(matJij, matQT)
      print("Matriz R_nova da iteração %d, %d" %(i, j))
      print(matRnew)
      print("\n")

  matQ = transposta(matQT)
  matR = matRnew.copy()
  return (matQ, matR)

#------------------------------------------------------------

def matrizJacobiBaseadaNoElemento_ij_DeRVelha(matA, i, j):
  matJij = []
  teta = 0.0
  e = 10**-6
  pi = 3.14159265358979323846
  n = len(matA)

  matJij = matIdentidade(n)
  if np.abs(matA[i][j]) <= e:
    return matJij
  
  if np.abs(matA[j][j]) <= e:
    if matA[i][j] < 0:
      teta = pi/2
    else:
      teta = -pi/2
  else:
    teta = math.atan((-matA[i][j])/(matA[j][j]))

  matJij[i][i] = math.cos(teta)
  matJij[j][j] = math.cos(teta)
  matJij[i][j] = math.sin(teta)
  matJij[j][i] = -math.sin(teta)

  return matJij

if __name__ == '__main__':
  matA = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  tamA = len(matA)
  erro = 10**-6

  (matP, lamb, matAnova) = metodoQR(matA, tamA, erro)
  print("Matriz P:")
  for i in range(tamA):
    print(matP[i])
  print("\n")
  
  print("Autovalores: ", lamb)

