# aula 22
# METODO QR

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
  # matAbarra = []
  lamb = [0.0 for _ in range(n)]
  val = 100.0

  matP = matIdentidade(n)
  matAold = matA.copy()

  while val > e:
    (matQ, matR) = decomposicaoQR(matAold, n)
    matAnew = multMatrizMatriz(matR, matQ)
    matAold = matAnew.copy()
    matP = multMatrizMatriz(matP, matQ)
    val = somaDosQuadradosDosTermosAbaixoDaDiagonal(matAnew, n)
  
  for i in range(len(lamb)):
    lamb[i] = matAnew[i][i]
  
  return (matP, lamb)

#------------------------------------------------------------

def decomposicaoQR(matA, n):
  matQT = []
  matJij = []
  matRnew = []
  matRold = []
  matR = []

  matQT = matIdentidade(n)
  matRold = matA.copy()

  for j in range(n-1):
    for i in range(j+1, n):
      matJij = matrizJacobiBaseadaNoElemento_ij_DeRVelha(matRold, i, j, n) 
      matRnew = multMatrizMatriz(matJij, matRold)
      matRold = matRnew.copy()
      matQT = multMatrizMatriz(matJij, matQT)

  matQ = transposta(matQT)
  matR = matRnew.copy()
  return (matQ, matR)

#------------------------------------------------------------

def matrizJacobiBaseadaNoElemento_ij_DeRVelha(matA, i, j, n):
  matI = matIdentidade(n)
  matJij = []
  teta = e = 10**-6
  pi = math.pi

  matJij = matI.copy()
  if abs(matA[i][j] <= e):
    return matJij
  if abs(matA[j][j] <= e):
    if matA[i][j] < 0:
      teta = pi/2
    else:
      teta = -pi/2
  else:
    teta = math.atan(-matA[i][j]/matA[j][j])

  matJij[i][i] = math.cos(teta)
  matJij[j][j] = math.cos(teta)
  matJij[i][j] = math.sin(teta)
  matJij[j][i] = -math.sin(teta)

  return matJij

if __name__ == '__main__':
  matA = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  tamA = len(matA)

  (matP, lamb) = metodoQR(matA, tamA, 10**-6)
  print("Matriz P:")
  for i in range(tamA):
    print(matP[i])
  print("Autovalores: ", lamb)