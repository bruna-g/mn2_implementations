# aula 20
# METODO HOUSEHOLDER

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *
from tarefa_11_1 import *
from tarefa_10 import *

def matriz_metodoDeHouseHolder(matA, i):
  tamA = len(matA)
  matI = matIdentidade(tamA)
  w = [0.0 for _ in range(tamA)] 
  wl = [0.0 for _ in range(tamA)]
  H = [0.0 for _ in range(tamA)] 
  N = []
  n = []

  for k in range(i+1, tamA):
    w[k] = matA[k][i]
  
  Lw = magnitude(w)

  wl[i+1] = Lw

  N = subtracaoVetorVetor(w, wl)

  n = Normalizar(N)

  nnT = multVetorVetorT(n, n)
  dobro_nnT = multEscalarMatriz(2.0, nnT)
  H = subtracaoMatrizMatriz(matI, dobro_nnT)

  return H

#-------------------------------------------------------------------

def metodoDeHouseHolder(matA, n):
  H = []
  Ht = []
  Hnew = [] #Hnew eh Hi
  Anew = [] #Anew eh Ai
  Abarra = []

  H = matIdentidade(n)
  Aold = matA.copy() #Aold eh Ai-1

  for i in range(n-2):
    Hnew = matriz_metodoDeHouseHolder(Aold, i)
    Ht = transposta(Hnew)
    aux = multMatrizMatriz(Ht, Aold)
    Anew = multMatrizMatriz(aux, Hnew)
    Aold = Anew.copy()
    H = multMatrizMatriz(H, Hnew)
  Abarra = Anew.copy()
  return(Abarra, H)

if __name__ == "__main__":
  #matA =  [[3.0,1.0,0.0,0.0,0.0],[1.0,4.0,3.0,0.0,0.0],[0.0,3.0,5.0,2.0,1.0],[0.0,0.0,2.0,6.0,3.0],[0.0,0.0,1.0,3.0,8.0]]
  matA = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  tamA = len(matA)

  n = tamA

  Abarra, H = metodoDeHouseHolder(matA, n)

  Abarra = [[round(elemento, 4) for elemento in linha] for linha in Abarra]
  H = [[round(elemento, 4) for elemento in linha] for linha in H]

  print("Matriz Abarra:")
  for i in range(n):
    print(Abarra[i])
  print("\n")

  print("Matriz H:")
  for i in range(n):
    print(H[i])
  print("\n")
  print("------------------------------------------")
  
  #Use os métodos da potência para encontrar os autovalores e autovetores da matriz Abarra:
  (autov, autovet) = potenciaRegular(Abarra, [1.0]*5, 10**-6)

  print("potencia regular:")
  print("O autovalor de Abarra é: ", autov)
  print("Os autovetores de Abarra são: ", autovet)
  print("\n")

  #usando a matriz H e os autovetores da matriz Abarra, encontre os autovetores da matriz A:
  autovet = Normalizar(autovet)
  autovet = multVetorMatriz(autovet, H)
  print("Os autovetores de A são: ", autovet)

  #encontre os autovalores da matriz A:
  autov = multVetorVetor(autovet, multVetorMatriz(autovet, matA))
  print("Os autovalores de A são: ", autov)

