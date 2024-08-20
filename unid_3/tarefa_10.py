# aula 18
# POTENCIA REGULAR

from numpy import double
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auxiliares import *


def potenciaRegular(matA, vOld, E):
  lambdaNew = 0
  vNew = []
  vNew = vOld.copy()

  while True:
    lambdaOld = lambdaNew
    vOld = vNew.copy()
    x1Old = Normalizar(vOld)
    vNew = multVetorMatriz(x1Old, matA)
    lambdaNew = multVetorVetor(x1Old, vNew)
    if convergencia(lambdaOld, lambdaNew) < E:
      break
  return (lambdaNew, x1Old)

if __name__ == '__main__':
  matA1 = [[5.0, 2.0, 1.0], [2.0, 3.0, 1.0], [1.0, 1.0, 2.0]]
  vOld1 = [1.0, 1.0, 1.0]
  E = 0.000006
  (lambdaNew1, x1Old1) = potenciaRegular(matA1, vOld1, E)
  print("O autovalor de A1 é: ", lambdaNew1)
  print("Os autovetores de A1 são: ", x1Old1)
  print("\n")

  matA2 = [[40, 8, 4, 2, 1],[8, 30, 12, 6, 2],[4, 12, 20, 1, 2],[2, 6, 1, 25, 4],[1, 2, 2, 4, 5]]
  vOld2 = [1.0, 1.0, 1.0, 1.0, 1.0]
  E = 0.000006
  (lambdaNew2, x1Old2) = potenciaRegular(matA2, vOld2, E)
  print("O autovalor de A2 é: ", lambdaNew2)
  print("Os autovetores de A2 é: ", x1Old2)
