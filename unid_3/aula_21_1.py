# aula 21
# tarefa não foi pedida nas atividades do classroom
# METODO JACOBI

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *
import math
from unid_3.tarefa_12_1 import *

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
  iter = 0
  while val > e:
    (matAnew, matJ) = varreduraDeJacobi(matAold, n, iter)
    matAold = matAnew.copy()
    matP = multMatrizMatriz(matP, matJ)
    val = somaDosQuadradosDosTermosAbaixoDaDiagonal(matAnew, n)
    iter += 1
  
  for i in range(len(lamb)):
    lamb[i] = matAnew[i][i]
  
  return (matAnew, matP, lamb, matJ)

#------------------------------------------------------------------

def varreduraDeJacobi(matA, n, iter):
  matJ = []
  matJij = []
  matAnew = []
  matAold = []
  matAbarra = []
  # matP = []
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

  matAbarra = matAnew.copy()
  matAbarraprint = [[round(elemento, 4) for elemento in linha] for linha in matAbarra]
  print("matAbarra da iteração %d: " %iter)
  for m in range(tamA):
    print(matAbarraprint[m])
  print("\n")
      
  return (matAbarra, matJ)

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

def varreduraDeJacobiADAPTADA(matA, n, iter):
  matJ = []
  matJij = []
  matAnew = []
  matAold = []
  matAbarra = []
  # matP = []
  tamA = n

  matJ = matIdentidade(tamA)
  matAold = matA.copy()

  for j in range(n-1):
    for i in range(j+1, n):
      matJij = matrizJacobiBaseadaNoElemento_ij_DaMatrizVelha(matAold, i, j, n)
      Jij_T = transposta(matJij)
      aux = multMatrizMatriz(Jij_T, matAold)
      matAnew = multMatrizMatriz(aux, matJij)

      print("matAnew da iteração %d: " %iter)
      for t in range(len(matAnew)):
        print(matAnew[t])

      matAold = matAnew.copy()
      matJ = multMatrizMatriz(matJ, matJij)

  matAbarra = matAnew.copy()
  matAbarraprint = [[round(elemento, 4) for elemento in linha] for linha in matAbarra]
  print("matAbarra da iteração %d: " %iter)
  for m in range(tamA):
    print(matAbarraprint[m])
  print("\n")
      
  return (matAbarra, matJ)

#------------------------------------------------------------------

if __name__== '__main__':
  matA = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  tamA = len(matA)
  (matAnew, matP, lamb, matJ) = metodoDeJacobi(matA, tamA, 10**-6)

  matAnew = [[round(elemento, 4) for elemento in linha] for linha in matAnew]
  matP = [[round(elemento, 4) for elemento in linha] for linha in matP]
  matJ = [[round(elemento, 4) for elemento in linha] for linha in matJ]

  print("Matriz diagonal A: ")
  for i in range(tamA):
    print(matAnew[i])
  print("\n")

  print("Matriz acumulada P:")
  for i in range(tamA):
    print(matP[i])
  print("\n")

  print("Autovalores: ", lamb)
  print("\n")

  #pares de autovalores e autovetores da matA:
  for i in range(tamA):
    print("Autovalor %d: " %(i+1), lamb[i])
    #imprimir as colunas de P
    print("Autovetor %d: [ " %(i+1), end="" )
    for j in range(tamA):
      print(matP[j][i], end=" ")
    print("]")
    print("\n")

  


  