#aula 20

import math

def transposta(matriz):
  matriz_t = []
  for i in range(len(matriz[0])):
    linha = []
    for j in range(len(matriz)):
      linha.append(matriz[j][i])
    matriz_t.append(linha)
  return(matriz_t)

def magnitude(vetor):
  total = 0.0
  for i in range(len(vetor)):
    total += vetor[i] ** 2.0
  return math.sqrt(total)

def multEscalarVetor(escalar, vetor):
  for i in range(len(vetor)):
    vetor[i] = vetor[i] * escalar
  return vetor

def multEscalarMatriz(escalar, matriz): 
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      matriz[i][j] = matriz[i][j] * escalar
  return matriz

def multVetorVetorT(vetor1, vetor2):
  matriz = []
  for i in range(len(vetor1)):
    linha = []
    for j in range(len(vetor2)):
      linha.append(vetor1[i] * vetor2[j])
    matriz.append(linha)
  return matriz

def multMatrizMatriz(matriz_a, matriz_b):
    n = len(matriz_a)
    matriz_resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_resultado

def subtracaoVetorVetor(w, wl):
  sub = []
  for a in range(len(w)):
    sub.append(w[a] - wl[a])
  return sub

def subtracaoMatrizMatriz(matriz1, matriz2):
  matriz3 = []
  for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz1[0])):
      linha.append(matriz1[i][j] - matriz2[i][j])
    matriz3.append(linha)
  return matriz3

def Normalizar(vOld):
  total = 0.0
  x1 = vOld.copy()
  for l in range(len(vOld)):
    total = total + vOld[l]**2.0
  denominador = math.sqrt(total)
  for m in range(len(vOld)):
    x1[m] = vOld[m] / denominador
  return x1

def matIdentidade(tam):
  matI = [[0.0 for _ in range(tam)] for _ in range(tam)]
  for i in range(tam):
    for j in range(tam):
      if i == j:
        matI[i][j] = 1.0
  return matI

#-------------------------------------------------------------------

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
  Abarra = []
  H = []

  Abarra, H = metodoDeHouseHolder(matA, n)

  Abarra = [[round(elemento, 4) for elemento in linha] for linha in Abarra]

  H = [[round(elemento, 4) for elemento in linha] for linha in H]

  print("Matriz Abarra:")
  for i in range(n):
    print(Abarra[i])

  print("Matriz H:")
  for i in range(n):
    print(H[i])
