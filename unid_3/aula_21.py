#aula 21
#tarefa não foi pedida nas atividades do classroom
# METODO JACOBI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *
import math

def metodoDeJacobi(matA, n, e):
  matP = []
  matJ = []
  matAnew = []
  matAold = []
  # matAbarra = []
  tamA = n

  lamb = [0.0 for _ in range(n)]
  val = 100.0

  matP = matIdentidade(tamA)
  matAold = matA.copy()

  while val > e:
    (matAnew, matJ) = varreduraDeJacobi(matAold, n)
    matAold = matAnew.copy()
    matP = multMatrizMatriz(matP, matJ)
    val = somaDosQuadradosDosTermosAbaixoDaDiagonal(matAnew, n)
  
  for i in range(len(lamb)):
    lamb[i] = matAnew[i][i]
  
  return (matP, lamb)

#------------------------------------------------------------------

def varreduraDeJacobi(matA, n):
  matJ = []
  matJij = []
  matAnew = []
  matAold = []
  matmatP = []
  tamA = n

  matJ = matIdentidade(tamA)
  matAold = matA.copy()

  for j in range(n-1):
    for i in range(j+1, n):
      matJij = matrizJacobiBaseadaNoElemento_ij_DaMatrizVelha(matAold, i, j, n)
      Jij_T = transposta(matJij)
      aux = multMatrizMatriz(Jij_T, matAold)
      matAnew = multMatrizMatriz(aux, matJij)
      matAold = matAnew.copy()
      matJ = multMatrizMatriz(matJ, matJij)

  matmatP = matAnew.copy()
  return (matmatP, matJ)

#------------------------------------------------------------------

def matrizJacobiBaseadaNoElemento_ij_DaMatrizVelha(matA, i, j, n):
  matI = []
  Jij = []
  teta = e = 10**-6
  Jij = matIdentidade(n)
  pi = math.pi

  if abs(matA[i][j]) <= e:
    return Jij
  if abs(matA[i][i] - matA[j][j]) <= e:
    teta = pi/4
  else:
    teta = 0.5 * math.atan((-2) * matA[i][j] / (matA[i][i] - matA[j][j]))

  Jij[i][i] = math.cos(teta)
  Jij[j][j] = math.cos(teta)
  Jij[i][j] = math.sin(teta)
  Jij[j][i] = -math.sin(teta)

  return Jij

#------------------------------------------------------------------

if __name__== '__main__':
  matA = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  tamA = len(matA)
  (matP, lamb) = metodoDeJacobi(matA, tamA, 10**-6)

  matP = [[round(elemento, 4) for elemento in linha] for linha in matP]

  print("Matriz P:")
  for i in range(tamA):
    print(matP[i])
  print("Autovalores: ", lamb)