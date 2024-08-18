import numpy as np
import math

#tarefa_10 ---------------------------------------------
def Normalizar(vOld):
  total = 0.0
  x1 = []
  for l in range(len(vOld)):
    total = total + vOld[l]**2.0
  denominador = math.sqrt(total)

  for m in range(len(vOld)):
    vOld[m] = vOld[m] / denominador

  x1 = vOld.copy() #x1 é o vOld normalizado
  return x1

def Normalizar2(vOld):
  total = 0.0
  x1 = vOld.copy()
  for l in range(len(vOld)):
    total = total + vOld[l]**2.0
  denominador = math.sqrt(total)
  for m in range(len(vOld)):
    x1[m] = vOld[m] / denominador
  return x1

def multVetorMatriz(vOld, matA):
  vNew = []
  for i in range(len(matA)):
    sum = 0.0
    for j in range(len(vOld)):
      sum = sum + vOld[j] * matA[i][j]
    vNew.append(sum)
  return vNew #resulta num vetor

def multVetorVetor(x1, vNew):
  lambdaNew = 0.0
  for i in range(len(x1)):
    lambdaNew += x1[i] * vNew[i]
  return lambdaNew # resulta num valor escalar

def convergencia(lambdaOld, lambdaNew):
  conv = abs((lambdaNew - lambdaOld) / lambdaNew)
  return conv


#tarefa_11 ---------------------------------------------
def decompLU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        # Diagonal da matriz L é composta por 1s
        L[i][i] = 1
        # Calcula os elementos da matriz U
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        # Calcula os elementos da matriz L
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U

def solverLU(A, y):
    L, U = decompLU(A)
    # Passo 1: Resolver Lb = y (b é o vetor intermediário)
    n = len(y)
    b = np.zeros_like(y, dtype=float)
    for i in range(n):
        b[i] = y[i] - sum(L[i][j] * b[j] for j in range(i))
    # Passo 2: Resolver Ux = b (encontrar o vetor x)
    x = np.zeros_like(y, dtype=float)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    return x


#tarefa_12 ---------------------------------------------
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



def matIdentidade(tam):
  matI = [[0.0 for _ in range(tam)] for _ in range(tam)]
  for i in range(tam):
    for j in range(tam):
      if i == j:
        matI[i][j] = 1.0
  return matI


#tarefa_12_1 ---------------------------------------------
def somaDosQuadradosDosTermosAbaixoDaDiagonal(matriz, n):
  soma = 0.0
  for i in range(n):
    for j in range(n):
      if i > j:
        soma += matriz[i][j] ** 2.0
  return soma

