#aula_18
# POTENCIA REGULAR

from numpy import double
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *

#inicializando a matriz A
tamA = int(input("Informe o tamanho da matriz A: ")) 
matA = [[0.0 for _ in range(tamA)] for _ in range(tamA)] 

for i in range(tamA):
  for j in range(tamA):
    matA[i][j] = float(input("elemento %d %d: " %(i,j)))
#matA = [[5.0, 2.0, 1.0], [2.0, 3.0, 1.0], [1.0, 1.0, 2.0]]

#inicializando o vetor arbitrário
vOld = [] 
tamvOld = int(input("Informe o tamanho do vetor arbitrário: "))

for m in range(tamvOld):
  vOld.append(float(input("elemento %d: " %m)))
#vOld = [1.0, 1.0, 1.0]

#inicializando a tolerância do erro
E = double(input("Informe a tolerância do erro: "))
#E = 0.000006

#outputs
lambdaNew = 0.0 #step2
vNew = vOld.copy() #step3

lambdaOld = 0.0

while True:
  lambdaOld = lambdaNew #step4
  vOld = vNew.copy() #step5
  x1 = Normalizar(vOld) #step6
  vNew =  multVetorMatriz(x1, matA) #step7
  lambdaNew = multVetorVetor(x1, vNew) #step8
  if convergencia(lambdaOld, lambdaNew) < E: #step9
    break

print("O autovalor é: ", lambdaNew)
print("O vetor normalizado é: ")
for i in range(len(x1)):
  print("x1[%d]: " %i, x1[i])

#----------------------------------------------------------
#somente para confirmar // lembrar de tirar:
copia = x1.copy()

print("Multiplicando o autovetor pelo autovalor")
for h in range(len(x1)):
  x1[h] = x1[h] * lambdaNew
  print("x1[%d]: " %h, x1[h])

#multiplicar a matriz A pelo autovetor
print("Multiplicando a matriz A pelo autovetor")
for i in range(len(matA)):
  sum = 0.0
  for j in range(len(copia)):
    sum = sum + copia[j] * matA[i][j]
  print("y[%d]: " %i, sum)
